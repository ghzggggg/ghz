def lay(lm):
    ans = []
    if len(lm) == 1:
        return [lm]
    else:
        for i in range(len(lm)):
            lem = lay(lm[:i] + lm[i + 1:])
            for j in range(len(lem)):
                ans.append([lm[i]] + lem[j])
        return ans

n = int(input())
m,q,k = int(input()),1,1
while q <= m:
    k+=1
    q*=k
k+=1

l_in = list(map(int,input().split()))
ll = lay(l_in[n-k:])
l_out = l_in[:n-k]+ll[m]
print(*l_out)