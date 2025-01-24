N = int(input())
l = str.split(input())
l.append('1')
i = m = n = 0
while i < N :
    if 0 < int(l[i]) :
        m = m + int(l[i])
    if int(l[i]) < 0 :
        m = m - 1
        if int(l[i+1]) >0 :
           n = n + min(0,m)
           if m < 0 :
               m = 0
    i = i + 1
print(abs(n))