import math
while True :
    l = str.split(input())
    c = max(0, int(l[1]) - 5 * int(l[3]))
    d = max(0, max(0,int(l[0]) - 11*int(l[4])) - max(0,-4*int(l[1]) + 20 * int(l[3])))
    if int(l[2])%4 != 0 :
        a = max(0, -d - int(l[2]) % 4 + 8)
        b = max(0, -c - 2*int(l[2]) % 4 + 7)
    else :
        a = b = 0
    ex = max(0,11*int(l[4])-int(l[0])) + max(0,20*int(l[3])-4*int(l[1]) - max(0,int(l[0])-11*int(l[4])))+a+4*b
    post = math.ceil((int(l[0])+int(l[1])*4+int(l[2])*9+int(l[3])*16+int(l[4])*25+ex)/36 + int(l[5]))
    if post == 0 :
        break
    else:
        print(post)