p = int(input())
l = str.split(input())
l.sort(key = int)
i = buy = 0
j = len(l)-1
while i <= j :
    if p >= int(l[i]) :
        p -= int(l[i])
        buy += 1
        i += 1
    else :
        if i+1 < j and buy+j+1-len(l) >0:
            p += int(l[j])
            j -= 1
        else :
            break
print(max( buy+j+1-len(l) , 0 ))