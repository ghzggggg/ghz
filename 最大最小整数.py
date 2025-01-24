import math
input()
lt = input().split()
max_len = len(max(lt, key = lambda x:len(x)))
lt.sort(key = lambda x: x * math.ceil(2*max_len/len(x)))
lt1 = reversed(lt)
print(''.join(lt1),''.join(lt))