__author__ = 'Reede'
import sys, math

def printBoard(board):
    size = len(board)
    length = int(math.sqrt(size))
    top = "\n+"
    for p in range(0, length):
        top = top + " ---- +"
    print(top)
    for _ in range(0, length):
        for i in range(0, length):
            sys.stdout.write("|  %2d  " % board[i+(_*length)])
        sys.stdout.write("|")
        print(top)

def checkBoard(board, gb):
    if board == gb:
        return True
    return False

def isValid(choice, board):
    if ((not choice in board) or choice == 0):
        return False

    size = len(board)
    square = int(math.sqrt(size))
    index = board.index(0)

    # find all valid choices:
    valid = []
    mod = (index+1) % square
    if mod == 0: #is on right edge
        valid.append(board[index-1]) # add left
        valid.extend(topBot(index, square, board))
    elif mod == 1: # is on left edge
        valid.append(board[index+1]) # add right
        print ("ABOVE/BELOW")
        print("index: " + str(index) + "    square: " + str(square))
        valid.extend(topBot(index, square, board))
    else: #in middle
        valid.append(board[index-1]) # add left
        valid.append(board[index+1]) # add right
        valid.extend(topBot(index, square, board))
    print(valid, choice)
    if choice in valid:
        return True
    return False


def topBot(index, square, board):
    ret = []
    # CASE: not on TOP row
    if index >= square:
            # all above are valid
        ret.append(board[index-square])
    # CASE: NOT on BOTTOM row
    if index < square*(square -1):
        ret.append(board[index+square])
    return ret






def makeMove(choice, board):
    ci = board.index(choice)
    zi = board.index(0)
    board[ci], board[zi] = board[zi], board[ci]
    return board
