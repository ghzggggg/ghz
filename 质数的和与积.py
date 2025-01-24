def zhi_judge(n) :
    ans = 1
    if n ==2 :
        return ans
    for m in range(2,int(n/2)+2) :
        if n%m == 0 :
            ans = 0
            break
        else :
            pass
    return ans
s = int(input())
if s%2 == 0 :
    for i in range(0,int(s/2)) :
        if zhi_judge(s/2-i)==1 and zhi_judge(s/2+i)==1 :
            print(int((s**2)/4-(i**2)))
            break
else :
    if zhi_judge(s-2) == 1 :
        print((s-2)*2)