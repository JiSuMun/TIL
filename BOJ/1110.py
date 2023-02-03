# 32ms
N = int(input())
n = N
cnt = 0
while True:
    a = n // 10
    b = n % 10
    c = (a + b) % 10
    n = (b * 10) + c
    cnt += 1
    if n == N: break       
print(cnt)

"""
1. 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리 숫자 더한다
=> a + b = (n//10) + (n%10)
2. 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙인다
원래 수로 돌아오는 사이클 구하기
=> 주어진 수의 가장 오른쪽 자리 수: b*10, 앞에서 구한 합의 가장 오른쪽 자리 수 = (a+b)%10
=> 사이클을 한 번 돌았으니 cnt += 1
=> 이후 n이 주어진 N과 같은 값이 되면 반복 종료
주어지는 0 < N <= 99 이므로 각 자리 숫자는 십의자리: N//10, 일의자리: N%10
사이클 수를 구하기 위해 반복문 전에 cnt 변수 선언
주어진 N은 반복문안에서 변경되면 안되므로 같은 값의 새로운 변수 n을 선언
"""