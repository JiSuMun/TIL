a = int(input())
res = 0
if a // 3 == 1: res = 'spring'
elif a //3 == 2: res = 'summer'
elif a // 3 == 3: res = 'fall'
else: res = 'winter'
print(res)