# 36ms
def hansu(n):
    h_count = 0
    for i in range(1, n+1):
        n_list = list(map(int, str(i)))
        if i < 100:
            h_count += 1
        elif n_list[0]-n_list[1] == n_list[1]-n_list[2]:
            h_count += 1
    return h_count

print(hansu(int(input())))

"""
한 자리, 두 자리 숫자는 비교 대상이 없기 때문에 모두 한수
세 자리 숫자부터 각 자리 숫자 간격 비교 가능하기 때문에 두자리까지는 모두 한수카운드 += 1
세자리부터 각 자리 숫자 차 비교
문제에서 N은 1000보다 작거나 같다고 한 조건이 있고, 1000은 한수가 아니기때문에
elif에서 각 자리 숫자의 인덱스 0, 1, 2만 비교
숫자는 각 자리 숫자를 분리 불가능 => for문에서 문자열로 변환시키고 각 자리수 분리해서 int변환
"""