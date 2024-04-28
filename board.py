import copy
import pygame
from sudoku_generator import generate_sudoku
from cell import Cell

class Board:
    def __init__(self, rows, cols, width, height, screen, difficulty, cell_size):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cell_size = cell_size

        if self.difficulty == "Easy":
            self.val = 30
        elif self.difficulty == 'Medium':
            self.val = 40
        else:
            self.val = 50
        self.answer_key = None
        self.original, self.answer_key = generate_sudoku(9, self.val)
        self.board = copy.deepcopy(self.original)
        self.cells = [
            [
                Cell(self.original[i][j], i, j, self.cell_size, self.screen)
                for j in range(self.cols)
            ]
            for i in range(self.rows)
        ]

    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw()
                k = 0
                while k < 4:
                    pygame.draw.line(self.screen, (0, 0, 0), (0, 3*k*self.cell_size),(self.width, 3*k*self.cell_size), 7)
                    pygame.draw.line(self.screen, (0, 0, 0), (3*k*self.cell_size, 0),(3*k*self.cell_size, self.height - self.cell_size), 7)
                    k += 1
                l = 1
                while l < 9:
                    pygame.draw.line(self.screen, (0, 0, 0), (0, l*self.cell_size), (self.width, l*self.cell_size),3)
                    pygame.draw.line(self.screen, (0, 0, 0), (l*self.cell_size, 0),(l*self.cell_size, self.height - self.cell_size), 3)
                    l += 1

    def initialize_board(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    cell.can_edit = True

    def select(self, row, col):
        if row < 9 and col < 9:
            self.draw()
            for line in self.cells:
                for cell in line:
                    cell.selected = False
            if self.cells[row][col].can_edit:
                self.cells[row][col].selected = True
                self.cells[row][col].draw()
            return row, col
        return 0, 0

    def click(self):
        pos = pygame.mouse.get_pos()
        x = pos[0] // self.cell_size
        y = pos[1] // self.cell_size
        return y, x

    def clear(self):
        for row in self.cells:
            for cell in row:
                if cell.selected:
                    cell.sketched_value = 0
                    cell.value = 0
                    cell.draw()
        pygame.display.update()

    def sketch(self, value):
        for row in self.cells:
            for cell in row:
                if cell.selected:
                    cell.set_sketched_value(value)
                    cell.draw()

    def place_number(self):
        i = 0
        while i < len(self.cells):
            row = self.cells[i]
            j = 0
            while j < len(row):
                cell = row[j]
                if cell.selected:
                    if cell.value == 0:
                        cell.set_cell_value(cell.sketched_value)
                        cell.sketched_value = 0
                        self.draw()
                        self.board[i][j] = cell.value
                j += 1
            i += 1
        pygame.display.update()

    def reset_to_original(self):
        self.board = copy.deepcopy(self.original)
        self.cells = [[Cell(self.board[i][j], i, j, self.cell_size, self.screen) for j in range(self.cols)] for i in range(self.rows)]

    def is_full(self):
        i = 0
        while i < len(self.board):
            row = self.board[i]
            j = 0
            while j < len(row):
                num = row[j]
                if num == 0:
                    return False
                j += 1
            i += 1
        return True

    def update_board(self):
        i = 0
        while i < len(self.cells):
            row = self.cells[i]
            j = 0
            while j < len(row):
                self.board[i][j] = self.cells[i][j].value
                j += 1
            i += 1

    def find_empty(self):
        for row in self.board:
            for num in row:
                if num == 0:
                    return (row, num)
        return True

    def check_board(self):
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                if self.board[i][j] != self.answer_key[i][j]:
                    return False
                j += 1
            i += 1
        return True
