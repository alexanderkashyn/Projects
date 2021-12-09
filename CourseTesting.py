from types import SimpleNamespace


def draw(board):
    for i in board:
        print(*i)

board = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]

draw(board)
game = True
sign = "x"

while game:
        x, y = map(int, input().split())
        # Check numbers for validation
        if 0 <= x <=2 and y in [0, 1, 2]:
                if board [x][y] == "-":
                        board [x][y] = sign
