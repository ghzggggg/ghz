height = list(map(int,input().split()))
i, j = 0, len(height)-1
max_even = min(height[i], height[j]) * (j - i)

while j > i:
    left, right = height[i], height[j]
    if right >= left:
        i+=1
        while height[i] <= left and j > i:
            i += 1
    else:
        j-=1
        while height[j] <= right and j > i:
            j -= 1
    max_even = max(max_even, min(height[i], height[j]) * (j - i))

print(max_even)