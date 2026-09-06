target = input()
answer = []

for e in target:
    if e.isdigit():
        answer.append(int(e))

print(sum(answer))