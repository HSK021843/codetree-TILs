target = input()
answer = []

for e in target:
    tmp = ord(e)

    if tmp >= 65 and tmp <= 90:
        answer.append(e.lower())
    elif tmp >= 97 and tmp <= 122:
        answer.append(e.upper())

print(''.join(answer))