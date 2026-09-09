string = list(input())
change = string[0]
target = string[1]

for idx in range(len(string)):
    if string[idx] == target:
        string[idx] = change

print(''.join(string))