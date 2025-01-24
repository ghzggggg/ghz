from collections import deque

n = int(input())
queue = deque([deque(list(map(int,input().split()))) for _ in range(n)])
ans = 0
for i in range(n//2+n%2):
    q = 0
    l1 = queue.popleft()
    if queue:
        l2 = queue.pop()
        q+=sum(l2)
    if queue:
        for l in queue:
            q+=l.popleft()
            if l:q+=l.pop()
    q+=sum(l1)
    ans = max(ans,q)
print(ans)