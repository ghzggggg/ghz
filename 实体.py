def count_numbers(s) :
    l = str.split(s)
    ml = []
    for i in range(len(l)) :
        if "#" in l[i] :
           ml.append(i)
    n = 0
    for j in range(len(ml)) :
        if ml[j] - ml[j-1] != 1 :
            n = n+1
        else :
            pass
    return n
N = int(input())
num = 0
while N != 0 :
    num = num + count_numbers(input())
    N = N - 1
print(num)