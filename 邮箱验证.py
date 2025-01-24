def e_mail(s) :
    l = []
    for i in s :
        l = l.append(i)
    if "@" in l :
        if "@" in l.remove("@") :
            return "NO"
        else :
            if "." in l :
                if l[0] != "@"and l[-1] != "@"and l[0] != "."and l[-1] != "." :
                    if l[l.index("@")+1] != "." :
                        for m in range(l.index('@') + 1, len(l)) :
                            if l[m] != "." :
                                return "NO"
                            else :
                                return "YES"
                    else :
                        return "NO"
                else :
                    return "NO"
            else :
                return "NO"
    else:return "NO"
while True :
    # noinspection PyBroadException
    try :
        s1 = str(input())
    except :
        break
    print(e_mail(s1))