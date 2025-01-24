n = int(input())
goods = list(map(int,input().split()))
love = {}
ever,ans = 0,0
for i in range(n):
    ever+=goods[i]-520
    if ever == 0:
        ans = 520*(i+1)
    else:
        if love.get(ever,-1)>=0:
            ans = max(ans, 520 * (i - love[ever]))
        else:
            love[ever] = i
print(ans)