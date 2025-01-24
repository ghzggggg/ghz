while True :
    r,n = map(int,input().split())
    if r == -1 :
        break
    l = list(map(int,input().split()))
    l.sort()
    cov = i = j = out = 0
    while j < n :
        out += 1
        if j == n-1:
            break
        while l[i+1] <= l[j]+r :
            if i == n-2 :
                i +=1
                break
            i += 1
        if i == n-1:
            break
        j = i
        while l[j+1] <= l[i]+r :
            if j == n-2 :
                j +=1
                break
            j += 1
        j += 1
        i = j
    print(out)