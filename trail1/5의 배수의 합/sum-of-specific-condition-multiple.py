tmp_lst = list(map(int, input().split()))
a, b = min(tmp_lst), max(tmp_lst)

answer = 0
for n in range(a, b + 1):
    if n % 5 == 0:
        answer += n

print(answer)