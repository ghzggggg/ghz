from collections import deque

s = input()
n,pos = len(s),1
queue,ans = deque([]),[]
while pos<=n:
    queue.append(s[pos-1])
    pos*=2
while queue:

    left = queue.popleft()
    ans.append(left)

    if queue:
        right = queue.pop()
        ans.append(right)

print(''.join(ans))