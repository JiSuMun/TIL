# 72ms
import sys
input = sys.stdin.readline
N = int(input())
li = set(input().rstrip() for _ in range(N))
s_dict = {}
for i in li:
    if len(i) not in s_dict:
        s_dict[len(i)] = []
    s_dict[len(i)].append(i)
for j in sorted(s_dict):
    print(*sorted(s_dict[j]), sep = '\n')

"""
dict 이용 풀이
문자열을 readline으로 입력받아오면 개행문자도 포함이므로 rstrip사용
중복된 단어를 하나만 남기고 제거해야 하므로 단어를 입력 받아올 때 set사용
단어길이 기준으로 정렬해야 하므로 dict를 사용하여 key에 단어길이를 value에 단어를 넣음
이후 sorted 함수를 사용하여 dict를 정렬하여 단어길이 순으로 만든 후 반복문을 돌림
반복문을 돌린 후 결과를 출력할 때 sorted를 사용하면 value값이 사전 순으로 바뀜
"""

# 88ms
import sys
input = sys.stdin.readline
N = int(input())
li = []
for _ in range(N):
    li.append(input().rstrip())
s_li = list(set(li))
ss_li = []
for i in s_li:
    ss_li.append((len(i), i))
for j, k in sorted(ss_li):
    print(k)

"""
list 이용 풀이
문자열을 개행문자없이 리스트에 입력받아옴
이후 set으로 중복을 제거하고 list로 변환
또 다른 빈 리스트를 만든 후 단어길이와 단어를 튜플로 만들어 반복문을 통해 빈 리스트에 추가
새로운 리스트를 정렬하여 길이, 사전순으로 바꾼 뒤, 반복문을 돌려 단어만 출력
"""

# 68ms
import sys
input = sys.stdin.readline
N = int(input())
li = [input().rstrip() for _ in range(N)]
li = list(set(li))
li = sorted(li)
li.sort(key = len)
print(*li, sep='\n')
# 72ms
import sys
input = sys.stdin.readline
N = int(input())
li = [input().rstrip() for _ in range(N)]
li = list(set(li))
li = sorted(li) # 사전순
li = sorted(li, key = len) # 길이순
print(*li, sep='\n')

"""
list 이용 풀이_시간 개선
문자열을 개행문자없이 리스트에 입력받아옴
이후 set으로 중복을 제거하고 list로 변환
그 다음 sort 혹은 sorted사용하여 사전순, 길이순으로 정렬하여 출력
"""