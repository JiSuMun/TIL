"""
알파벳 소문자로 이루어진 단어에서 임의의 두 부분을 골라서 단어를 쪼갠다.
각각은 적어도 길이가 1 이상인 단어여야 한다.
나눈 세 개의 단어를 앞뒤로 뒤집고, 다시 원래의 순서대로 합친다.
이렇게 만든 단어 중 사전순으로 가장 앞선 단어를 출력
"""
# 과거 풀이
# 40ms
import sys
input = sys.stdin.readline
s = input().rstrip()
N = len(s)
s_li = []
for i in range(1, N-1):
    for j in range(i+1, N):
        ns = s[:i][::-1] + s[i:j][::-1] + s[j:][::-1]
        s_li.append(ns)
print(min(s_li))

"""
문자열을 입력받으므로 rstrip이용해서 개행문자 없이 입력받아옴
문자열을 슬라이싱하기 위해 문자열의 개수를 세고, 자르는 부분을 i와 j로 결정
세 단어가 각각 1개 이상의 길이가 되어야 하므로 1<=i<N-1, i+1<=j<N으로 범위를 정함
새롭게 만든 단어들을 s_li에 집어넣고 사전순으로 가장 앞선 단어를 출력해야 하므로
=> 가장 작은 단어 출력 => min함수 이용
"""

# 현재 풀이
# 40ms
import sys
input = sys.stdin.readline
word = input().rstrip()
n = len(word)
ans = 'z' * n
for i in range(n - 2): # 두 군데 선택돼야 함
    t = word[:i + 1][::-1]
    for j in range(i + 1, n - 1):
        s = t + word[i + 1:j + 1][::-1] + word[j + 1:][::-1]
        if s < ans:
            ans = s
print(ans)
"""
min함수를 사용하지 않고도 사전순으로 가장 앞선 단어를 구할 수 있다.
'z'*(len(word)) 는 사전 순 가장 마지막 단어가 된다.
위의 풀이와 다르게 i와 j의 범위에서 0을 포함했으므로 i<n-2, i+1<=j<n-1이 된다.
또한 단어들을 구해서 if문으로 사전 순 가장 마지막 단어인 ans와 비교하고 ans에 단어를 해당
=> min없이 가장 앞선 단어 구할 수 있음
"""
# 40ms
import sys
input = sys.stdin.readline
s = input().rstrip()[::-1]
n = len(s)
print(min(s[j:]+s[i:j]+s[:i] for i in range(1,n) for j in range(i+1,n)))

"""
위의 두 풀이와 다르게 처음 입력 받아올 때부터 문자열을 거꾸로 입력 받아옴
나눈 세 개의 단어를 앞뒤로 뒤집고, 다시 원래의 순서대로 합쳐야 하므로
단어의 순서가 위의 두 풀이와 다르다.
"""