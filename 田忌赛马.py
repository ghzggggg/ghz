while True :
    n = int(input())
    if n == 0 :
        break
    Tian = list(map(int,input().split()))
    King = list(map(int,input().split()))
    Tian.sort ()
    King.sort()
    a,l1,r1,l2,r2 = 0,0,n-1,0,n-1
    while l1 <= r1:
        if Tian[l1] > King[l2]:
            a += 1
            l1 += 1
            l2 += 1
        elif Tian[r1] > King[r2]:
            a += 1
            r1 -= 1
            r2 -= 1
        else:
            if Tian[l1] < King[r2]:
                a -= 1
            l1 += 1
            r2 -= 1
    print(a * 200)