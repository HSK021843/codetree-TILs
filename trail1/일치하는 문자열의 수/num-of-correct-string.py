n, a = input().split(' ')

cnt = 0
for _ in range(int(n)):
    if input() == a:
        cnt += 1

print(cnt)