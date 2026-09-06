n = int(input())
arr = [[0] * n for _ in range(n)]

for c in range(1, n + 1):
    for r in range(1, n + 1):
        arr[c - 1][r - 1] += (c  + (r - 1) * n)

for c in range(n):
    row = arr[c]
    print(' '.join(map(str, row)))