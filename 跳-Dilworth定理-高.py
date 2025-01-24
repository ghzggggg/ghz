from bisect import bisect_left

n = int(input())
l = list(map(int,input().split()))
long = []
l.reverse()

for i in l :
    x = bisect_left(long,i)
    if x < len(long):
        long[x] = i
    else: long.append(i)

print(len(long))