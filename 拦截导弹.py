n = int(input())
ql = list(map(int,input().split()))
l = [1]*n
for i in range(n):
    for j in range(i) :
        if ql[i] <= ql[j] :
            l[i] = max(l[i],l[j]+1)
print(max(l))