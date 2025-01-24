m,n = map(int,input().split())
a_map = [list(map(int,input().split())) for _ in range(m)]
dp = [[0]*n for _ in range(m)]
dr = [(0,1),(1,0),(0,-1),(-1,0)]
ans = 0

def dfs(x,y):

    if dp[x][y]:
        return dp[x][y]

    else:
        for dx,dy in dr:
            nx,ny = x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and a_map[nx][ny]<a_map[x][y]:
                dp[x][y] = max(dp[x][y],dfs(nx,ny)+1)
        return dp[x][y]

for i in range(m):
    for j in range(n):
        ans = max(ans,dfs(i,j))
print(ans+1)