import heapq
q = int(input())
left,right,pop_left,pop_right = [],[],[],[]
heapq.heapify(left)
heapq.heapify(right)
heapq.heapify(pop_left)
heapq.heapify(pop_right)
for _ in range(q):
    s1,a,b = map(str,input().split())
    a1,b1 = -int(a),int(b)
    if s1 == '+':
        heapq.heappush(left,a1)
        heapq.heappush(right,b1)
    else:
        heapq.heappush(pop_left,a1)
        heapq.heappush(pop_right,b1)
        while pop_left and pop_left[0] == left[0]:
            heapq.heappop(pop_left)
            heapq.heappop(left)
        while pop_right and pop_right[0] == right[0]:
            heapq.heappop(pop_right)
            heapq.heappop(right)
    if left and right and left[0]+right[0]<0:print('YES')
    else:print('NO')