"""
금민수는 어떤 수가 4와 7로만 이루어진 수
N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램
"""
# 과거 풀이
# 112ms
import sys
input = sys.stdin.readline
N = int(input())
while 1:
    flag = True
    for i in str(N):
        if i != '4'  and i != '7':
            flag = False
            N -= 1
    if flag:
        print(N)
        break

"""
N을 입력받고 while문을 사용하여 반복문을 돌리면서 가장 큰 것을 구하면 출력하며 종료하는 조건을 주었다.
입력받은 정수를 문자열로 바꾸고 그 문자열의 원소를 i로 for문의 반복문을 돌린다.
문자열의 원소가 4와 7이 아니면 금민수가 아니므로 False로 바꾸고 숫자를 하나씩 줄인다.
가장 큰 수부터 반복을 시작하기 때문에 작은 수부터 시작하는 것보다 반복 횟수를 줄일 수 있다.
"""

# 현재 풀이
# 44ms
def solve(n):
    res = n
    if n * 10 + 4 <= N:
        res = max(res, solve(n * 10 + 4))
    if n * 10 + 7 <= N:
        res = max(res, solve(n * 10 + 7))
    return res

N = int(input())
print(solve(0))

"""
함수 정의하여 사용
n=0부터 시작해야 4, 7도 가능
def문 안에서도 def로 반복해서 큰값을 res에 저장하여 리턴함
다시 풀어보니 시간복잡도 부분에서 상당히 개선되었다.
"""