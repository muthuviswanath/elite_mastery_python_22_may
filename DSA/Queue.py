def createQueue():
    queue = []
    return queue

def enque(queue,element):
    queue.append(element)

def deque(queue):
    if(len(queue)==0):
        print("Cannot dequeue")
    else:
        queue.pop(0)

my_queue = createQueue()
enque(my_queue,123)
enque(my_queue,345)
enque(my_queue,390)
print(my_queue)
deque(my_queue)
print(my_queue)
deque(my_queue)
print(my_queue)
deque(my_queue)
print(my_queue)
deque(my_queue)