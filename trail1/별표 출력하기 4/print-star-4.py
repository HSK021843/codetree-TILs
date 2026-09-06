n = int(input())

for c in range(n, 0, -1):
    print(('* ' * c).strip())

for c in range(2, n + 1):
    print(('* ' * c).strip())