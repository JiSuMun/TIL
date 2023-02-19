num = int(input())
n = 1
res = 0
while 1:
    if res >= num: break
    res += n
    n += 1  
print(n-1)