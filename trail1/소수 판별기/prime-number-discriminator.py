import math

n = int(input())

flag = 'P'
for e in range(2, int(math.sqrt(n)) + 1):
    if n % e == 0:
        flag = 'C'
        break

print(flag)