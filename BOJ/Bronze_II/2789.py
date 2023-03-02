"""
이메일의 각 단어 중에서 CAMBRIDGE에 포함된 알파벳은 모두 지우기로 했다.
"""

# 과거 풀이
# 36ms
str = list(input())
S = list('CAMBRIDGE')
s_list = []
for i in str:
    if i not in S:
        s_list.append(i)
print(*s_list, sep = '')

"""
str을 변수로 사용했었다.
이런 방식은 사용하면 안된다.
빈 결과 리스트를 만들고, 반복문을 돌려 리스트 S와 str을 비교하여 없다면 결과리스트에 넣어 출력했다.
"""

# 현재 풀이
# 40ms
import sys
input = sys.stdin.readline
s = input().rstrip()
for i in s:
    if i not in 'CAMBRIDGE': print(i, end='')

"""
문자열을 입력받고, 반복문을 돌려 'CAMBRIDGE'에 요소가 존재하지 않으면 출력하도록 했다.
"""