n = int(input())
m,ans = 0,0
while 2*m <= n:
    q = 1
    for i in range(1,m+1):
        q *=(n-2*m+i)/i
    ans+=q
    m+=1
print(int(ans))