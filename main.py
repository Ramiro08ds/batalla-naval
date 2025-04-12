#!/bin/env python3
from random import randrange
from enum import Enum
# Para comando de 'clear' y 'cls'
from os import system

SIZE: int = 10
shots: int = 17


# https://docs.python.org/3/howto/enum.html
class Square(Enum):
    def __str__(self) -> str:
        # https://www.geeksforgeeks.org/switch-case-in-python-replacement/
        match self:
            case Square.SHIP:
                return 'X'
            case Square.HIT:
                return '%'
            case Square.MISS:
                return 'O'
            case _:
                return '?'

    def add(self, n: int):
        '''Adds 2 squares together'''
        val = self.value
        self = Square.int(val + n)
        return self

    def int(n: int):
        '''Convierte int a Square'''
        if n >= len(Square):
            n -= len(Square)
        return Square(n)

    EMPTY = 0
    SHIP = 1
    MISS = 2
    HIT = 3


# https://www.w3schools.com/python/python_classes.asp
class Board:
    '''Representa a un lado del tablero'''

    def __init__(self, height: int, width: int, total_ships: int):
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        self.board = [[
                Square.EMPTY for _ in range(width)
        ] for _ in range(height)]
        while total_ships > 0:
            # https://docs.python.org/3/library/random.html#functions-for-integers
            row: int = randrange(SIZE)
            col: int = randrange(SIZE)
            if (self.board[row][col] == Square.SHIP):
                continue
            self.board[row][col] = Square.SHIP
            total_ships -= 1

    def __str__(self) -> str:
        text: str = ''
        for row in self.board:
            for col in row:
                text += col.__str__() + ' '
            text += '\n'
        return text

    def set(self, x: int, y: int, val: Square) -> None:
        '''Setea la casilla en (`x`, `y`) a `val`'''
        self.board[y][x] = val

    def fire(self, x: int, y: int) -> Square:
        '''Dispara a la casilla y retorna el resultado'''
        self.board[y][x] = self.board[y][x].add(2)
        return self.board[y][x]

    board: list[list[Square]]


total_ships: int = 17

board: Board = Board(SIZE, SIZE, total_ships)

print(board)

while True:
    cords_str: str = input("Coords(x, y): ")
    x: int = int(cords_str[0])
    y: int = int(cords_str[2])
    board.fire(x, y)
    system('clear')
    print(board)
    shots -= 1
