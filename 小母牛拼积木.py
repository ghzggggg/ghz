n = int(input())
approach = []
s1 = set(input())
s2 = set(input())
s3 = set(input())
s4 = set(input())
s1.add('')
s2.add('')
s3.add('')
s4.add('')
for a in s1:
    for b in s2:
        for c in s3:
            for d in s4:
                l = [a,b,c,d]
                l.sort()
                approach.append(''.join(l))
for _ in range(n):
    goal = list(input())
    goal.sort()
    if ''.join(goal) in approach:
        print('YES')
    else:
        print('NO')