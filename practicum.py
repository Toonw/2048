# Skeleton file for BVP Practicum
#
# You need to implement all functions in this file.
#
# If you implement them correctly, you can run this file to
# play the 2048 game.  For that to work, this file has to be
# in the same directory as the `game.py` file we provided.


# This imports our GUI code and allows you to play the game based on the
# functions you define in this file.
import game
from random import randint
import math


def initialize(dimension=4,nb_of_pieces=2,difficulty=2):

    # initializes a two-dimensional array with None elements
    board = [[None for i in range(dimension)] for j in range(dimension)]

    # places random pieces on random places in the array
    pieces_on_board = 0
    while pieces_on_board < nb_of_pieces:
        i = randint(0, dimension-1)
        j = randint(0, dimension-1)
        if (board[i][j] is None) & (pieces_on_board < nb_of_pieces):
            board[i][j] = math.pow(2, randint(1, difficulty))
            pieces_on_board += 1

    return board


def match(row):
    """
    Matches all identical elements in the row.
    """
    score = 0
    for i in range(len(row) - 1):
        if row[i] is not None:
            if row[i] == row[i + 1]:  # next to each other. ex: [2, 2, None]
                row[i] *= 2
                row[i + 1] = None
                score += row[i]
            elif row[i + 1] is None:  # not next to each other. ex: [2, None, 2]
                for e in range(i + 2, len(row)):
                    if row[e] is not None:
                        if row[e] == row[i]:
                            row[i] *= 2
                            row[e] = None
                            score += row[i]
                        else:
                            break
    return row, score  # Complete me


def reduce(row):
    """
    Removes the empty spaces in a row.
    """

    for e in range(len(row)):
        for i in range(len(row)):
            if row[i] is not None:
                if (i > 0) & (row[i - 1] is None):
                    row[i - 1] = row[i]
                    row[i] = None
    return row  # Complete me


def transpose(matrix):
    """
    Calculates the transpose of a matrix.
    """
    matrix = [list(x) for x in zip(*matrix)]
    return matrix  # complete me


def mirror(matrix):
    """
    Mirrors all rows in the matrix.
    """

    for i in range(len(matrix)):
        matrix[i].reverse()

    return matrix  # complete me


def has_empty_slot(matrix):
    """
    Checks for empty slots (`None`) elements in the matrix.
    """

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] is None:
                return True

    return False  # Complete me


def has_matches(matrix):
    """
    Checks if there are potential matches in the matrix.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] is not None:
                try:
                    if (matrix[i][j] == matrix[i+1][j]) or (matrix[i][j] == matrix[i][j+1]):
                        return True
                except IndexError:
                    break
                try:
                    if matrix[i+1][j] is None:
                        for e in range(i+1, len(matrix)):
                            if matrix[e][j] is not None:
                                if matrix[e][j] == matrix[i][j]:
                                    return True
                except IndexError:
                    break
                try:
                    if matrix[i][j+1] is None:
                        for e in range(i+1, len(matrix)):
                            if matrix[i][e] is not None:
                                if matrix[i][e] == matrix[i][j]:
                                    return True
                except IndexError:
                    break
    return False  # Complete me


def insert_new(matrix, number, difficulty=1):
    """
    Inserts `number` new elements in the matrix.
    """
    counter = 0
    while counter != number:
        if has_empty_slot(matrix):
            i = randint(0, len(matrix)-1)
            j = randint(0, len(matrix)-1)
            if matrix[i][j] is None:
                matrix[i][j] = math.pow(2, randint(1, difficulty))
                counter += 1

    return matrix  # Complete me


def should_continue(matrix):
    """
    Calculates whether the game should continue
    """
    if has_matches(matrix) | has_empty_slot(matrix):
        return True
    else:
        return False


def handle_key_press(board, score, direction):
    """
    Function called whenever there was a keypress.

    :param board: board state as returned by handle_key_press or initialize function
    :param score: players current score
    :param direction: symbol that was pressed ( one of "Up", "Down", "Left", "Right" )
    :return: new valid board state and the players new score
    """
    initialBoard =  origin(board)

    if direction == "Up":

        for i in range(len(board)):
            score += match(board[i])[1]
            reduce(board[i])

        if board != initialBoard:
            insert_new(board, 1, 2)

    elif direction == "Down":

        mirror(board)
        for i in range(len(board)):
            score += match(board[i])[1]
            reduce(board[i])
        mirror(board)

        if board != initialBoard:
            insert_new(board, 1, 2)

    elif direction == "Left":

        board = transpose(board)
        for i in range(len(board)):
            score += match(board[i])[1]
            reduce(board[i])
        board = transpose(board)

        if board != initialBoard:
            insert_new(board, 1, 2)

    elif direction == "Right":

        board = transpose(board)
        for i in range(len(board)):
            score += match(board[i])[1]
            reduce(board[i])
        mirror(board)
        for i in range(len(board)):
            reduce(board[i])
        mirror(board)
        board = transpose(board)

        if board != initialBoard:
            insert_new(board, 1, 2)

    return board, score   # Complete me


def origin(board):
    if len(board) == 0:
        return []
    return [list(board[0])] + origin(board[1:])


# This next bit of code initializes our GUI code with your functions
# `initialize`, `handle_key_press` and `should_continue` and starts
# the game.  The if test checks whether this file is being executed
# or just imported (e.g. for testing)
if __name__ == "__main__":
    game = game.Game(initialize, handle_key_press, should_continue)
    game.play()
