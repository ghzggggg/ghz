for i in range(int(input())):
    n = int(input())
    l = []
    for j in range(n) :
        l.append(list(map(int,input().split())))
    l.sort(key=lambda x:x[0])
    k = output = 0
    while k < len(l) :
        output += 1
        if k == len(l)-1:
            break
        spa = list(set(list(range(l[k][0],l[k][1]+1))) & set(list(range(l[k+1][0],l[k+1][1]+1))))
        while spa :
            k += 1
            if k == len(l)-1:
                break
            spa = list(set(spa) & set(list(range(l[k + 1][0], l[k + 1][1] + 1))))
        k += 1
    print(output)