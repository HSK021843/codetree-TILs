def push_right(string):
    push = string[:-1]
    to_head = string[-1]

    return to_head + push

a = input()
b = input()

n = 0
while a != b:
    a = push_right(a)
    n += 1

    if n == len(a):
        n = -1
        break

print(n)