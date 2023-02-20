n = int(input())
nums = list(map(int, input().split()))
res = [0]*24
for i in nums:
    res[i] += 1
print(*res[1:])