n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
min_size = float('inf')
for idx in range(n):
    tmp_x = []
    tmp_y = []

    for i in range(n):
        if idx != i:
            tmp_x.append(x[i])
            tmp_y.append(y[i])
    
    max_row = max(tmp_x) - min(tmp_x)
    max_col = max(tmp_y) - min(tmp_y)
    size = max_row * max_col

    min_size = min(min_size, size)

print(min_size)