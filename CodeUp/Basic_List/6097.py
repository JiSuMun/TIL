h, w = map(int, input().split()) # 세로, 가로
n = int(input()) # 막대개수
li = [[0]*w for _ in range(h)]
for i in range(n):
    l, d, x, y = map(int, input().split()) # 막대길이, 방향(가로:0, 세로: 1), 좌표   
    for j in range(l):
        if d == 0: li[x-1][y-1+j] = 1
        else: li[x-1+j][y-1] = 1
for i in li:
    print(*i)