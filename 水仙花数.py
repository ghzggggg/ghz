l = str.split(input())
output = []
for j in range(int(l[0]),int(l[1])+1) :
    i = str(j)
    if int(i[0])**3 +int(i[1])**3 +int(i[2])**3 == int(i) :
        output.append(i)
if output :
    s = str(output[0])
    for i in output[1:] :
        s = s + " " +i
    print(s)
else :
    print('NO')