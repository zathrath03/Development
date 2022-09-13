'''
Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0.
'''

def find_zeros(matrix: list[list]) -> list:
    zeros = [set(), set()]
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                zeros[0].add(r)
                zeros[1].add(c)
    return zeros


def zero_matrix(matrix: list[list]) -> None:
    zeros = find_zeros(matrix)
    rows, columns = zeros[0], zeros[1]
    for row in rows:
        for c in range(len(matrix[0])):
            matrix[row][c] = 0
    for col in columns:
        for r in range(len(matrix)):
            matrix[r][col] = 0

# This one is not currently working properly
def zero_matrix_constant_space(matrix: list[list]) -> None:
    first_row_has_zero = False
    first_col_has_zero = False
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                if r == 0:
                    first_row_has_zero = True
                if c == 0:
                    first_col_has_zero = True
                if r and c:
                    matrix [r][0] == 0
                    matrix [0][c] == 0
    for r in range(1, len(matrix)):
        if matrix[r][0] == 0:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
    for c in range(1, len(matrix[0])):
        if matrix[0][c] == 0:
            for r in range(len(matrix)):
                matrix[r][c] = 0
    if first_row_has_zero:
        for c in range(len(matrix[0])):
            matrix[0][c] = 0
    if first_col_has_zero:
        for r in range(len(matrix)):
            matrix[r][0] = 0

from random import randint
def generate_matrix(r, c):
    return [[randint(0,9) for _ in range(c)] for _ in range(r)]
