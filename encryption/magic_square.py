import random


def is_magic_square(square):
    target_sum = sum(square[0])

    # Check rows
    for row in square:
        if sum(row) != target_sum:
            return False

    # Check columns
    for col in range(3):
        column_sum = 0
        for row in range(3):
            column_sum += square[row][col]
        if column_sum != target_sum:
            return False

    # Check diagonals
    if square[0][0] + square[1][1] + square[2][2] != target_sum:
        return False
    if square[0][2] + square[1][1] + square[2][0] != target_sum:
        return False

    return True


def generate_magic_squares():
    # List to store all magic squares
    magic_squares = [
        [
            [2, 7, 6], [9, 5, 1], [4, 3, 8]
        ],
        [
            [2, 9, 4], [7, 5, 3], [6, 1, 8]
        ],
        [
            [4, 3, 8], [9, 5, 1], [2, 7, 6]
        ],
        [
            [4, 9, 2], [3, 5, 7], [8, 1, 6]
        ],
        [
            [6, 1, 8], [7, 5, 3], [2, 9, 4]
        ],
        [
            [6, 7, 2], [1, 5, 9], [8, 3, 4]
        ],
        [
            [8, 1, 6], [3, 5, 7], [4, 9, 2]
        ],
        [
            [8, 3, 4], [1, 5, 9], [6, 7, 2]
        ]
    ]
    result = random.choice(magic_squares)

    return result


def find_in_matrix(value, input_matrix):
    size = len(input_matrix)
    for i in range(size):
        for j in range(size):
            if input_matrix[i][j] == value:
                return [i, j]

    return [-1, -1]


def encypt(string, magic_square):
    n = len(magic_square)
    string = string + " " * (n * n - len(string))
    res = [[" " for _ in range(n)] for y in range(n)]
    for i in range(len(string)):
        i_pos, j_pos = find_in_matrix(i + 1, magic_square)
        res[i_pos][j_pos] = string[i]
    return res


def decrypt(crypt_square, magic_square):
    string = ""
    for i in range(len(crypt_square) ** 2):
        i_pos, j_pos = find_in_matrix(i + 1, crypt_square)
        string += magic_square[i_pos][j_pos]
    return string
