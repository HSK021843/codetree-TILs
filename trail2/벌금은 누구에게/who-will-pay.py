N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
penalty_count = [0] * (N + 1)

std_number = 0
for std in student:
    tmp = int(std)
    penalty_count[tmp] += 1

    if penalty_count[tmp] >= K:
        std_number += tmp
        break

print(-1 if std_number == 0 else std_number)