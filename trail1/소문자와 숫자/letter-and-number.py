target = input()
answer = ''

for e in target:
    if e in 'abcdefghijklmnopqrstuvwxyz1234567890':
        answer += e
    elif e in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        answer += e.lower()

print(answer)