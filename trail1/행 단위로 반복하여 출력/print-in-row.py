n = int(input())
row = []

for i in range(n):
    row.append(str(i + 1))

for _ in range(n):
    print(''.join(row))