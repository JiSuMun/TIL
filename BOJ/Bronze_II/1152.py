# 과거 풀이
# 56ms
string = list(input().split())
print(len(string))

# 현재 풀이
# 48ms
import sys
input = sys.stdin.readline
s = input().strip()
print(s.count(" ") + 1) if s else print(0)

"""
굳이 리스트로 입력 받지 않고도 문자열로 입력받아 공백의 개수 +1 을 하게 되면 문자열의 단어 개수를 알 수 있음

input()으로 입력 받을 때, 반복문으로 여러 줄을 입력 받게 되면 시간 초과가 발생할 수 있다.
이를 위해 import sys로 모듈을 불러오고 sys.stdin.readline()을 사용한다.
주의사항: sys.stdin.readline()은 개행문자가 같이 입력받아짐
=> 문제에 따라 개행문자를 제거하는 것이 좋다.
"""