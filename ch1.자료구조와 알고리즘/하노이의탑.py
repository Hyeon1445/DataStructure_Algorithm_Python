def hanoi_tower(n,fr,by,to):
    if(n==1):
        print("원판 1: %s -> %s"%(fr,to))
    else:
        hanoi_tower(n-1,fr,to,by)
        print("원판 %d: %s -> %s"%(n,fr,to))
        hanoi_tower(n-1,by,fr,to)

hanoi_tower(4,'A','B','C')

#시간복잡도
#T(n)=2T(n-1)+1
#T(n)=2(2T(n-2)+1)+1
#...
#O(2^n)