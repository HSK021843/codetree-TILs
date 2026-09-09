str_lst = ''.join(list(input().split('.')))
answer = []

for s in str_lst:
    if s.isalpha():
        answer.append(s.upper())

print(''.join(answer))