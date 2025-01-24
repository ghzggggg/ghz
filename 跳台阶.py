n = int(input())
dp = [1]*n
for i in range(n):
    for j in range(i):
        dp[i]+=dp[j]
print(dp[-1])