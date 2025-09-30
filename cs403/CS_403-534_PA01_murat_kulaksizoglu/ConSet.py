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

    def pop(self):
        while True:
            with self.lock:
                if self.state:
                    for item, val in self.state.items():
                        if val:
                            self.state[item] = False
                            return item

    def printSet(self):
        with self.lock:
            for item, val in self.state.items():
                print(f'{item}: {val}')
        





def thread1_function(con_set):
    print("Start 1")
    item = con_set.pop()
    con_set.insert(1)
    con_set.printSet()
    print("End 1")

    
    print(f'Thread 1 popped item: {item}')

def thread2_function(con_set):
    print("Start 2")
    con_set.insert(3)
    con_set.insert(4)
    con_set.printSet()
    print("end 2")


con_set = ConSet()

thread1 = threading.Thread(target=thread1_function, args=(con_set,))
thread2 = threading.Thread(target=thread2_function, args=(con_set,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

