A, B = map(int, input().split())

answer = 0
for a in range(A, B + 1):
    answer += a

print(answer)