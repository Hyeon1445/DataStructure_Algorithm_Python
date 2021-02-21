Q=[]

def isEmpty():
    return len(Q)==0

def enqueue(data):
    Q.append(data)
#O(1)

def dequeue():
    if not isEmpty():
        return Q.pop(0)
#O(n)
#삭제하고 한칸씩 앞으로 당겨져야 함

def peek():
    if not isEmpty():
        return Q[0]
# 책에는 Q[-1]로 나와있는데
# Q[0]이 맞는거같음
# peek함수는 나가기 직전인(제일 먼저 들어온) 데이터 출력(삭제는 안함)




