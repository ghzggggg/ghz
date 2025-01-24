d = {}
for i in range(1,21):
    d[i] = []
m = int(input())
n = int(input())
sl = input().split()
for s in sl:
    d[len(s)].append(s)
for i in range(1,21):
    d[i].sort(reverse=True)
dp = [['',[]] for _ in range(m+1)]

for i in range(1,m+1):
    for j in range(1,21):
        if i-j>0 and dp[i-j][0] and dp[i-j][1] or i==j :
            s1,l1 = dp[i-j][0],dp[i-j][1]
            l = l1[:]
            if d[j]:
                for s in d[j]:
                    if s not in l:
                        l.append(s)
                        s1+=s
                        break
            if s1>dp

for i in range(m,-1,-1):
    if dp[i][0]:
        print(int(dp[i][0]))
        break