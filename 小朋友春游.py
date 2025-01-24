n = int(input())
l = str.split(input())
nl = list(i for i in range(1,n+1))
ol = []
for i in l :
    if int(i) in nl :
        nl.remove(int(i))
    else :
        ol.append(int(i))
ol.sort()
print(*nl)
print(*ol)