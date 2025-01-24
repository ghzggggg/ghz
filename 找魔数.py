import math
n = int(input())
nums = list(map(int,input().split()))
q = 0
for a in nums:
    q = 0
    for c1 in range(1,32):
        if c1**2<a and math.sqrt(a-c1**2) == int(math.sqrt(a-c1**2)):
            q=1
            break
    if q==1:
        print(bin(a),oct(a),hex(a))