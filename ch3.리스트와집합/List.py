items=[]

def insert(position,data):
    items.insert(position,data)
#삽입

def delete(position):
    return items.pop(position)
#삭제&삭제값 반환

def getEntry(position):
    return items[position]
#삭제 없이 보여주기

def isEmpty():
    if len(items)==0:
        return True
    else:
        return False
# 한줄로 쓰면 def isEmpty():return len(items)==0

def size():
    return len(items)

def clear():
    global items
    #global items안쓰면 제대로 실행 안됨.items를 함수 내의 지역함수로 인식하기 때문
    items=[]

def find(item):
    return items.index(item)

def replace(position,data):
    items[position]=data 

def sort():
    items.sort()

def merge(lst):
    items.extend(lst)

def display(msg='ArrayList:'):
    print(msg,size(),items)


insert(0,10)
insert(0,20)
insert(1,30)
insert(size(),40)
insert(2,50)
display("삽입5실행:")

sort()
display("정렬후:")

replace(2,90)
display("교체후:")

delete(2)
delete(size()-1)
delete(0)
display("삭제 후:")

lst=[1,2,3]
merge(lst)
display("병합 후:")

clear()
display("정리 후")