def first_half(n):
    for c in range(1, n + 1):
        print(('* ' * c).strip())


def second_half(n):
    for c in range(n - 1, 0, -1):
        print(('* ' * c).strip())



n = int(input())

first_half(n)
second_half(n)