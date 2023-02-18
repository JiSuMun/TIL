a = int(input())
res = 0
if a >= 90: res = 'A'
elif 70 <= a < 90: res = 'B'
elif 40 <= a < 70: res = 'C'
else: res = 'D'
print(res)