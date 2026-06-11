n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
avg = int(sum(blocks) / len(blocks))
cnt = 0

for n in blocks:
    if n > avg:
        cnt += (n - avg)

print(cnt)