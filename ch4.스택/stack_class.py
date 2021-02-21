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


s=stack()
for i in range(1,6):
    s.push(i)

print('push 5회:',s.st)
print('pop()->',s.pop())
print('pop()->',s.pop())
print(' pop 2회 후 :',s.st)
