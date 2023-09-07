#!/usr/bin/python3
# 101-nqueens.py
"""Solves the N-queens puzzle.

Attributes:
    board (list): representing the chessboard.
    solutions (list): containing solutions.

"""
import sys


def init_board(n):
    """Initialize chessboard with 0's."""
    pzz = []
    [pzz.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in pzz]
    return (pzz)


def board_copy(pzz):
    """ return copy of chessboard."""
    if isinstance(pzz, list):
        return list(map(board_copy, pzz))
    return (pzz)


def get_solution(pzz):
    """Return the list of lists of a solved chessboard."""
    solution = []
    for r in range(len(pzz)):
        for c in range(len(pzz)):
            if pzz[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def dout(pzz, row, col):
    """X out spots on a chessboard.

    
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    
    for c in range(col + 1, len(pzz)):
        pzz[row][c] = "x"

    for c in range(col - 1, -1, -1):
        pzz[row][c] = "x"

    for r in range(row + 1, len(pzz)):
        pzz[r][col] = "x"

    for r in range(row - 1, -1, -1):
        pzz[r][col] = "x"

    c = col + 1
    for r in range(row + 1, len(pzz)):
        if c >= len(pzz):
            break
        pzz[r][c] = "x"
        c += 1

    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        pzz[r][c]
        c -= 1

    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(pzz):
            break
        pzz[r][c] = "x"
        c += 1

    c = col - 1
    for r in range(row + 1, len(pzz)):
        if c < 0:
            break
        pzz[r][c] = "x"
        c -= 1


def recr_solve(pzz, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        pzz (list): list of chessboard.
        row (int): The working row.
        queens (int): numb of placed queens.
        solutions (list): A list of lists of solutions.

    """
    if queens == len(pzz):
        solutions.append(get_solution(pzz))
        return (solutions)

    for c in range(len(pzz)):
        if pzz[row][c] == " ":
            tmp_board = board_copy(pzz)
            tmp_board[row][c] = "Q"
            dout(tmp_board, row, c)
            solutions = recr_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    pzz = init_board(int(sys.argv[1]))
    solutions = recr_solve(pzz, 0, 0, [])
    for sol in solutions:
        print(sol)
    print("Found %d solutions" % len(solutions))

    sys.exit(0)
# End of 101-nqueens.py
