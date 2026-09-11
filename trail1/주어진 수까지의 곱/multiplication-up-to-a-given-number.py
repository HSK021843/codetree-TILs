a, b = map(int, input().split())

answer = 1
for n in range(a, b + 1):
    answer *= n

print(answer)