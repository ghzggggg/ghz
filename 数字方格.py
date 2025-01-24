n = int(input())
m1 = 3*n - (2*n)%3
if m1%5 == 1:
    print(m1 -6)
else :
    print(m1 -m1%5)