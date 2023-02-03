# 36ms
import sys
input = sys.stdin.readline
x, y, w, h = map(int, input().split())
print(min(x, w-x, y, h-y))

"""
현재 위치(x, y), 왼쪽 아래 꼭짓점(0, 0), 오른쪽 위 꼭짓점(w, h)
직사각형 경계선까지 가는 거리 최솟값
가로, 세로 구분없이 최소거리만 찾으면 됨
현재위치 x, y 각 좌표에서 꼭짓점 x, y 좌표 까지 거리 4개 중 최솟값
"""