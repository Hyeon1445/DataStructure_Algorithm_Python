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

def isValidPos(x,y):
    if x<0 or y<0 or x>=MAZE_SIZE or y>=MAZE_SIZE:
        return False
    else:
        return map[y][x]=='0' or map[y][x]=='x'

def BFS():
    que=CircularQueue()
    que.enqueue((0,1))#시작위치, DFS와의 차이점
    print('BFS: ')

    while not que.isEmpty():
        here=que.dequeue() # DFS와의 차이점
        print(here,end='->')
        x,y=here
        if(map[y][x]=='x'):
            return True
        else:
            map[y][x]='.'#지나간자리 표시
            if isValidPos(x,y-1):que.enqueue((x,y-1))
            if isValidPos(x,y+1):que.enqueue((x,y+1))                
            if isValidPos(x-1,y):que.enqueue((x-1,y))
            if isValidPos(x+1,y):que.enqueue((x+1,y))
    return False

map=[['1','1','1','1','1','1'],
    ['e','0','1','0','0','1'],
    ['1','0','0','0','1','1'],
    ['1','0','1','0','1','1'],
    ['1','0','1','0','0','x'],
    ['1','1','1','1','1','1']] 

MAZE_SIZE=6
result=BFS()

if result:
    print('->미로 탐색 성공')
else:
    print('->미로 탐색 실패')

