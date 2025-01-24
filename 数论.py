N = int(input())
l = []
while N > 1 :
    i = 2
    while N%i != 0 :
        i = i+1
    N = N/i
    l.append(i)
sl = set(l)
if len(sl) < len(l) :
    print(0)
else :
    if len(l)%2 == 0 :
        print(1)
    else :
        print(-1)