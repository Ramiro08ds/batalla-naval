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

    EMPTY: int = 0
    SHIP: int = 1
    MISS: int = 2
    HIT: int = 3


# https://www.w3schools.com/python/python_classes.asp
class Board:
    '''Representa a un lado del tablero'''

    def __init__(self, height: int, width: int, total_ships: int):
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        self.board = [[
                Square.EMPTY for _ in range(width)
        ] for _ in range(height)]
        self.discovered = [[
                False for _ in range(width)
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
        for rowidx in range(len(self.board)):
            row = self.board[rowidx]
            for colidx in range(len(row)):
                col = row[colidx]
                if self.discovered[rowidx][colidx] or self.revealing:
                    text += col.__str__() + ' '
                else:
                    text += Square.EMPTY.__str__() + ' '
            text += '\n'
        return text

    def reveal(self) -> None:
        self.revealing = True
        print(self)
        self.revealing = False

    def set(self, x: int, y: int, val: Square) -> None:
        '''Setea la casilla en (`x`, `y`) a `val`'''
        self.board[y][x] = val

    def fire(self, x: int, y: int) -> bool:
        '''Dispara a la casilla y retorna el resultado'''
        if self.board[y][x] == Square.SHIP:
            self.board[y][x] = Square.HIT
            return True
        if self.board[y][x] == Square.EMPTY:
            self.board[y][x] = Square.MISS
        return False

    board: list[list[Square]]
    discovered: list[list[bool]]
    revealing: bool = False


total_ships: int = 17

board: Board = Board(SIZE, SIZE, total_ships)

print(board)

hits = 0
misses = 0

while shots > 0:
    system('clear')
    print(board)
    cords_str: str = input(f"Coords(x, y) (quedan {shots} disparos): ")

    if len(cords_str) != 3 or cords_str[1] != ',':
        print("Coordenadas inválidas. Deben tener el formato 'x,y'.")
        continue

    try:
        x = int(cords_str[0])
        y = int(cords_str[2])
    except ValueError:
        print("Coordenadas inválidas. Asegúrate de ingresar números.")
        input("Presioná Enter para continuar...")
        continue

    if not (0 <= x < SIZE and 0 <= y < SIZE):
        print(f"Coordenadas fuera de los límites del tablero ({SIZE}x{SIZE}). Intenta de nuevo.")
        input("Presioná Enter para continuar...")
        continue
    if board.discovered[y][x]:
        print("Ya habías disparado ahí.")
        input("Presioná Enter para continuar...")
        continue

    resultado = board.fire(x, y)
    board.discovered[y][x] = True

    if resultado:
        print("¡Acertaste!")
        hits += 1
    else:
        print("Fallaste.")
        misses += 1

    shots -= 1
    print(f"Te quedan {shots} disparos.")
    input("Presioná Enter para continuar...")

print("¡Se acabaron los disparos!")
print(f"Disparos acertados: {hits}")
print(f"Disparos fallados: {misses}")
print("Tablero final:")
board.reveal()
