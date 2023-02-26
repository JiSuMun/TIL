"""
오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력
가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목
"""

# 과거 풀이
# 60ms
import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
li = []
for i in range(N):
    li.append(input().strip())
li.sort()    
new = Counter(li).most_common()
print(new[0][0])

"""
리스트에 책 제목들을 입력받고, 정렬한 뒤 Counter를 사용하고, most_common을 사용하여 많은 순으로 정렬함 => 가장 앞의 데이터 뽑아옴
most_common: 데이터의 개수가 많은 순으로 정렬된 배열 리턴
미리 sort하고 Counter().most_common()을 하면 사전순으로 정렬되어 나옴
"""

# 현재 풀이
# 40ms
import sys
input = sys.stdin.readline
N = int(input())
li = []
d = {}
best = []
for _ in range(N):
    li.append(input().rstrip())
for i in list(set(li)): d[i] = li.count(i)
for k in d.keys():
    if d[k] == max(d.values()):
        best.append(k)
best.sort()
print(best[0])

"""
Counter를 사용하지 않고, 전체를 입력받은 리스트를 set으로 중복을 제거하여 다시 리스트로 만들어 준 뒤, 딕셔너리에 키값을 더하고, value는 중복제거 하기 전 리스트에서 count를 사용하여 개수를 세어 넣어준다.
.keys() 와 .values()를 사용하여 가장 큰 값을 가진 키값들을 새로운 리스트에 입력
그 리스트를 사전순으로 정렬하여 가장 앞의 값을 뽑음
"""
