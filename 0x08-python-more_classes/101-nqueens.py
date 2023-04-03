import sys

def print_board(board):
    for row in board:
        print(' '.join(row))

def is_valid(board, row, col, N):
    for i in range(N):
        if board[row][i] == 'Q' or board[i][col] == 'Q':
            return False
        if row-i >= 0 and col-i >= 0 and board[row-i][col-i] == 'Q':
            return False
        if row-i >= 0 and col+i < N and board[row-i][col+i] == 'Q':
            return False
        if row+i < N and col-i >= 0 and board[row+i][col-i] == 'Q':
            return False
        if row+i < N and col+i < N and board[row+i][col+i] == 'Q':
            return False
    return True

def solve(board, col, N):
    if col == N:
        print_board(board)
        print()
        return True
    result = False
    for row in range(N):
        if is_valid(board, row, col, N):
            board[row][col] = 'Q'
            result = solve(board, col+1, N) or result
            board[row][col] = '.'
    return result

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [['.' for _ in range(N)] for _ in range(N)]
solve(board, 0, N)
