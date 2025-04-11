#!/bin/env python3

from random import randrange
from enum import Enum

class Square(Enum):
    def __str__(self):
        if(self.value == 0):
            return '-'
        if(self.value == 1):
            return 'X'
        if(self.value == 2):
            return 'O'
        if(self.value == 3):
            return '%'
    EMPTY = 0
    SHIP = 1
    MISS = 2
    HIT = 3

def printBoard(board: list[list[Square]]):
    for row in board:
        for col in row:
            print(col, end=" ")
        print()



SIZE: int = 10
SHOTS: int = 17

total_ships: int = 17

# https://www.w3schools.com/python/python_lists_comprehension.asp
board: list[list[Square]] = [[Square.EMPTY for _ in range(SIZE)] for _ in range(SIZE)]

# https://docs.python.org/3/library/random.html#functions-for-integers
while total_ships > 0:
    row: int = randrange(SIZE)
    col: int = randrange(SIZE)
    if(board[row][col]):
        continue
    board[row][col] = Square.SHIP
    total_ships -= 1

printBoard(board)
