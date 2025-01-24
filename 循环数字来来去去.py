def round_round(b) :
    n = len(b)
    ss = str(int(b)*(n+1))
    ans = b +' is cyclic'
    for i in range(len(ss)) :
        if ss[i] != '9' :
            ans = b +' is not cyclic'
            break
    return ans
while True :
    try : a = input()
    except : break
    print(round_round(a))