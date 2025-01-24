import math
we = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
N = int(input())
for i in range(N) :
    s = input()
    ye = int(s[0:4])
    if float(s[4]+s[5]) < 3.0 :
        m = float(s[4]+s[5]) + 12
        ye -= 1
    else :
        m = float(s[4]+s[5])
    y = float(str(ye)[2]+str(ye)[3])
    c = float(str(ye)[0]+str(ye)[1])
    d = float(s[6]+s[7])
    w = int(y+ math.floor(y/4) + math.floor(c/4) -2*c+ math.floor(2.6*(m+1)) +d-1)%7
    print(we[w])