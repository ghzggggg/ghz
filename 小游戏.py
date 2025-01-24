from collections import deque

def segment(x,y,h1,w1,ll,x22,y22):
    ans = float('inf')
    dr = [(1,0),(0,1),(-1,0),(0,-1)]

    queue = deque([(x,y,-1,0)])
    in_queue = set()

    while queue:
        x0,y0,dir_ever,seg = queue.popleft()
        if (x0, y0) == (x22,y22):
            ans = min(ans,seg)
            break
        for dire,(dx,dy) in enumerate(dr):
            nx,ny = x0+dx,y0+dy
            if 0<=nx<h1+2 and 0<=ny<w1+2 and ((nx,ny,dire) not in in_queue):
                new_dire = dire
                new_seg = seg+1 if dir_ever!=dire else seg
                if (nx,ny) == (x22,y22) :
                    ans = min(ans,new_seg)
                if ll[nx][ny] != 'X':
                    in_queue.add((nx,ny,dire))
                    queue.append((nx,ny,new_dire,new_seg))
    if ans == float('inf') :
        ans =-1
    return ans


i = 0
while True :
    i+=1
    w,h = map(int,input().split())
    if w ==0 : break
    print('Board #'+str(i)+':')
    board = [[' ']*(w+2)]
    for _ in range(h):
        lh = [' ']+list(input())+[' ']
        board.append(lh)
    board.append(['']*(w+2))
    c = 0
    while True:
        c+=1
        y1,x1,y2,x2 = map(int,input().split())
        a = segment(x1,y1,h,w,board,x2,y2)
        if x1==0 : break
        if a !=-1:
            print('Pair '+str(c)+': '+str(a)+' segments.')
        else:
            print('Pair ' + str(c) + ': impossible.')
    print()