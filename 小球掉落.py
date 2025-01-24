h,l,n = map(int,input().split())
balls = list(map(int,input().split()))
balls.sort()
t_max = l/balls[n//2]
h_min = h-5*(t_max**2)
print('%.2f'%h_min)