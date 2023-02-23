# 오른쪽, 아래족으로만(벽에 막히면 아래) 이동 => 오른쪽, 아래로만 이동하니 DFS 불필요
# 갈수 있는 곳: 0, 벽: 1, 먹이: 2
# 먹이(2) 만나거나 (9, 9) 도착하면 break

li = [list(map(int, input().split())) for _ in range(10)]
x, y = 1, 1
li[1][1] = 9
while 1:
    if li[x][y] == 0: li[x][y] = 9
    elif li[x][y] == 2: li[x][y] = 9; break
    if li[x][y+1] == 1 and li[x+1][y] == 1: break
    if li[x][y+1] != 1: y += 1
    elif li[x+1][y] != 1: x += 1
for i in li:
    print(*i)