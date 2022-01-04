import tkinter as tk


class Sudoku:
    def __init__(self):
        self.sudoku = [[tk.Entry(self.frame_sudoku, width=3) for x in range(9)] for y in range(9)]


class SudokuSolution:
    def __init__(self):
        self.sudoku_solution = [[0 for x in range(9)] for y in range(9)]