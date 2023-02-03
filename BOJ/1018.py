# 76ms
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]
res = []
for i in range(N-7): # 8*8크기이므로 이 지점부터 8*8크기의 체스판 검사할 것
    for j in range(M-7): # i, j는 칠할 부분 찾는 시작점
        a = 0 # 시작 지점이 흰색일때
        b = 0 # 시작 지점이 검은색일때
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0: # 짝수
                    if board[k][l] != 'W': a += 1
                    else: b += 1
                else: 
                    if board[k][l] != 'W': b += 1
                    else: a += 1
        res.append(a)
        res.append(b)
print(min(res))

"""
시작 지점이 흰색인지 검은색인지에 따라 체스판을 색칠하는 경우가 다르다.
시작지점과 같은 색의 칸은 (짝, 짝), (홀, 홀)로 (x,y)라 할 때, x+y는 짝수이다.
주어지는 체스판의 크기에서 8*8만큼 잘라야 하므로 N,M이 주어졌을때 -7을 한 수까지의 범위로 반복 시작
그 뒤 각 수에서 +8을 한 범위까지의 반복 시작
시작 지점의 색깔에 따른 최소 개수를 구하기 위해 리스트에 a,b의 최종값을 넣어 min사용
"""