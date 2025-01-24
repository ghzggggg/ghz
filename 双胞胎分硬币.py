n = int(input())
l = list(map(int,input().split()))
l.sort(reverse=True)
N = sum(l)
maxi = 0
j = 0
for i in range(n):
    if float(maxi) >float(N/2) :
        break
    maxi += l[i]
    j += 1
print(j)