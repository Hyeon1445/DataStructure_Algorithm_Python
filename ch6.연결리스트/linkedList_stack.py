class Node:
    def __init__(self,data,next=None):
        #link 디폴트 : None
        self.data=data
        self.next=next
        #파이썬) 클래스의 모든 멤버는 self로 접근해야 하기 때문에 매개변수(data)와 데이터 멤버(self.data) 이름이 같아도 된다

class LinkedStack:
    def __init__(self):
        self.head=None
    
    def isEmpty(self):
        return self.head==None

    def clear(self):
        self.head=None

    def push(self,data):
        n=Node(data,self.head) #노드 만들고, data입력
        self.head=n #head에 삽입노드 연결

        #head -> A -> B -> C -> D 에서 E 삽입
        #head -> E -> A -> B -> C -> D

    def pop(self):
        if not self.isEmpty():#빈 스택이 아니면
            n=self.head 
            self.head=n.next #head를 next에 연결
            return n.data #삭제한 데이터 반환

    def size(self):
        node=self.head
        count=0
        while not node==None: #마지막 노드까지 하나씩 옮겨가면서 개수 센다
            node=node.link
            count+=1
        return count

    def display(self,msg='LinkedStack:'):
        print(msg,end=" ")
        node=self.head
        while not node==None:
            print(node.data,end=' ')
            node=node.next
        print()


odd=LinkedStack()
even=LinkedStack()

for i in range(10):
    if(i%2==0):
        odd.push(i)
    else:
        even.push(i)

odd.display('odd')
#8 6 4 2 0
even.display('even')
#9 7 5 3 1