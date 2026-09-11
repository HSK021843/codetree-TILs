n = int(input())
parts = []

for i in range(1, n):
    if n % i == 0:
        parts.append(i)

if sum(parts) == n:
    print("P")
else:
    print("N")