string = list(input())

f, s = string[0], string[1]

for idx in range(len(string)):
    if string[idx] == f:
        string[idx] = s
    elif string[idx] == s:
        string[idx] = f

print(''.join(string))        