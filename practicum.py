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


def initialize(dimension=4, nb_of_pieces=2, difficulty=2):
    """
    Initialization function.
    """

    board = [[None for i in range(dimension)] for j in range(dimension)]
    piecesOnBoard = 0
    while piecesOnBoard < nb_of_pieces:
        i = randint(0, dimension-1)
        j = randint(0, dimension-1)
        if (board[i][j] is None) & (piecesOnBoard < nb_of_pieces):
            board[i][j] = math.pow(2, randint(1, difficulty))
            piecesOnBoard += 1

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
                    if (row[e] is not None) & (row[e] == row[i]):
                        row[i] *= 2
                        row[e] = None
                        score += row[i]

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


def insert_new(matrix, number, difficulty=2):
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

    Should return a tuple with the new state of the
    board, the score and whether the game should continue.

    This function should calculate the new state of the board after
    all elements have been moved in the direction indicated by `direction`.
    All elements should be matched and then moved in the direction of the
    keypress.  If the state of the board has changed, new elements can
    be introduced in the board.

    We consider board to be a matrix where board[i][j] is the element in the i-th column
    of the board and j-th row of the board.

    Given the current score that is passed as an argument, the function should also
    update that value and return it as the second item in the tuple.

    Examples:
        >>> handle_key_press( [ [ 2, 2 ], [ None, 4 ] ], 0, "Up" )
        ( [ [ 4, None ], [ 4, None ] ], 4 )
        >>> handle_key_press( [ [ 4, None ], [ 4, None ] ], 4, "Left" )
        ( [ [ 8, None ], [ None, 2 ] ], 12 )
        >>> handle_key_press( [ [ 8, None ], [ None, 2 ] ], 12, "Right" )
        ( [ [ None, None ], [ 8, 2 ] ], 12 )
        >>> handle_key_press( [ [ None, None ], [ 8, 2 ] ], 12, "Down" )
        ( [ [ 2, None ], [ 8, 2 ] ], 12 )

    :param board: board state as returned by handle_key_press or initialize function
    :param score: players current score
    :param direction: symbol that was pressed ( one of "Up", "Down", "Left", "Right" )
    :return: new valid board state and the players new score
    """
    return (board, score)  # Complete me


# This next bit of code initializes our GUI code with your functions
# `initialize`, `handle_key_press` and `should_continue` and starts
# the game.  The if test checks whether this file is being executed
# or just imported (e.g. for testing)
if __name__ == "__main__":
    game = game.Game(initialize, handle_key_press, should_continue)
    game.play()
