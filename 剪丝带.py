n,a,b,c = map(int,input().split())
l = [0]*(n+1)
for i in (a,b,c) :
    if i<=n :
        l[i] = 1
for i in range(1,n+1):
    for j in (a,b,c):
        if i-j >= 0 and l[i-j] != 0 :
            l[i] = max(l[i-j]+1,l[i])
print(l[-1])