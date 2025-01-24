n,b = map(int,input().split())
v1 = list(map(int,input().split()))
v2 = list(map(int,input().split()))
bm = [0]*(b+1)
for i in range(n):
    for j in range(b,v2[i]-1,-1) :
        bm[j] = max(bm[j],bm[j-v2[i]]+v1[i])
print(bm[-1])