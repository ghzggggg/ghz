n,m = map(int,input().split())
dp = [[0]*m for _ in range(n)]
l = []
for _ in range(n):
    x,y = map(int,input().split())
    l.append((x,y))

for j in range(m):
    x0,y0 = l[0]
    dp[0][j] = dp[0][max(j - 1, 0)]
    if 0<=j-y0<=x0<j : dp[0][j] = 1

for i in range(1,n):
    for j in range(m):
        xi,yi = l[i]
        if 0<=j-yi<=xi<j :
            dp[i][j] = max(dp[i-1][j-yi]+1,dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])