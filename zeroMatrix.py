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


