han = [0,1]
for n in range(2,13):
    an = 2**n-1
    for k in range(1,n):
        an = min(an,2*han[n-k]+2**k-1)
    han.append(an)
for i in range(1,13) :
    print(han[i])