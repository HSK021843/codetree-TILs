a, b = map(int, input().split())

answer = 0
for n in range(a, b + 1):
    if n % 2 == 0:
        answer += n

print(answer)