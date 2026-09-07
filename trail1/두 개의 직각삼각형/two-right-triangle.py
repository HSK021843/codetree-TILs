n = int(input())

cnt = n
space = 0
for _ in range(n):
    tmp = '*' * cnt + ' ' * space
    row = tmp + tmp[::-1]
    print(row)

    cnt -= 1
    space += 1