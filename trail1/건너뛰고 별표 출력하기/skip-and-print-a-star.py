n = int(input())
answer = []

for c in range(1, n + 1):
    answer.append(('*' * c))

for c in range(n - 1, 0, -1):
    answer.append(('*' * c))

print('\n\n'.join(answer))