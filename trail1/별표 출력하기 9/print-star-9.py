n = int(input())
answer = []

space = n - 1
for s in range(1, n + 1):
    answer.append((' ') * (space * 2) + ('* ' * (2 * s - 1)).strip())
    space -= 1

print('\n'.join(answer))