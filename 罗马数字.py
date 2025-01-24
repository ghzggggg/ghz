s = input()
d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
ln3 = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
ln2 = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
ln1 = ['','I','II','III','IV','V','VI','VII','VIII','IX']

if s[0] in ['I', 'C', 'L', 'X', 'D', 'M', 'V'] :
    ans = 0
    for i in s :
       ans += d[i]
    if len(s) == 1 :
        print(ans)
    else :
        for i in range(len(s)-1):
            if s[i] == 'C' and s[i + 1] == 'M':
                ans -= 200
            if s[i] == 'C' and s[i + 1] == 'D':
                ans -= 200
            if s[i] == 'X' and s[i + 1] == 'C':
                ans -= 20
            if s[i] == 'X' and s[i + 1] == 'L':
                ans -= 20
            if s[i] == 'I' and s[i + 1] == 'X':
                ans -= 2
            if s[i] == 'I' and s[i + 1] == 'V':
                ans -= 2
        print(ans)
else:
    output = ''
    if len(s) == 4:
        for i in range(int(s[0])):
            output += 'M'
        output += ln3[int(s[1])]+ln2[int(s[2])]+ln1[int(s[3])]
    if len(s) == 3:
        output += ln3[int(s[0])] + ln2[int(s[1])] + ln1[int(s[2])]
    if len(s) == 2:
        output += ln2[int(s[0])] + ln1[int(s[1])]
    if len(s) == 1:
        output += ln1[int(s[0])]
    print(output)