board = [list(map(int, input().split())) for _ in range(19)]
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(19):
        if board[i][b-1] == 1: board[i][b-1] = 0
        else: board[i][b-1] = 1
        if board[a-1][i] == 1: board[a-1][i] = 0
        else: board[a-1][i] = 1
for i in board:
    print(*i)