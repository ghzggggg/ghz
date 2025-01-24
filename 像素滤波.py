m,n = map(int,input().split())
icon = [[0]*(n+2)]
for _ in range(m):
    icon.append([0]+list(map(int,input().split()))+[0])
icon.append([0]*(n+2))
ans = [[0]*n for _ in range(m)]
dr = [(0,0),(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(-1,-1),(1,-1)]
for x in range(1,m+1):
    for y in range(1,n+1):
        cq,su = 0,0
        for dx,dy in dr:
            if icon[x+dx][y+dy]>0:
                su+=1
            cq+=icon[x+dx][y+dy]
        ans[x-1][y-1] = int(cq/su)//1
for l in ans:
    print(*l)