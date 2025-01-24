from collections import deque
n = int(input())
queue2 = deque()
for _ in range(n):
    queue1 = deque(map(int,input().split()))
    queue2.append(queue1)
ans = 0
while queue2:
    q = 0
    left = queue2.popleft()
    right = []
    if queue2:
       right = queue2.pop()
    for queue in queue2:
        a,b=queue.popleft(),queue.pop()
        q+=a+b
    q+=sum(left)+sum(right)
    ans = max(ans,q)
print(ans)