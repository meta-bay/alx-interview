#!/usr/bin/python3
"""
0x05-Nqueens
"""
import sys


def check_position(chessboard, row_pos, col_pos, board_size):
    # Check this row on the left side
    for left in range(col_pos):
        if chessboard[row_pos][left] == 'Q':
            return False

    # Check upper diagonal on the left side
    row_check = row_pos
    col_check = col_pos
    while row_check >= 0 and col_check >= 0:
        if chessboard[row_check][col_check] == 'Q':
            return False
        row_check -= 1
        col_check -= 1

    # Check lower diagonal on the left side
    row_check = row_pos
    col_check = col_pos
    while row_check < board_size and col_check >= 0:
        if chessboard[row_check][col_check] == 'Q':
            return False
        row_check += 1
        col_check -= 1

    return True


def find_solutions(board_size):
    chessboard = [['.' for _ in range(board_size)] for _ in range(board_size)]
    all_solutions = []

    def search_solutions(col_pos):
        if col_pos == board_size:
            all_solutions.append(
                [[row_idx, row_val.index('Q')]
                 for row_idx, row_val in enumerate(chessboard)])
            return

        for row_pos in range(board_size):
            if check_position(chessboard, row_pos, col_pos, board_size):
                chessboard[row_pos][col_pos] = 'Q'
                search_solutions(col_pos + 1)
                chessboard[row_pos][col_pos] = '.'

    search_solutions(0)
    return all_solutions


def run_program():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = find_solutions(board_size)
    for single_solution in solutions:
        print(single_solution)


if __name__ == "__main__":
    run_program()
