st=[]

def isEmpty():
    return len(st)==0

def push(data):
    st.append(data)
#리스트의 맨 뒤에 data추가
#O(1)

def pop():
    if not isEmpty():
        return st.pop(-1)

def peek():
    if not isEmpty():
        return st[-1]

def size():
    return len(st)

def clear():
    global st
    st=[]


for i in range(1,6):
    push(i)

print('push 5회:',st)
print('pop()->',pop())
print('pop()->',pop())
print(' pop 2회 후 :',st)
