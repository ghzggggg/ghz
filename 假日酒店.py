N = int(input())
l1 = []
l2 = []
l3 = []
for i in range(N):
    l = str.split(input())
    l1.append(int(l[0]))
    l2.append(int(l[1]))
a = 10001
b = 10001
ans = 2
for i in range(N):
    if l1[i] <= a :
        a = l1[i]
for i in range(N):
    if l2[i] <= b:
        b = l2[i]
for i in range(N):
    if l1[i] == a :
        l3.append(l2[i])
if b in l3 :
    ans = 1
print(ans)