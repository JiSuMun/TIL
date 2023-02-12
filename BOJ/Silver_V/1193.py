# 과거 풀이
# 52ms
X = int(input())
line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    up = X
    down = line - X + 1
else:
    up = line - X + 1
    down = X
print(f'{up}/{down}')

"""
라인은 1/1의 1줄부터 시작이다.
X가 대각선 line 수보다 작아질 때, 해당 대각선에 X가 있다.
대각선 라인 기준 지그재그
홀수 라인: 갈수록 분자-1, 분모+1 (분자 line->1)(분모 1->line)
짝수 라인: 갈수록 분자+1, 분모-1 (분자 1->line)(분모 line->1)
분수가 n라인에 n개 존재
대각선으로 각 줄을 나눠서 보면
line 1 = 1/1
line 2 = 1/2, 2/1
line 3 = 3/1, 2/2, 1/3
line 4 = 1/4, 2/3, 3/2, 4/1
X -= line => 몇 번째 line 인지 알 수 있다.
"""
# 현재 풀이
# 40ms
import sys
input = sys.stdin.readline
X = int(input())
line = 1
while X > line:
    X -= line
    line += 1
print('/'.join([str(line+1-X), str(X)][::2*(line%2)-1]))
"""
[::2*(line%2)-1] => 오름차순, 내림차순 => -1이면 값이 반대로 출력
2를 곱하는 이유는 홀수열은 그대로 출력하기 위해 값이 1이 되어야 하기 때문에 2를 곱해주고 -1함
"""