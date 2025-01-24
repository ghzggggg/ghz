l = list(map(int,input().split()))
i,j,left,right = 0,len(l)-1,l[0],l[-1]
ans = 0
while i<j:
    ans = max(ans,right-left)
    if l[i+1]<l[i]:
        left = min(l[i+1],left)
    else:
        ans = max(ans,l[i+1]-left)
    i+=1
    if l[j-1]>l[i]:
        right = max(l[j-1],right)
    else:
        ans = max(ans,right-l[j-1])
    j-=1
print(ans)