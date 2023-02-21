# 과거 풀이
# 80ms
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
d = deque()
for _ in range(N):
    order = input().rstrip().split()
    o = order[0]
    if o == 'push_front': d.appendleft(order[1])
    elif o == 'push_back': d.append(order[1])
    elif o == 'pop_front': print(d.popleft()) if d else print(-1)
    elif o == 'pop_back': print(d.pop()) if d else print(-1)      
    elif o == 'size': print(len(d))
    elif o == 'empty': print(1) if len(d) == 0 else print(0)       
    elif o == 'front': print(d[0]) if d else print(-1)
    elif o == 'back': print(d[-1]) if d else print(-1)

"""
appendleft: 왼쪽에 값 넣음
"""

# 현재 풀이
# 48ms
import sys
input = sys.stdin.readline
N = int(input())
d = []
for _ in range(N):
    order = input().rstrip().split()
    o = order[0]
    if o == 'push_front': d.insert(0, order[1])
    elif o == 'push_back': d.append(order[1])
    elif o == 'pop_front': print(d.pop(0) if d else -1)
    elif o == 'pop_back': print(d.pop() if d else -1)    
    elif o == 'size': print(len(d))
    elif o == 'empty': print(0 if d else 1)       
    elif o == 'front': print(d[0] if d else -1)
    elif o == 'back': print(d[-1] if d else -1)

"""
.insert(i, x) : 위치 i에 값 x 삽입
"""