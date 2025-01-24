data = input()
d = str.split(data)
N = float(d[0])
M = float(d[1])
a = float(d[2])
if int(N/a) == N/a :
     n = int(N/a)
else:n = int(N/a)+1
if int(M/a) == M/a :
     m = int(M/a)
else:m = int(M/a)+1
print(m*n)