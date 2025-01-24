def max_true(a,b) :
    n = int(min([int(a), int(b)]))
    m = int(max([int(a), int(b)]))
    while m % n != 0:
          n = min([min([m,n]),m-min([m,n])])
          m = max([min([m,n]),m-min([m,n])])
    return min([m,n])
while True:
    # noinspection PyBroadException
    try:
        c, d = map(int, input().split())
    except:
        break
    print(max_true( a = c, b = d))