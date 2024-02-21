def calculate(N):
    tmp = 0
    for i in range(1, N + 1):
        tmp += i

    res = tmp // 10

    return res


N = int(input())
ans = calculate(N)

print(ans)