n = int(input())
for _ in range(n):
    q = int(input())
    c = 1
    while c <= q:
        c*=2
    print(int((q+1)*q/2-2*c+2))