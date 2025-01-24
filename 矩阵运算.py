def matr_born(l) :
    m = []
    for b in range(int(l[0])):
        la = str.split(input())
        m.append(la)
    return m
while True :
    A = matr_born(str.split(input()))
    B = matr_born(str.split(input()))
    C = matr_born(str.split(input()))
    if len(A[0]) != len(B) or len(A) != len(C) or len(B[0]) != len(C[0]):
        print("Error!")
        break
    D = []
    for i in range(len(A)) :
        li = []
        for j in range(len(B[0])) :
            a = 0
            for k in range(len(B)) :
                a += int(A[i][k])*int(B[k][j])
            a += int(C[i][j])
            li.append(a)
        D.append(li)
    for ll in D :
        s = ' '.join(str(i) for i in ll)
        print(s)
    break