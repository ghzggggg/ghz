def int_map(a=50):
    array = [[1]*a] + [[0]*a for _ in range(a-1)]
    for i in range(1,a):
        for j in range(1,i):
            for k in range(min(i-j,j+1)):
                array[j][i] += array[k][i-j-1]
        array[i][i] = 1
    return array

l = int_map()

while True:
    try : n = int(input())
    except:break
    q = 0
    for ll in l:
        q += ll[n-1]
    print(q)