# BFS(너비우선탐색) 풀이
# 72ms
import sys 
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
def BFS(board, a, b):
    queue = deque()
    queue.append((a,b))
    board[a][b] = 0 # 방문처리
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    queue.append((nx, ny))
    return

for _ in range(T):
    cnt = 0
    M, N, K = map(int,input().split())
    board = [[0]*N for _ in range(M)]
    for i in range(K):
        x, y = map(int, input().split())
        board[x][y] = 1
    
    for a in range(M):
        for b in range(N):
            if board[a][b] == 1:
                BFS(board, a, b)
                cnt += 1
    print(cnt)

"""
BFS(너비우선탐색) 알고리즘 이용한 풀이
배추흰지렁이는 하나의 배추에 존재하면 인접한 다른 배추에도 이동
따라서 배추가 인접한 곳이 몇 군데인지 찾아야함
BFS로 인접한 1을 0으로 만들어줌
2차원 리스트를 만들어 1인 경우 BFS를 실행하여 0으로 바꾸고, 한 번 실행될 때마다 cnt += 1
BFS함수가 인접한 모든 1을 0으로 만들어 배추가 인접한 곳의 개수를 구할 수 있다.
nx, ny를 큐에 추가해 반복문을 통해 popleft를 해주면서 인접한 곳으로 이동해 0으로 만드는 과정
"""
# DFS(깊이우선탐색) 풀이
# 52ms
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def DFS(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 1:
                board[nx][ny] = -1
                DFS(nx, ny)
    return

for _ in range(T):
    M, N, K = map(int,input().split())
    board = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                DFS(i, j)
                cnt += 1
    print(cnt)
# 52ms
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def DFS(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if board[ny][nx] == 1:
                board[ny][nx] = -1
                DFS(nx, ny)
    return

for _ in range(T):
    M, N, K = map(int,input().split())
    board = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
    for i in range(M):
        for j in range(N):
            if board[j][i] == 1:
                DFS(i, j)
                cnt += 1
    print(cnt)
"""
x,y위치와 M,N위치, i,j의 위치 잘 살피기
"""