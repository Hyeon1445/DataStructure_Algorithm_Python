class Node:
    def __init__(self,data,next=None):
        #link 디폴트 : None
        self.data=data
        self.next=next


class CircularLinkedQueue:
    def __init__(self):
        self.tail=None
        #front=rear.next

    def isEmpty(self):
        return self.tail==None
    
    def clear(self):
        self.tail=None
    
    def peek(self):
        if not self.isEmpty():
            return self.tail.next.data

    def enqueue(self,data):
        node=Node(data,None)
        if self.isEmpty():#첫 삽입
            node.next=node#그 다음노드도 자신
            self.tail=node#tail도 삽입노드 
        else:#첫 삽입 아님
            node.next=self.tail.next
            self.tail.next=node
            self.tail=node#tail 위치에 노드 삽입

    def dequeue(self):
        if not self.isEmpty():#비어있지 않은 경우 삭제
            data=self.tail.next.data#front=rear.next의 데이터 반환
            if self.tail.next==self.tail:#노드가 하나뿐
                self.tail=None
            else:#노드가 둘 이상
                self.tail.next=self.tail.next.next# 뺄 노드의 전 후를 이어준다
            return data

    def size(self):
        if self.isEmpty():
            return 0#비어있으면 0
        else:
            count=1
            node=self.tail.next
            while not node==self.tail:#반복문 돌려서 tail까지의 개수 세기
                node=node.next
                count+=1
            return count

    def display(self,msg='CircularLinkedQueue:'):
        print(msg,end='')
        if not self.isEmpty():
            node=self.tail.next#tail의 next는 front
            while not node==self.tail:
                print(node.data,end=' ')
                node=node.next
            print(node.data,end=' ')
        print()

q=CircularLinkedQueue()
for i in range(8):
    q.enqueue(i)

q.display()
for i in range(5):
    q.dequeue()
q.display()
for i in range(8,14):
    q.enqueue(i)
q.display()
print('size:', q.size())