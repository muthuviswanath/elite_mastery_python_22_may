class CircularQueue:

    def __init__(self,size):
        self.size = size
        self.queue = [None]  * size
        self.front = self.rear = -1
    
    def enqueue(self,element):
        if(self.rear+1)%self.size == self.front:
            print("The queue is full")
        elif(self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = element
        else:
            self.rear = self.rear+1
            self.queue[self.rear] = element
    
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        elif(self.front  == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = self.front+1
            return temp
        
    def  printQueue(self):
        if(self.front == -1):
            print("No element in the queue")
        elif(self.rear >= self.front):
            print()
            for i in range(self.front,self.rear+1):
                print(self.queue[i], end=" ")
        else:
            print()
            for i in range (self.head,self.size):
                print(self.queue[i],end=" ")
            for i in range (self.tail+1):
                print(self.queue[i], end=" ")
            print()    


cq = CircularQueue(5)
cq.enqueue(10);cq.enqueue(20)
cq.enqueue(30);cq.enqueue(40)
cq.enqueue(50)
cq.printQueue()
cq.dequeue()
cq.printQueue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.printQueue()