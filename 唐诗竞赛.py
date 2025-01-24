n = int(input())
a = 1
q = 0
while a <= n :
    l = input()
    m = str.split(l)
    if int(m[0])+int(m[1])+int(m[2]) < 2 :
        q = q
    else:
        q = q+1
    a = a+1
print(q)