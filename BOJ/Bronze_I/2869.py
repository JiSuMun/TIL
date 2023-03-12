"""
달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램
"""

# 과거 풀이
# 40ms
import math
A, B, V = map(int, input().split())
print(math.ceil((V-B)/(A-B)))

"""
높이가 V미터
낮에 A미터 올라감
밤에 B미터 미끄러짐
정상에서는 미끄러지지 않음
시간 = V / A-B : 정상에 올라가도 밤에 내려오는 계산
n일 걸린다 => 올라가는 횟수n, 내려가는 횟수 n-1
V = An - B(n-1) => n = (V-B)/(A-B)
"""

# 현재 풀이
# 40ms
import sys
input = sys.stdin.readline
A, B, V = map(int, input().split())
print((V-B-1) // (A-B)+1)

"""
위와 같은 방식, ceil을 사용하지 않은 풀이 
"""