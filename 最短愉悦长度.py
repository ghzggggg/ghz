n,m = map(int,input().split())
nums = list(map(int,input().split()))
di,num_m,num_0 = {}, [0]*10001,[]
for i in range(n):
    di[nums[i]] = di.get(nums[i],0)+1
    num_m[nums[i]] = 1
for i in range(1,10001):
    if num_m[i]:
        num_0.append(i)
ans,q = 1,m
for i in range(n):
    if num_m[nums[i]]==1:
        num_m[nums[i]]-=1
        q-=1
    if di[nums[i]]>0:
        di[nums[i]]-=1
    else:
        break
    if q==0:
        q = m
        for j in num_0:
            num_m[j] = 1
        ans+=1
print(ans)