import queue
#import queue할때에는 같은 경로에 queue.py 있으면 에러남!!


Q=queue.Queue(maxsize=20)
#큐 객체 생성(최대크기 20)
#maxsize=0이면 큐의 크기 무한대

#import queue에서는 함수 이름이 다르다!
#enqueue()->put()
#dequeue()->get()

for i in range(1,10):
    Q.put(i)
print("큐 :",end='')

for _ in range(1,10):
    print(Q.get(),end=' ')
print()

#put()과 get()은 언더플로, 오버플로가 발생해도 에러 반환X, 무한루프 가능성 -> empty, full 검사 필수!


S=queue.LifoQueue(maxsize=20)
#스택
#후입선출Last in First out

for i in range(1,10):
    S.put(i)
print("스택 :",end='')

for _ in range(1,10):
    print(S.get(),end=' ')
print()
#똑같이 


#결과
#큐 : 1 2 3 4 5 6 7 8 9
#스택 : 9 8 7 6 5 4 3 2 1


