# 과거풀이
# 172ms
import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
li = [input().rstrip().split('.')[1] for _ in range(N)]
s = Counter(li)
print('\n'.join(i + ' ' + str(s[i]) for i in sorted(s.keys())))

"""
확장자만 필요하므로 split('.')[1] 로 입력받음
파일을 확장자 별로 정리해서 몇 개씩 있는지 알려줘 => Counter 사용해서 정리
보기 편하게 확장자들을 사전 순으로 정렬해 줘 => sorted(s.keys())
"""

# 현재풀이
# 156ms
import sys
input = sys.stdin.readline
def file():
    f = {}
    N = int(input())
    for _ in range(N):
        ext = input().rstrip().split('.')[1]
        f[ext] = f.get(ext, 0) + 1
    print('\n'.join(i + ' ' + str(f[i]) for i in sorted(f.keys())))
file()

"""
dict.get() => 시간복잡도 O(1)
Counter => 시간복잡도 O(N)
시간줄이기 위해 간편한 Counter 대신 dict.get(key, default) 사용
"""