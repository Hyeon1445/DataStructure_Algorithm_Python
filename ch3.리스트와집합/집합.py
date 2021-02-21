class Set():
    def __init__(self):
        self.items=[]
    
    def size(self):
        return len(self.items)
    
    def display(self,msg):
        print(msg,self.items)
    
    def contains(self,data):
        return data in self.items
        #data의 유무 검사

    def insert(self,data):
        if data not in self.items:
            self.items.append(data)
    
    def delete(self,data):
        if data in self.items:
            self.items.remove(data)

    def union(self,setB):#합집합
        setC=Set()
        setC.items=list(self.items)
        for elem in setB.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC
    
    def intersect(self,setB):#교집합
        setC=Set()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC

    def difference(self,setB):
        setC=Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC


setA=Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('SetA:')

setB=Set()
setB.insert('빗')
setB.insert('책')
setB.insert('공')
setB.insert('지갑')
setB.display('SetB:')

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('SetA:')
setB.display('SetB:')
setA.union(setB).display("A U B:")
setA.intersect(setB).display('A ^ B:')
setA.difference(setB).display('A - B')
