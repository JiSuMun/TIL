# 완전탐색
# 모음사전
# 시간복잡도: O(5^5)
"""
이중 반복문 => 첫 번째 반복문은 1부터 5까지 5번 실행, 두 번째 반복문은 5의 i승번 실행

따라서 전체 실행 횟수는 5 + 5^2 + 5^3 + 5^4 + 5^5이며, 이는 대략 3,130번입니다. 이것은 입력 단어의 길이와 상관없이 항상 일정합니다.

따라서 이 코드의 시간 복잡도는 O(1)에 가깝습니다. 그러나 상수가 상당히 크므로 실행 시간이 길어질 수 있습니다.
"""
"""
중복순열 사용해서 모든 경우의 수 구함
"""
from itertools import product
def solution(word):
    res = []
    alpha = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for j in product(alpha, repeat=i):
            res.append(''.join(j))
    res.sort()
    return res.index(word) + 1

# 시간복잡도: O(N)
"""
취준 때 진수 관련 문제 많이 풀어서 5진수로 풀려고 했으나 처음에는 실패 => 구글링하여 해답 찾음
A, E, I, O, U에 각각 인덱스 값을 주면
주어진 word 는 
첫번째 자리 = (5^4 * 인덱스값) + (5^3 * 인덱스값) + (5^2 * 인덱스값) + (5^1 * 인덱스값) + (5^0 * (인덱스값+1))
두번째 자리 = (5^3 * 인덱스값) + (5^2 * 인덱스값) + (5^1 * 인덱스값) + (5^0 * (인덱스값+1))
세번째 자리 = (5^2 * 인덱스값) + (5^1 * 인덱스값) + (5^0 * (인덱스값+1))
네번째 자리 = (5^1 * 인덱스값) + (5^0 * (인덱스값+1))
다섯번째 자리 = 5^0 * (인덱스값+1)
"""
def solution(word):
    res = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    result = [5 ** i for i in range(5)] # 5진수값 저장
    for i in range(len(word)-1, -1, -1): # 큰 값부터 계산
        idx = alpha.index(word[i])
        for j in range(5-i):
            res += result[j] * idx
        res += 1
    return res