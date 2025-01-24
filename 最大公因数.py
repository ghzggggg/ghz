def com(a, b):
    n = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            n = i
    return n

while True:
    try:
        c, d = map(int, input().split())
    except:
        break
    print(comfac(a = c, b = d))