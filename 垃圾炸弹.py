d = int(input())
l = [list(map(int,input().split())) for _ in range(int(input()))]
dic = {}
for n in range(len(l)) :
    for i in range(max(0,l[n][0]-d),min(l[n][0]+d+1,1025)):
        for j in range(max(0,l[n][1]-d),min(l[n][1]+d+1,1025)):
            dic[(i,j)] = dic.setdefault((i,j),0) + l[n][2]
ll = list(dic.values())
a = max(ll)
print(str(ll.count(a))+' '+str(a))