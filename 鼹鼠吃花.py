def ddp(n,k):
    dp = [1]*(n+1)
    if k <= n:
        for i in range(k,n+1):
            dp[i]=dp[i-1]+dp[i-k]
    return dp[n]

t,k1 = map(int,input().split())

for _ in range(t):
    a,b = map(int,input().split())
    ans = 0
    for n1 in range(a,b+1):
        ans += ddp(n1,k1)
    print(ans)