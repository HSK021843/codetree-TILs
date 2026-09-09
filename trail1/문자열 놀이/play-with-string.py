s, q = map(str, input().split(' '))
s = list(s)

for _ in range(int(q)):
    order, target, change = map(str, input().split(' '))

    if order == '1':
        s[int(target) - 1], s[int(change) - 1] = s[int(change) - 1], s[int(target) - 1]
        print(''.join(s))
        
    elif order == '2':
        for idx in range(len(s)):
            if s[idx] == target:
                s[idx] = change
        print(''.join(s))