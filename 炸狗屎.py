def time(l,n):
    l.sort()
    su = sum(l)
    while su/2 < l[-1] :
        max_one = l.pop()
        su-= max_one
    return su/2

while True:
    try :n1 = int(input())
    except :break
