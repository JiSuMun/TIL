# 과거 풀이
# 36ms
import sys
input = sys.stdin.readline
A, B = input().split()
A = list(map(int, A))
B = list(map(int, B))
print(sum(A)*sum(B))

# 현재 풀이
# 40ms
import sys
input = sys.stdin.readline
A, B = input().split()
print(sum(map(int, A))*sum(map(int, B)))
# 44ms
A, B = map(map, [int]*2 ,input().split())
print(sum(A)*sum(B))

"""
숫자의 각 자리를 선택해야 하므로 str로 입력받아, map함수를 이용하여 각 자리수를 int로 바꿔 저장
각 자리를 곱해 더하는 것은 각 자리를 더해 곱하는 값과 같다.
"""