# 시간복잡도: O(N log N)
from heapq import heappush, heappop
def solution(scoville, K):
    heap = []
    for i in scoville: heappush(heap, i)
    cnt = 0
    while heap[0] < K:
        try: heappush(heap, heappop(heap) + heappop(heap) * 2)
        except: return -1
        cnt += 1
    return cnt

"""
가장 작은 스코빌 지수가 K 이상이 될때까지 반복
heapq는 가지고 있는 요소를 push, pop할 때마다 자동으로 정렬
반복문을 돌면서 계산할 때마다 다시 heap에 추가
"""