n = int(input())
radius = list(map(int,input().split()))
a_map = [0]*n
for i in range(n):
    a_map[max(0,i-radius[i])] = max(a_map[max(0,i-radius[i])],i+radius[i])
i = j = k = ans = 0
while j<n-1:
    while i <= j :
        k = max(k,a_map[i])
        i+=1
    j = max(k,i)
    ans+=1
print(ans)