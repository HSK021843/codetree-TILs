a = input()
orders = input()

for order in orders:
    if order == 'L':
        a = a[1:] + a[:1]
    elif order == 'R':
        a = a[-1:] + a[:-1]

print(a)