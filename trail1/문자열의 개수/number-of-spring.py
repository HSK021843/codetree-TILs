count = 0
strings = []

while True:
    s = input()
    if s == '0':
        break

    strings.append(s)
    count += 1

print(count)

for i in range(0, len(strings), 2):
    print(strings[i])