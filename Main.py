__author__ = 'Reede'
import random
import sys
import Methods as m

size = int(input("How many tiles do you want to play with? (must be a power of 2 and 9 is the minimum)"))
brd = [k for k in range(size)]
goodBoard = brd[:]
del goodBoard[0]
goodBoard.append(0)
random.shuffle(brd)
won = False

print("\nWelcome to the puzzle. Select a number next to the 0 to switch the position of those two tiles.")

m.printBoard(brd)

# print(brd)
# print(goodBoard)

count = 0
while(not m.checkBoard(brd, goodBoard)):
    choice = int(input("Swap tile #:"))
    if (not m.isValid(choice, brd)): #if the choice is invalid
        print("Invalid input. Choice must be present on the board and neighboring 0.")
    else:
        brd = m.makeMove(choice, brd)
        count +=1
    m.printBoard(brd)

print("You won in " + str(count) + " moves")