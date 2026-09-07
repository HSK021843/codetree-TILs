n = input()
lst = list(map(int, input().split()))

cnt = 0
idx = 0

while cnt < 3:
    if lst[idx] == 2:
        cnt += 1
        idx += 1
    else:
        idx += 1

print(idx)