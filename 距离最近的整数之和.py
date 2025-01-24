t = int(input())
l = list(map(int,input().split()))
l.sort()
g1,g2,i,j= t,-t,0,len(l)-1
while True :
    if l[i]+l[j] < t:
        g1 = min(g1,t-l[i]-l[j])
        i+=1
        if i == j :
            break
    elif l[i]+l[j]>t:
        g2 = max(g2,t-l[i]-l[j])
        j-=1
        if i == j :
            break
    else :
        g1,g2 = 0,0
        break
if g1+g2 > 0 :
    print(t-g2)
else :
    print(t-g1)