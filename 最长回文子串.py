s = input()
n = len(s)
l = list(s)
max_ever = -1
ans = ''
for i in range(n):
            left,right = i,i
            c = -1
            while 0<=left<n and 0<=right<n and l[left] == l[right]:
                c+=2
                left -=1
                right+=1
                print(c)
            if c>max_ever:
                ans = l[left+1:right]
                print(ans,left,right)
                max_ever = c
print(ans)