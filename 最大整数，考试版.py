m = int(input())
n = int(input())
nums = input().split()
i = 1
while i < n:
    if nums[i-1]+nums[i] < nums[i]+nums[i-1]:
        nums[i],nums[i-1] =nums[i-1],nums[i]
        i = 1
    else:
        i+=1
length = []
for i in nums:
    length.append(len(i))
dp = [[0]*n for _ in range(m+1)]

for j in range(n):
    for i in range(m,-1,-1):
        if i-length[j]>=0:
            dp[i][j] = max(int(str(dp[i-length[j]][j-1])+nums[j]),dp[i][j-1])
        else:
            dp[i][j] = dp[i][max(j-1,0)]
print(dp[-1][-1])