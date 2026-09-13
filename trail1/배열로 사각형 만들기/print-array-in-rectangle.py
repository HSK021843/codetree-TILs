dx = [-1, 0]
dy = [0, -1]
board = [[0] * 5 for _ in range(5)]

for i in range(0, 5):
    for j in range(0, 5):
        if i == 0 or j == 0:
            board[j][i] += 1
        elif i != 0 and j != 0:
            for idx in range(0, 2):
                nj, ni = j + dy[idx], i + dx[idx]
                board[j][i] += board[nj][ni]

for row in board:
    print(*row)