lights = [list(map(int,input().split())) for _ in range(5)]
ans1 = [[0]*6 for _ in range(5)]
ans2 = []
dr = [(0,1),(0,-1),(1,0),(-1,0),(0,0)]

def dp(light, ans, c=0):
    global ans2
    light_c = [light[i][:] for i in range(5)]
    ans_c = [ans[i][:] for i in range(5)]
    if c<6:
        dp(light_c,ans_c,c+1)
        ans_c[0][c] = 1
        for dx,dy in dr:
            nx,ny = dx,c+dy
            if 0<=nx<5 and 0<=ny<6 and light_c[nx][ny] == 1:
                light_c[nx][ny] = 0
            elif 0<=nx<5 and 0<=ny<6 and not light_c[nx][ny]:
                light_c[nx][ny] = 1
        dp(light_c,ans_c,c+1)
    else:
        for i in range(1,5):
            for j in range(6):
                if light_c[i-1][j] == 1:
                    ans_c[i][j] = 1
                    for dx, dy in dr:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < 5 and 0 <= ny < 6 and light_c[nx][ny] == 1:
                            light_c[nx][ny] = 0
                        elif 0 <= nx < 5 and 0 <= ny < 6 and not light_c[nx][ny]:
                            light_c[nx][ny] = 1
        if sum(light_c[4]) == 0:
            ans2 = ans_c
            return ans_c

dp(lights,ans1,0)
for l in ans2:
    print(*l)