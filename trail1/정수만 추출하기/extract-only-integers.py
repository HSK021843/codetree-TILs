strings = list(input().split(' '))
numbers = []

for e in strings:
    answer = ''

    for s in e:
        if s.isdigit():
            answer += s
        else:
            break

    numbers.append(int(answer))

print(sum(numbers))