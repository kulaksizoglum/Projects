import threading
import time
import random

class ConSet:
    def __init__(self):
        self.state = {}
        self.lock = threading.Lock()

    def insert(self, newItem):
        with self.lock:
            self.state[newItem] = True
    '''
    def pop(self):
        while True:
           with self.lock:
                if self.state:
                    for item, val in self.state.items():
                        if val:
                            self.state[item] = False
                            return item
    '''
    def pop(self):
        while True:
            self.lock.acquire()
            if self.state != {}:
                for item, val in self.state.items():
                    if val:
                        self.state[item] = False
                        self.lock.release()
                        return item
            else:
                self.lock.release()
                time.sleep(0.1)

    def printSet(self):
        with self.lock:
            for item, val in self.state.items():
                print(f'{item}: {val}')

n = 10
mailboxes = [ConSet() for _ in range(n)]
print_lock = threading.Lock()
def nodeWork(node_id, n):
    notFound=1
    i=0
    while(notFound):    
       

        i+=1
        random_num = random.randint(0, n**2)
        with print_lock:
           print(f"Node {node_id} proposes value {random_num} for round {i}.") 
  
        message = (random_num, node_id)
        for mailbox in mailboxes:
            mailbox.insert(message)

        received_messages = []
        for _ in range(n):
            received_messages.append(mailboxes[node_id].pop())
        max_pair = max(received_messages, key=lambda x: x[0])
        max_value = max_pair[0]
        max_index = max_pair[1]
        count_max_values = sum(1 for pair in received_messages if pair[0]==max_value)

        if count_max_values == 1:
            with print_lock:
               print(f"Node {node_id} decided {max_index} as the leader.")
               
            notFound=0
        
        

threads = []
for i in range(n):
    thread = threading.Thread(target=nodeWork, args=(i, n))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

