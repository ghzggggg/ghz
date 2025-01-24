n = int(input())
ll = []
for i in range(n) :
    ll.append([0]+list(map(int,input().split()))+[0])
l = [0]*(n+1)
for i in range(n):
    li = list(m for m in l)
    for j in range(1,i+2) :
        l[j] = max(li[j],li[j-1])+ll[i][j]
print(max(l))