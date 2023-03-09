"""
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램
소수가 없을 경우에는 -1 출력
"""

# 과거 풀이
# 544ms
M = int(input())
N = int(input())
li = []
for i in range(M, N+1):
    c = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                c += 1
                break
        if c == 0:
            li.append(i)

if len(li) < 1:
    print(-1)
else:
    print(sum(li))
    print(min(li))

"""
모든 숫자를 다 검사해서 시간이 오래걸림
"""

# 현재 풀이
# 56ms
import sys
input = sys.stdin.readline
M = int(input())
N = int(input())
li = []

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        li.append(i)

if(len(li) == 0):
    print(-1)
else:
    print(sum(li))
    print(li[0])

"""
최대 약수는 sqrt(n)이므로 sqrt(n)까지만 검사, 만약 M이 100이면 50까지 검사
i까지 모든 수를 검사해봐도 되지만, 효율을 위해 i의 제곱근(i의 최대약수)까지만 검사
어떤 자연수의 약수의 개수는 제곱근을 기준으로 대칭이기 때문
"""
# 40ms
import sys
input = sys.stdin.readline
M = int(input())
N = int(input())
li = [1]*(N+1)
li[1] = 0
for i in range(2, int(N**0.5)+1):
    if li[i]:
        for j in range(i**2, N+1, i):
            li[j] = 0
li = [i for i in range(M, N+1) if li[i] == 1]
if sum(li) == 0: print(-1)
else:    
    print(sum(li))
    print(min(li))
"""
첫 반복문에서 소수가 아니면 0으로 바꿔줌
두 번째 반복에서 li는 소수인 것만 빼서 리스트화
"""