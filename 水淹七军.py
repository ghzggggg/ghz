def judge(a_map,x1,y1,tip):
    height = a_map[tip[0]][tip[1]]
    an = 0
    dr = [(0,1),(1,0),(-1,0),(0,-1)]
    stack = [tip]

    while stack:
        x,y = stack.pop()
        for dx,dy in dr :
            nx=x+dx
            ny=y+dy
            if 0<nx<m+1 and 0<ny<n+1 and a_map[nx][ny] <= height:
                if (nx,ny) == (x1,y1) and a_map[x1][y1] < height:
                    an =1
                stack.append((nx,ny))
                a_map[nx][ny] = height+1
    return an

k = int(input())
for _ in range(k):
    m,n = map(int,input().split())
    ll = [[0]*(n+2)]
    for _ in range(m):
        li = [0]+list(map(int,input().split()))+[0]
        ll.append(li)
    ll.append([0]*(n+2))
    x0,y0 = map(int,input().split())
    p = int(input())
    ans = 'No'
    for _ in range(p):
        xi,yi = map(int,input().split())
        ti = (xi,yi)
        lc = []
        for l in ll:
            lc.append(l[:])
        if judge(lc,x0,y0,ti)==1:
            ans = 'Yes'
            break
    print(ans)