import math
N = int(input())
while N != 0 :
    l = str.split(input())
    print( math.ceil(float(l[0])/float(l[1]))*int(l[1]) - int(l[0]))
    N = N-1