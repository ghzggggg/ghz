for _ in range(int(input())):
    l1 = input().split()
    l2 = input().split()
    l3 = input().split()
    l = [chr(i) for i in range(65, 77)]
    dic = {}
    dic[0], dic[1], dic[-1] = 'even', 'up', 'down'
    for i in l:
        for j in l:
            dic[j] = 0
        for q in (-1, 1):
            dic[i] = q
            l10 = dic[l1[0][0]] + dic[l1[0][1]] + dic[l1[0][2]] + dic[l1[0][3]]
            l20 = dic[l2[0][0]] + dic[l2[0][1]] + dic[l2[0][2]] + dic[l2[0][3]]
            l30 = dic[l3[0][0]] + dic[l3[0][1]] + dic[l3[0][2]] + dic[l3[0][3]]
            l11 = dic[l1[1][0]] + dic[l1[1][1]] + dic[l1[1][2]] + dic[l1[1][3]]
            l21 = dic[l2[1][0]] + dic[l2[1][1]] + dic[l2[1][2]] + dic[l2[1][3]]
            l31 = dic[l3[1][0]] + dic[l3[1][1]] + dic[l3[1][2]] + dic[l3[1][3]]
            if dic[l10 - l11] == l1[2] and dic[l20 - l21] == l2[2] and dic[l30 - l31] == l3[2]:
                if q == -1:
                    print(i + ' is the counterfeit coin and it is light.')
                else:
                    print(i + ' is the counterfeit coin and it is heavy.')
                break