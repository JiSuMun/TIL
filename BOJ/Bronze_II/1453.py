"""
피시방에는 1~100번까지 컴퓨터 있다.
들어오면서 번호를 말한다. 그 자리 사람 없으면 그 손님 앉아서 컴퓨터, 아니면 거절당한다.
거절당하는 사람의 수를 출력하는 프로그램
자리는 맨 처음에 모두 비어있고, 어떤 사람이 자리에 앉으면 자리를 비우는 일은 없다
"""
# 과거 풀이
# 48ms
import sys
input = sys.stdin.readline
N = int(input())
PC = list(map(int, input().split()))
cnt = 0
s = []
for i in range(N):
    if PC[i] in s:
        cnt += 1
    else:
        s.append(PC[i])
print(cnt)

"""
거절당하는 사람 수 cnt라는 변수 선언
손님이 앉고 싶어하는 자리 리스트 PC를 입력받음
손님수만큼 반복문을 돌리면서 빈 리스트 s에 PC리스트안의 자리가 있으면 cnt += 1, 없으면 리스트에 추가
"""

# 현재 풀이
# 36ms
import sys
input = sys.stdin.readline
N = int(input())
PC = list(map(int, input().split()))
s = len(list(set(PC)))
print(N-s)

"""
앉고 싶어하는 자리 리스트를 set으로 중복을 없앤 것을 리스트로 만들어 len으로 개수를 센다
거절당하는 사람 수 = 손님 수 - 중복없앤 자리리스트 개수
"""