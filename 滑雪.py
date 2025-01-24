m,n = map(int,input().split())
a_map = [list(map(int,input().split())) for _ in range(m)]
q_map = [[(0,0)]*n for _ in range(m)]
dr = [(0,1),(1,0),(0,-1),(-1,0)]
ans = 0

for i in range(m):
    for j in range(n):

        arrive,set_off = q_map[i][j]
        if arrive==0 and set_off==0:
            up,down = 0,0
            queue2 = [(i,j,0)]

            while queue2:
                x, y, s = queue2.pop()
                up = max(up, s)
                for dx, dy in dr:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and a_map[nx][ny] > a_map[x][y]:
                        a, b = q_map[nx][ny]
                        q = s + 1
                        if a :q_map[nx][ny] = a+1,b
                        else:

            queue1 = [(i,j,up+1)]

            while queue1:
                x, y, s = queue1.pop()
                down = max(down, s)
                for dx, dy in dr:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and a_map[nx][ny] < a_map[x][y] :
                        a, b = q_map[nx][ny]
                        q = s + 1
                        if a < q:
                            queue1.append((nx, ny, q))
                            q_map[nx][ny] = a,q

            ans = max(ans,up+down+1)
print(ans)