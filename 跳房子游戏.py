from collections import deque

def bfs(n,m):
    di = {}
    queue = deque([(n, 0, '')])

    while queue:
        x, d, s = queue.popleft()

        x1, d1, s1 = x * 3, d + 1, s + 'H'
        if di.get(x1, (float('inf'), '')) > (d1, s1):
            di[x1] = (d1, s1)
            queue.append((x1, d1, s1))
            if x1 == m:
                return d1,s1

        x2, d2, s2 = x // 2, d + 1, s + 'O'
        if di.get(x2, (float('inf'), '')) > (d2, s2):
            di[x2] = (d2, s2)
            queue.append((x2, d2, s2))
            if x2 == m:
                return d2,s2

while True:
    n1,m1 = map(int,input().split())
    if n1 == 0:break
    ans1,ans2 = bfs(n1,m1)
    print(ans1)
    print(ans2)