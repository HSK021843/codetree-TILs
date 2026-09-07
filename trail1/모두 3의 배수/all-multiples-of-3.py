flag = 1
for _ in range(5):
    tmp = int(input())

    if tmp % 3 != 0:
        flag = 0
        break

print(flag)