"""
대칭 차집합
"""
# 과거 풀이
# 296ms
import sys
input = sys.stdin.readline
A, B = map(int, input().split())
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(len((s1-s2) | (s2-s1)))

"""
각각 s1과 s2의 차집합을 구해서 합집합하여 개수를 세었다.
대칭차집합 = (A-B) | (B-A)
"""

# 현재 풀이
# 164ms
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
A = list(input().split())
B = list(input().split())
print(2 * len(set(A + B)) - a - b)
"""
(A-B) = (A+B)-B, (B-A) = (A+B)-A 이용
"""
# 172ms
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
def sol():
    cnt = 0
    set_B = set(B)
    for a in A:
        if a in set_B:
            cnt += 1
    print(N + M - (cnt * 2))   
sol()

"""
합집합 개수에서 교집합 개수를 각각 빼줌
대칭차집합 개수 = (len(A)-cnt) + (len(B)-cnt)
"""