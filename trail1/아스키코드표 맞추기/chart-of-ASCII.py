target = list(map(int, input().split()))
answer = []

for n in target:
    answer.append(chr(n))

print(' '.join(answer))