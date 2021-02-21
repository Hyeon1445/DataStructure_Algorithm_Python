# 큐

파이썬에서는 front와 rear를 따로 지정해줄 필요X

front=0 rear=len(list)-1

***

# 원형 큐

* 맨 처음에는 front=rear=0
* 공백상태 front=rear
* 포화상태 : front==(rear+1)%MAX_QSIZE (front가 rear보다 한칸 앞일 때)

