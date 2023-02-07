"""
그룹 단어: 주어진 문자열에서 각 문자가 연속해서 나타나는 경우
"""
# 과거 풀이
# 36ms
N = int(input())
result = N
for _ in range(N):
    s = input()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            pass
        elif s[i] in s[i+1:]:
            result -= 1
            break
print(result)

"""
첫 if문에서 알파벳이 연속적이면 통과
elif문에서 알파벳이 연속적이지 않으면서 뒤의 위치에 같은 알파벳이 있다면 단어개수 -1, break
"""

# 현재 풀이
# 40ms
import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    a = input()
    if list(a) != sorted(a, key=a.find): N -= 1       
print(N)
"""
1. 문자열을 리스트로 바꾼다.
2. 문자열을 find함수로 순서대로 확인하면서 등장하는 문자와 동일한 문자로 정렬
=> 알파벳 순서와 상관없이 첫 등장한 위치부터 중복되는 문자를 순서대로 나열해줌
1과 2의 결과가 같지 않으면 그룹단어가 아니기 때문에 -1해줌
"""