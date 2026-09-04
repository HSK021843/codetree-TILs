def draw_square(n):
    for _ in range(n):
        print('*' * n)
    print()


n = int(input())

for _ in range(2):
    draw_square(n)