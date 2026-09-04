def line_writer(n):
    part = '*' * n
    line = ((part + ' ') * n).strip()

    return line


n = int(input())

for i in range(n, 0, -1):
    print(line_writer(i))