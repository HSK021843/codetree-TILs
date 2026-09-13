n = int(input())
answer = 0

for _ in range(n):
    number = int(input())
    answer += number

tmp = str(answer)
print(tmp[1:] + tmp[:1])