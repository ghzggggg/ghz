def cada(lq):
    here = ma = lq[0]
    for qx in lq[1:]:
        here = max(qx,qx+here)
        ma = max(ma,here)
    return ma

n = int(input())
num = []
while len(num) < n**2:
    num.extend(list(map(int,input().split())))
ans = -128
l = [num[i*n:(i+1)*n] for i in range(n)]

for i in range(n):
    line = [0]*n
    for j in range(i,n):
        for q in range(n):
            line[q] += l[q][j]
        ans = max(ans,cada(line))
print(ans)