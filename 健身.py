t,n = map(int,input().split())
l = []
for _ in range(n):
    tt,w = map(int,input().split())
    l.append((tt,w))
lan = [0]+[-1]*t

for tt,w in l:
    for i in range(t,tt-1,-1):
        if lan[i-tt] != -1 :
            lan[i] = max(lan[i],lan[i-tt]+w)

print(lan[-1])