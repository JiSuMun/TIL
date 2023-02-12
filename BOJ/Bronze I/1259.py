"""
어떤 단어, 수를 뒤에서부터 읽어도 같다 => 팰린드롬
"""
# 과거 풀이
# 36ms
def pelindrome(num):
    N = len(num)
    for i in range(N//2):
        if num[i] != num[N-1-i]: return 'no'            
    return 'yes'
while True:
    num = int(input())
    if num == 0: break       
    print(pelindrome(str(num)))
"""
함수 선언해서 사용
num = 121
N = 3
N // 2 = 1
i = 0, num[0]=1, num[N-1-0]=2
num = 1231
N = 4
N // 2 = 2
i = 0, num[0]=1, num[N-1-0]=2
i = 1, num[1]=2, num[N-1-1]=3
"""          
# 36ms
import sys
while True:
    n = sys.stdin.readline().rstrip()
    if n == '0': break        
    else: print("yes") if n == n[::-1] else print("no")

"""
숫자를 문자열로 입력 받아와서 0이면 break
문자열과 거꾸로한 문자열이 같으면 팰린드롬, 아니라면 'no'출력
"""