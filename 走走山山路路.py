import heapq

m,n,p = map(int,input().split())
dr = [(0,1),(1,0),(0,-1),(-1,0)]
a_map = [input().split() for _ in range(m)]

for _ in range(p):

    x0,y0,x1,y1 = map(int,input().split())

    if a_map[x0][y0] == '#' or a_map[x1][y1] == '#':
        print('NO')
    else:
        heap = [(0, x0, y0)]
        heapq.heapify(heap)
        q_map = [[float('inf')] * n for _ in range(m)]
        q_map[x0][y0] = 0

        while heap:
            d, x, y = heapq.heappop(heap)
            for dx, dy in dr:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and a_map[nx][ny] != '#':
                    d1 = d + abs(int(a_map[nx][ny]) - int(a_map[x][y]))
                    if d1 < q_map[nx][ny] and d1 < q_map[x1][y1]:
                        q_map[nx][ny] = d1
                        heapq.heappush(heap, (d1, nx, ny))

        if q_map[x1][y1] < float('inf'):
            print(q_map[x1][y1])
        else:
            print('NO')