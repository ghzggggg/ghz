N = int(input())
for a in range(6,N+1) :
    dic = {}
    for b in range(2,a+1) :
        for c in range(2,b+1) :
            for d in range(2,c+1) :
                if a**3 == b**3 + c**3 + d**3 :
                    s ='Cube = '+str(a)+', Triple = ('+str(d)+','+str(c)+','+str(b)+')'
                    dic[d] = s
    l = sorted(dic.keys())
    for i in l :
        print(dic[i])