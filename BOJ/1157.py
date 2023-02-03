# 과거 풀이
# 76ms
S = input().upper()
s_list = list(set(S))
cnt = []
for i in s_list:
    cnt.append(S.count(i))
if cnt.count(max(cnt)) > 1: print('?')
else: print(s_list[cnt.index(max(cnt))])
    
"""
중복제거를 위해 set 사용(순서가 없어 인덱스가 없다 => 리스트로 변환)
cnt에 입력받은 문자열의 알파벳 개수를 추가
cnt 리스트에서 가장 높은 숫자가 2개 이상일 때 ? 출력
cnt 리스트에서 가장 높은 숫자의 인덱스 번호를 찾아서 s_list에서 알파벳 출력
"""

# 현재 풀이
# 116ms
import sys
from collections import Counter
input = sys.stdin.readline
s = input().upper().rstrip()
res = Counter(s).most_common()
ans = []
for i in res:
    if i[1] == res[0][1]: ans.append(i[0])
print('?') if len(ans) > 1 else print(*ans)

"""
Counter 클래스 활용
최빈값을 구하기 위해 Counter 클래스의 most_common() 메서드를 사용(횟수를 내림차순으로 정리함)
반복문을 돌리며 최대값이 다음 인덱스의 값과 같다면 ans에 알파벳을 추가
ans 리스트의 길이가 1 초과이면 ? 출력하게 함
"""

# 64ms
import sys
input = sys.stdin.readline
s = input().upper()
m_num = 0
for i in range(26):
    cnt = s.count(chr(i + 65))
    if m_num < cnt: m_num = cnt; m_char = chr(i + 65)        
    elif m_num == cnt: m_char = "?"
print(m_char)

"""
chr(0+65)~chr(25+65): 아스키코드에서 대문자 알파벳 A~Z
아스키코드에 해당하는 문자가 문자열에 있는지 count 함수로 세고 cnt 변수에 저장
cnt와 비교할 최대 개수 m_num 변수 선언
최대 개수가 cnt보다 작다면 cnt와 같다고 변경, 결과를 해당하는 알파벳으로 변경
그 이후 반복하면서 최대 개수가 이전의 cnt와 같다면 같은 최대 개수를 가진 알파벳이 존재한다는 것
=> 결과를 ?로 변경
"""