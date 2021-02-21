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

    def getNode(self,pos):
        if pos<0:
            return None
        node=self.head
        while pos>0 and node!=None:
            node=node.next
            pos-=1
        return node
    #해당 위치의 노드 찾아서 반환

    def getEntry(self,pos):
        node=self.getNode(pos)
        if node==None:
            return None
        else:
            return node.data
    #해당 위치의 데이터값 반환

    def replace(self,pos,data):
        node=self.getNode(pos)
        if node!=None:
            node.data=data
    #해당 위치의 데이터값 바꾸기

    def find(self,data):
        node=self.head
        while node is not None:
            if node.data:
                return node #찾으면 해당 노드 반환
            node=node.next
        return node # 못찾으면 None 노드 반환
    #데이터값으로 노드 찾아서 반환하기

    def insert(self,pos,elem):
        before=self.getNode(pos-1)
        if before==None:#첫 위치에 삽입할 때
            self.head=Node(elem.self.head)#head에 삽입
        else:
            node=Node(elem,before.next) #D -> B
            before.next=node # A -> D
        #head -> A -> B -> C
        #head -> A -> D -> B -> C
        #before을 찾기 위해 O(n)걸림 (before위치 알고있다면 O(1))

    def delete(self,pos):
        before=self.getNode(pos-1)
        if before==None: #맨 첫번째 위치한 노드 삭제
            if self.head is not None:#연결리스트가 비어 있지 않다면
                self.head=self.head.next
        elif before.next!=None:#첫번째가 아닌 다른 노드 삭제
            before.next=before.next.next # A -> C연결

        #head -> A -> B -> C
        #head -> A -> C

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