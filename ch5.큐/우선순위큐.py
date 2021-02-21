#들어온 순서와 상관없이 우선순위가 높은 데이터가 먼저 출력
#가장 효율적인 우선순위 큐의 구현 방법은 힙(heap)

class PriorityQueue:
    def __init__(self):
        self.PQ=[]
    
    def isEmpty(self):
        return len(self.PQ)==0
    
    def size(self):
        return len(self.PQ)

    def clear(self):
        self.PQ=[]

#여기서는 그냥 값으로 우선순위 매김
#이상적인 구조는 (데이터,우선순위)의 튜플 입력

    def enqueue(self,data):
        self.PQ.append(data) #그냥 맨 뒤에 삽입
        #삽입 O(1)

    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest=0
            for i in range(1,self.size()):
                if self.PQ[i]>self.PQ[highest]:
                    highest=i
            return highest
    #O(n) 제일 큰 값 탐색

    def dequeue(self):
        highest=self.findMaxIndex()
        if highest is not None:
            return self.PQ.pop(highest) #우선순위 제일 큰거 반환
    #O(n) 찾아서 반환
    
    def peek(self):
        highest=self.findMaxIndex()
        if highest is not None:
            return self.PQ[highest]

q=PriorityQueue()
q.enqueue(34)
q.enqueue(18)
q.enqueue(27)
q.enqueue(45)
q.enqueue(15)
print("PQueue:",q.PQ)

while not q.isEmpty():
    print("Max Priority=",q.dequeue())
