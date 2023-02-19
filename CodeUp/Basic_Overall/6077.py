n = int(input())
res = 0
for i in range(1, n+1):
    if i % 2 == 0:
        res += i
print(res)