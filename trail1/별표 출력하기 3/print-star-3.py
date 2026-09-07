n = int(input())

cnt = n
space = 0
while cnt > 0:
    print((' ' * (space * 2)) + ('* ' * (2 * cnt - 1)).rstrip())
    cnt -= 1
    space += 1