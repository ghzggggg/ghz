from functools import lru_cache

m,n = map(int,input().split())
a_map = [list(map(int,input().split())) for _ in range(m)]
dr = [(0,1),(1,0),(0,-1),(-1,0)]
ans = 0

@lru_cache(maxsize=None)
def dfs(x,y):

    ans1 = 0
    for dx,dy in dr:
        nx,ny = x+dx,y+dy
        if 0<=nx<m and 0<=ny<n and a_map[nx][ny]<a_map[x][y]:
            ans1 = max(ans1,dfs(nx,ny)+1)
    return ans1

for i in range(m):
    for j in range(n):
        ans = max(ans,dfs(i,j))
print(ans+1)