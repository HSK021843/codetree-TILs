n = int(input())

answer = 0
for _ in range(n):
    num = int(input())

    if num % 2 == 1 and num % 3 == 0:
        answer += num

print(answer)