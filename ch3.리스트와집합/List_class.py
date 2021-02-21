class ArrayList: # 리스트 여러개 쓸 때에는 클래스가 더 낫다
    def __init__(self):
        self.items=[]

    def insert(self,position,data):
        self.items.insert(position,data)
    #삽입

    def delete(self,position):
        return self.items.pop(position)
    #삭제&삭제값 반환

    def getEntry(self,position):
        return self.items[position]
    #삭제 없이 보여주기

    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    # 한줄로 쓰면 def isEmpty():return len(items)==0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items=[]

    def find(self,item):
        return self.items.index(item)

    def replace(self,position,data):
        self.items[position]=data 

    def sort(self):
        self.items.sort()

    def merge(self,lst):
        self.items.extend(lst)

    def display(self,msg='ArrayList:'):
        print(msg,self.size(),self.items)


s=ArrayList()
s.insert(0,10)
s.insert(0,20)
s.insert(1,30)
s.insert(s.size(),40)
s.insert(2,50)
s.display("삽입5실행:")

s.sort()
s.display("정렬후:")

s.replace(2,90)
s.display("교체후:")

s.delete(2)
s.delete(s.size()-1)
s.delete(0)
s.display("삭제 후:")

lst=[1,2,3]
s.merge(lst)
s.display("병합 후:")

s.clear()
s.display("정리 후")