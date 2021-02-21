class stack:
    def __init__(self):
        self.st=[]

    def isEmpty(self):
        return len(self.st)==0

    def push(self,data):
        self.st.append(data)
    #리스트의 맨 뒤에 data추가
    #O(1)

    def pop(self):
        if not self.isEmpty():
            return self.st.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.st[-1]

    def size(self):
        return len(self.st)

    def clear(self):
        self.st=[]



map=[['1','1','1','1','1','1'],
    ['e','0','0','0','0','1'],
    ['1','0','1','0','1','1'],
    ['1','1','1','0','0','x'],
    ['1','1','1','0','1','1'],
    ['1','1','1','1','1','1']]
#1은 막혀있음/ 0은 길/ e는 시작위치/ x는 목적지

MAZE_SIZE=6


def isValidPos(x,y):
    if x<0 or y<0 or x>=MAZE_SIZE or y>=MAZE_SIZE:
        return False
    else:
        return map[y][x]=='0' or map[y][x]=='x'

def DFS():
    ss=stack()
    ss.push((0,1))#x튜플 삽입
    print('DFS:')

    while not ss.isEmpty():
        here=ss.pop()
        print(here,end="->")
        (x,y)=here
        if(map[y][x]=='x'):
            return True
        else:
            map[y][x]='.'#지나왔다고 표시함
            if isValidPos(x,y-1):ss.push((x,y-1))
            if isValidPos(x,y+1):ss.push((x,y+1))
            if isValidPos(x-1,y):ss.push((x-1,y))
            if isValidPos(x+1,y):ss.push((x+1,y))
            #4방향을 갈 수 있으면 스택에 삽입한다
        print("현재 스택:",ss.st)
    return False

result=DFS()
if result:
    print('->미로탐색성공')
else:
    print('->미로탐색실패')
