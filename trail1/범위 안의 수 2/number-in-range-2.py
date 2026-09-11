tmp = []

for _ in range(10):
    n = int(input())

    if n >= 0 and n <= 200:
        tmp.append(n)

print(sum(tmp), round(sum(tmp) / len(tmp), 1))