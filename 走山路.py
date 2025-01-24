from collections import deque

m,n,p = map(int,input().split())
a_map = [input().split() for _ in range(m)]

def bfs(x0,y0,x1,y1):

    global a_map
    q_map = [[float('inf')]*n for _ in range(m)]
    q_map[x0][y0] = 0
    dr = [(0,1),(0,-1),(1,0),(-1,0)]
    queue = deque([(x0,y0,0)])

    while queue:
        x,y,hp = queue.popleft()
        if hp >=q_map[x1][y1]:pass
        else:
            for dx, dy in dr:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and a_map[nx][ny] != '#':
                    q1 = hp + abs(int(a_map[x][y]) - int(a_map[nx][ny]))
                    if q1 < q_map[nx][ny]:
                        queue.append((nx, ny, q1))
                        q_map[nx][ny] = q1

    return q_map[x1][y1]

for _ in range(p):
    a,b,c,d = map(int,input().split())
    if a_map[a][b]=='#' or a_map[c][d] =='#':
        print('NO')
    else:
        ans = bfs(a, b, c, d)
        if ans == float('inf'):
            print('NO')
        else:
            print(ans)