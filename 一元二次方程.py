import math
def one_sec(a,b,c) :
    if b**2 - 4*a*c > 0 :
       x1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
       x2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
       print("x1="+'%.5f'%x1+";"+"x2="+'%.5f'%x2)
    elif b**2 - 4*a*c == 0 :
       x1 = (-b)/(2*a)
       print("x1=x2="+'%.5f'%x1)
    elif b**2 - 4*a*c < 0 :
       x1 = (math.sqrt(-b*b+4*a*c))/(2*a)
       x2 = (-b)/(2*a)
       print("x1="+'%.5f'%x2+"+"+'%.5f'%x1+"i"
             +";"+"x2="+'%.5f'%x2+"-"+'%.5f'%x1+"i")
dic = {}
i = 1
m = int(input())
while i <= m:
    l = str.split(input())
    dic[i] = l
    i =i+1
for i in range(1,m+1):
    one_sec(a = float(dic[i][0]) ,b = float(dic[i][1]) ,c = float(dic[i][2]) )