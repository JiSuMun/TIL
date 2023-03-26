# DFS와 BFS
# 80ms
"""
방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문 => 정렬
visited를 함수 안에 넣으면 반복될 때마다 초기화되므로 밖에서 정의하고 함수안에서 사용해야함
"""
import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)] # 인접리스트 생성하여 연결된 노드 저장

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

# 현재 노드 방문 후 연결된 노드들 중 방문하지 않은 노드 방문 반복하여 모든 노드 방문
def dfs(graph, V): 
    visited[V] = 1
    print(V, end=' ')
    for i in graph[V]:
        if not visited[i]:
            dfs(graph, i)

# 현재 노드 방문 후 연결된 노드들 중 방문하지 않은 노드 deque에 삽입 반복하여 모든 노드 방문
def bfs(graph, V):   
    d = deque([V])
    visited[V] = 1
    while d:
        a = d.popleft()
        print(a, end=' ')
        for i in graph[a]:
            if not visited[i]:
                d.append(i)
                visited[i] = 1
visited = [0] * (N+1)
dfs(graph, V)
print('')
visited = [0] * (N+1)
bfs(graph, V)

# 76ms
import sys
input = sys.stdin.readline
from collections import deque
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(V):
    visited[V] = 1
    dfs_li.append(V)
    for i in sorted(graph[V]):
        if not visited[i]:
            dfs(i)

def bfs(V):
    visited[V] = 1
    d = deque([V])
    while d:
        a = d.popleft()
        bfs_li.append(a)
        for j in sorted(graph[a]):
            if not visited[j]:
                visited[j] = 1
                d.append(j)

dfs_li = []
bfs_li = []
visited = [0] * (N+1)
dfs(V)
visited = [0] * (N+1)
bfs(V)
print(*dfs_li)
print(*bfs_li)
"""
방문한 노드의 리스트를 만들어 출력함
"""