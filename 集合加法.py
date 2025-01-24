for i in range(int(input())) :
    s = int(input())
    a = int(input())
    l1 = str.split(input())
    b = int(input())
    l2 = str.split(input())
    n = 0
    for j in l1 :
        n += l2.count(str(s - int(j)))
    print(n)