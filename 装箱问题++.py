import math
while True :
    r = [0,5,3,1]
    l = str.split(input())
    t = max(0,int(l[1]) - 5*int(l[3]) - r[int(l[2])%4])
    a = math.ceil(int(l[2])/4) + int(l[3]) + int(l[4]) +int(l[5]) + math.ceil(t/9)
    b = math.ceil((int(l[0])+int(l[1])*4+int(l[2])*9+int(l[3])*16+int(l[4])*25)/36 + int(l[5]))
    post = max(a,b)
    if post == 0 :
        break
    else:
        print(post)