n,m = map(int,input().split())
l = str.split(input())
l.sort(key=int)
dell = [int(l[i+1])- int(l[i]) for i in range(len(l)-1)]
dell.sort(reverse=True)
output = int(l[-1]) - int(l[0])
for i in range(m-1) :
    output -= dell[i]
print(output)