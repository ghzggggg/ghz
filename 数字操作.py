from collections import deque

n = int(input())
l = [0]*(n+1)
queue = deque([(1,0)])
ans = 0

while queue:
    x,s = queue.popleft()
    if x*2 < n and not l[x*2]:
        queue.append((x*2,s+1))
        l[x*2] = 1
    elif x*2 ==n:
         ans = s+1
         break
    if x+1 < n and not l[x+1]:
        queue.append((x+1,s+1))
        l[x+1] = 1
    elif x+1 ==n:
         ans = s+1
         break

print(ans)