N = int(input())
for i in range(6, N + 1):
    if N % i == 0:
        print(N / i)