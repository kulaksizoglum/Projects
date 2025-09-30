from abc import abstractmethod
import multiprocessing
import zmq
import json
import os
import time

class MapReduce:
    def __init__(self, num_workers):
        self.num_workers = num_workers

    @abstractmethod
    def Map(self, map_input):
        pass
    @abstractmethod
    def Reduce(self, reduce_input):
        pass

    def start(self, filename):
        input_data=[]
        with open(filename, 'r') as file:
            for line in file:
                values = line.strip().split('\t')
                edge = tuple(map(int, values))
                input_data.append(edge)
        processes = []

        producer_process = multiprocessing.Process(target=self.Producer, args=(input_data,))
        processes.append(producer_process)

        for _ in range(self.num_workers):
            consumer_process = multiprocessing.Process(target=self.Consumer, args=())
            processes.append(consumer_process)

        result_collector_process = multiprocessing.Process(target=self.ResultCollector, args=())
        processes.append(result_collector_process)

        for process in processes:
            process.start()

        for process in processes:
            process.join()

    def Producer(self, input_data):
        piece_size = len(input_data) // self.num_workers
        remaining = len(input_data) % self.num_workers
        

        context = zmq.Context()
        producer_socket = context.socket(zmq.PUSH)
        producer_socket.bind("tcp://127.0.0.1:5555")
        start=0
        for i in range(self.num_workers):
            if i < remaining:
                end = start + piece_size + 1
            else:
                end = start + piece_size
            piece = input_data[start:end]
            start = end
            producer_socket.send_json(piece)
            time.sleep(0.1)
        


    def Consumer(self):

        context = zmq.Context()
        consumer_socket = context.socket(zmq.PULL)
        consumer_socket.connect("tcp://127.0.0.1:5555")
        
        while(True):
            try:
                piece = consumer_socket.recv_json(flags=0)
                if piece != None:
                    break
            except zmq.Again:
                continue
        consumer_socket.close()
        context.term()
        
        partial_result = self.Map(piece)

        
        context = zmq.Context()
        result_socket = context.socket(zmq.PUSH)
        result_socket.connect("tcp://127.0.0.1:5558")
        result_socket.send_json(partial_result)
        

    def ResultCollector(self):

        context = zmq.Context()
        result_socket = context.socket(zmq.PULL)
        result_socket.bind("tcp://127.0.0.1:5558")
        partial_results = []

        for _ in range(self.num_workers):
            partial_result = result_socket.recv_json()
            partial_results.append(partial_result)
    

        final_result = self.Reduce(partial_results)
        with open("results.txt", "w") as result_file:
            result_file.write(json.dumps(final_result))


