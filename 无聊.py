n = int(input())
l0 = list(map(int,input().split()))
l0.sort()
l = []
q = 0
for i in range(n):
    q += l0[i]
    if i < n-1 and l0[i+1]!=l0[i] or i==n-1 :
        l.append((l0[i],q))
        q = 0
la = [l[0][1]]+[0]*(len(l)-1)
for i in range(1,len(l)):
    if l[i][0]-l[i-1][0] != 1:
        la[i] = la[i-1]+l[i][1]
    else:
        la[i] = max(la[i-1],la[i-2]+l[i][1])
print(la[-1])