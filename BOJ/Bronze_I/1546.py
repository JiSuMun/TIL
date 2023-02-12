"""
점수 중 최댓값을 제외한 나머지 점수를 점수/최대점수*100 고쳐 평균 구하기
"""

# 과거 풀이
# 36ms
N = int(input())
nums = list(map(int, input(). split()))
M = max(nums)
list = []
for i in nums:
    list.append(i/M*100)
print(sum(list)/len(list))

"""
점수 변환하는 반복문을 사용하여 구했다. 사용하지 않아도 되는 반복문이다.
"""

# 현재 풀이
# 40ms
import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int,input().split()))
print((sum(L)/max(L)*100) / N)

"""
과거풀이와는 달리 점수를 모두 합하고 변환하여 반복문을 사용하지 않고 풀었다.
"""