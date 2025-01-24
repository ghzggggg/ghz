while True:
    try: s1,s2 = input().split()
    except:break

    public = [[0]*(1+len(s2))for i in range(len(s1)+1)]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1]==s2[j-1]:
                public[i][j] = public[i-1][j-1]+1
            else:
                public[i][j] = max(public[i][j-1],public[i-1][j])

    print(public[-1][-1])