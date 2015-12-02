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
        i = randint(0, 3)
        j = randint(0, 3)
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

    Examples:
        >>> has_empty_slot( [ [ 1 ] ] )
        False
        >>> has_empty_slot( [ [ None ] ] )
        True
        >>> has_empty_slot( [ [ 2, 2 ], [ 4, 4 ] ] )
        False
        >>> has_empty_slot( [ [ 2, None ], [ 4, 4 ] ] )
        True
        >>> has_empty_slot( [ [ 2, None ], [ 4, None ] ] )
        True

    :param matrix: matrix to check
    :rtype matrix: list[ list[ int | None ] ]
    :return: whether there is an empty slot
    :rtype boolean
    """
    return True  # Complete me


def has_matches(matrix):
    """
    Checks if there are potential matches in the matrix.

    There is a potential match in the matrix if in any of the rows
    or columns contain two identical elements next to each other or
    only separated by `None`'s.

    Examples:
        >>> has_matches( [ [ 2, None ], [ None, 2 ] ] )
        False
        >>> has_matches( [ [ 2, 2 ], [ None, None ] ] )
        True
        >>> has_matches( [ [ 2, None ], [ 2, None ] ] )
        True
        >>> has_matches( [ [ 2, 4 ], [ 4, 2 ] ] )
        False
        >>> has_matches( [ [ 2, None, 2 ], [ None, None, None ], [ None, None, None ] ] )
        True
        >>> has_matches( [ [ 2, 4, 2 ], [ None, None, None ], [ None, None, None ] ] )
        False
        >>> has_matches( [ [ 2, None, None ], [ None, None, None ], [ 2, None, None ] ] )
        True
        >>> has_matches( [ [ None, None, 2 ], [ None, None, 2 ], [ None, None, None ] ] )
        True
        >>> has_matches( [ [ 2, None, None ], [ None, None, None ], [ None, None, 2 ] ] )
        False
        >>> has_matches( [ [ 2, None, None ], [ None, 2, None ], [ None, None, 2 ] ] )
        False

    :param matrix: matrix to check for matches
    :rtype matrix: list[ list[ int | None ] ]
    :return: whether there are any matches
    :rtype: boolean
    """
    return False  # Complete me


def insert_new(matrix, number, difficulty=2):
    """
    Inserts `number` new elements in the matrix.  The maximum log2 of the newly
    introduced elements should be difficulty.

    This method should introduce new elements in the matrix.  The number of
    elements to introduce is given by `number`.  The location of the new elements
    should be chosen at random.

    To make the game more difficult, the elements introduced could also be greater
    than 2.  This is achieved through the `difficulty` argument.  Given a `difficulty` of
    `n`, this function should only introduce elements smaller or equal to math.pow( 2, n ).
    The power of 2 for the new elements can be chosen randomly from the range 1 to n,
    including both 1 and n.

    If `number` is greater than the number of empty slots in the board.  The function
    should simply fill the board, not overriding any of the existing elements.

    Examples:
        >>> insert_new( [ [ 8, 8 ], [ 8, 8 ] ], 1, 1 )
        [ [ 8, 8 ], [ 8, 8 ] ]
        >>> insert_new( [ [ 8, 8 ], [ 8, None ] ], 1, 1 )
        [ [ 8, 8 ], [ 8, 2 ] ]
        >>> insert_new( [ [ None, None ], [ None, None ] ], 4, 3 )
        [ [ 2, 4 ], [ 2, 8 ] ]
        >>> insert_new( [ [ None, None ], [ None, None ] ], 2, 2 )
        [ [ 2, None ], [ 4, None ] ]
        >>> insert_new( [ [ None, None ], [ None, None ] ], 2, 1 )
        [ [ None, 2 ], [ None, None ] ]

    :param matrix: matrix to insert new elements into
    :type matrix: list[ list[ int | None ] ]

    :param number: number of elements to introduce
    :type number: int

    :param difficulty: maximum log2 of the new elements
    :type difficulty: int

    :return: matrix with new elements
    :rtype: list[list[int | None]]
    """
    return matrix  # Complete me


def should_continue(matrix):
    """
    Calculates whether the game should continue

    The game should continue as long as there are empty slots
    in the game or there are matches possible.

    :param matrix: current board state
    :return: whether there are empty slots or matches left in the board
    """
    return True  # Complete me


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
