ML = input()
mist = str.split(ML)
L = mist[0]
M = mist[1]
nlist = []
m = 1
n = 0
while 1 <= m <= int(M) :
    ab = input()
    abl = str.split(ab)
    am = int(abl[0])
    bm = int(abl[1])
    list1 = list(range(am,bm+1))
    nlist.extend(list1)
    m = m+1
llist = list(set(nlist))
l = len(llist)-1
print(int(L)-int(l))