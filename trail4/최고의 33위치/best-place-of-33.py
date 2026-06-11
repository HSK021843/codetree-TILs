n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
coins = [[0] * n for _ in range(n)]
mx_val = 0

for row_st in range(n):
    for col_st in range(n):
        row_ed, col_ed = row_st + 3, col_st + 3

        if row_ed <= n and col_ed <= n:
            tmp = 0

            for row in range(row_st, row_ed):
                for column in range(col_st, col_ed):
                    tmp += grid[row][column]

            coins[row_st][col_st] += tmp
            mx_val = max(tmp, mx_val)
        
        else:
            pass


print(mx_val)