n,t = map(int,input().split())
q = list(map(int,input().split()))
su = sum(q)
ans = 0
if su >=t :
    q.sort()
    dp = [[1] * n]
    for i in range(su):
        dp.append([0] * n)
    for i in range(n):
        dp[q[0]][i] = 1
    for i in range(1,su+1):
        for j in range(1,n):
            if i-q[j] >=0 and dp[i-q[j]][j-1] :
                for k in range(j,n):
                    dp[i][k] = 1
                if i >=t: ans = i
        if ans!=0: break
print(ans)