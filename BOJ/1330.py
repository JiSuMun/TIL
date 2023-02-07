# 과거 풀이
# 36ms
A, B = map(int, input().split())

if A > B:
    print(">")
elif A < B:
    print("<")
elif A == B:
    print("==")

# 현재 풀이
# 40ms
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
print(">" if a > b else ("<" if a < b else "=="))

"""
과거에 풀었을 때보다 코드가 간결해짐
"""