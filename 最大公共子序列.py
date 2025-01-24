from bisect import bisect_left

def max_spring(s1,s2):
    l1,l2 = list(s1), list(s2)
    lq = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                lq.append(j)
    max_up = []
    if lq :
        for i in range(len(lq)):
            pos = bisect_left(max_up,lq[i])
            if pos < len(max_up):
                max_up[pos] = lq[i]
            else: max_up.append(lq[i])
        print(max_up)
        return len(max_up)
    else: return 0

while True :
    try: s11,s22 = map(str,input().split())
    except :break
    print(max_spring(s11,s22))