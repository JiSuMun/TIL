# 과거 풀이
# 36ms
C = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()
for i in C:
    str = str.replace(i, 'C')
print(len(str))

"""
알파벳을 미리 리스트에 넣어놓고, 문자열을 입력 받아 바꿔주도록 함
변수명을 str로 사용하지 않아야함.
"""

# 현재 풀이
# 44ms
import sys
input = sys.stdin.readline
C = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input().rstrip()
cnt = 0
for i in C:
    cnt += s.count(i)
print(len(s)-cnt)

"""
위 목록에 없는 알파벳은 한 글자씩 센다.
라고 했으므로 전체 길이에서 두 글자씩 취급하는 크로아티아 알파벳 개수만 세서 전체길이에서 빼준다.
"""
