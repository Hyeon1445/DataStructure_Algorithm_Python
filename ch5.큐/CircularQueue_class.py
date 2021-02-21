MAX_QSIZE=10

class CircularQueue:
    def __init__(self):
        self.front=0
        self.rear=0
        self.Q=[None]*MAX_QSIZE
        # [None,None,None,None,None,None,None,None,None,None]

    def isEmpty(self):
        return self.front==self.rear

    def isFull(self):
        return self.front==(self.rear+1)%MAX_QSIZE

    def clear(self):
        self.front=self.rear

    def enqueue(self,data):
        if not self.isFull():
            self.rear=(self.rear+1)%MAX_QSIZE #rear 한칸 뒤로
            self.Q[self.rear]=data

    def dequeue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%MAX_QSIZE#front 한칸 뒤로
            return self.Q[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.Q[(self.front+1)%MAX_QSIZE]

    def size(self):
        return (self.rear-self.front+MAX_QSIZE)%MAX_QSIZE

    def display(self):
        out=[]
        if self.front<self.rear:
            out=self.Q[self.front+1:self.rear+1]
        else:
            out=self.Q[self.front+1:MAX_QSIZE]+self.Q[0:self.rear+1]
        print("[f=%s,r=%d]==>"%(self.front,self.rear),out)

q=CircularQueue()
for i in range(8):
    q.enqueue(i)
q.display()

for i in range(5):
    q.dequeue()
q.display()
for i in range(8,14):
    q.enqueue(i)
q.display()
