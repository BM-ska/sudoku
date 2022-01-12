import tkinter
import tkinter as tk
import random
import sudoku.sudoku_base as sdb


class SudokuSolution:
    # Obiekt klasy to tablica sudoku

    def __init__(self, sudoku):
        self.sudoku = sudoku

    def write_sudoku(self):
        diagram = ""
        diagram += "\n"
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] != 0:
                    diagram += str(self.sudoku[i][j]) + " "
                else:
                    diagram += "  "

                if (j + 1) % 3 == 0 and j != 8:
                    diagram += " |  "

            diagram += "\n"
            if (i + 1) % 3 == 0 and i != 8:
                for j in range(25):
                    diagram += "-"
                diagram += "\n"

        print(diagram)

    def if_possible(self, s, row, column, val):
        # czy mozna wstawic liczbe na miejsce

        start_column = column - (column % 3)
        start_row = row - (row % 3)

        for i in range(9):
            if val == s[row][i] or val == s[i][column] or val == s[start_row + i % 3][start_column + i // 3]:
                return 0

        return 1

    def find_number(self, s, row, column):
        # znajdz prawidlowa liczbe

        for i in range(1, 10):
            if self.if_possible(s, row, column, i):
                return i
        return

    def if_only_one_number(self, s, row, column):
        # czy tylko jedna prawidlowa liczba pasuje

        correct_number = 0
        for i in range(1, 10):
            if self.if_possible(s, row, column, i):
                correct_number += 1

            if correct_number > 1:
                return 0
        if correct_number == 0:
            return 0
        return 1

    def s(self):
        # rozwiaz

        s = self.sudoku
        for i in range(81):
            for j in range(81):
                if s[j // 9][j % 9] == 0:
                    if self.if_only_one_number(s, j // 9, j % 9):
                        s[j // 9][j % 9] = self.find_number(s, j // 9, j % 9)
        self.sudoku = s

    def solve(self):
        # funkcja do rozwiazywania sudoku
        self.s()

        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] == 0:
                    return None


class Message:
    # wiadomosc do wyswietlania

    def __init__(self, option):
        if option == "start":
            self.text = "start the game"

        elif option == "clean":
            self.text = "clean board"

        elif option == "check_t":
            self.text = "there are no mistakes"

        elif option == "check_f":
            self.text = "incorrect"

        elif option == "generate":
            self.text = "new sudoku"

        elif option == "answer":
            self.text = "solution"


class Interface(tk.Frame):
    def __init__(self):
        self.padding = 5

        self.window = tk.Tk()
        self.window.title("Sudoku")
        self.window.geometry('600x400')
        # self.window.eval('tk::PlaceWindow . center')

        self.text_message = tk.StringVar()
        self.text_message.set(Message('start').text)

        self.label_message = tk.Label(self.window, textvariable=self.text_message)
        self.label_message.grid(row=0, column=1, padx=self.padding, pady=self.padding)

        self.frame_sudoku = tk.Frame(self.window)
        self.frame_buttons = tk.Frame(self.window)

        self.sudoku = [[tk.Entry(self.frame_sudoku, width=3) for x in range(9)] for y in range(9)]
        self.sudoku_solution = [[0 for x in range(9)] for y in range(9)]
        self.generated_sudoku = [[tk.Entry(self.frame_sudoku, width=3) for x in range(9)] for y in range(9)]
        self.is_generated = False

    def update_sudoku_solution(self):

        if self.is_generated:
            for x in range(9):
                for y in range(9):
                    if self.generated_sudoku[y][x].get() == '':
                        self.sudoku_solution[x][y] = 0
                    else:
                        self.sudoku_solution[x][y] = int(self.generated_sudoku[y][x].get())

        else:
            for x in range(9):
                for y in range(9):
                    if self.sudoku[y][x].get() == '':
                        self.sudoku_solution[x][y] = 0
                    else:
                        self.sudoku_solution[x][y] = int(self.sudoku[y][x].get())

        s = SudokuSolution(self.sudoku_solution)
        s.solve()
        self.sudoku_solution = s.sudoku

    def app_interface(self):
        self.option_buttons()
        self.sudoku_interface()

        tk.mainloop()

    def option_buttons(self):

        self.frame_buttons.grid(row=1, column=0, padx=self.padding, pady=self.padding)

        clean = tk.Button(self.frame_buttons, command=self.button_clean_click, text="clean", width=20)
        clean.grid(row=0, column=0, padx=self.padding, pady=self.padding)

        generate = tk.Button(self.frame_buttons, command=self.button_generate_click, text="generate", width=20)
        generate.grid(row=1, column=0, padx=self.padding, pady=self.padding)

        check = tk.Button(self.frame_buttons, command=self.button_check_click, text="check", width=20)
        check.grid(row=2, column=0, padx=self.padding, pady=self.padding)

        answer = tk.Button(self.frame_buttons, command=self.button_answer_click, text="show answer", width=20)
        answer.grid(row=3, column=0, padx=self.padding, pady=self.padding)

    def unlock_sudoku(self):
        for i in range(9):
            for j in range(9):
                self.sudoku[j][i].config(state='normal')

    def clean_sudoku(self):
        for i in range(9):
            for j in range(9):
                self.sudoku[i][j].delete(0, 'end')

    def compare_sudoku(self):
        self.update_sudoku_solution()

        for i in range(9):
            for j in range(9):
                if self.sudoku[j][i].get() != '':
                    if int(self.sudoku[j][i].get()) != self.sudoku_solution[i][j]:
                        return False
        return True

    def button_clean_click(self):
        self.text_message.set(Message('clean').text)
        self.unlock_sudoku()
        self.clean_sudoku()
        self.is_generated = False

    def button_generate_click(self):

        self.text_message.set(Message('generate').text)
        self.unlock_sudoku()
        self.clean_sudoku()

        number_of_sudoku = sdb.get_number_of_sudoku()
        numer = random.randint(1, number_of_sudoku)
        s = sdb.return_array_sudoku(numer)

        self.clean_sudoku()

        for i in range(9):
            for j in range(9):
                if s[i][j] != 0:
                    self.sudoku[j][i].insert(0, s[i][j])
                    self.sudoku[j][i].config(state='readonly')

        self.is_generated = True

        for x in range(9):
            for y in range(9):
                self.generated_sudoku[x][y].delete(0, 'end')
                self.generated_sudoku[x][y].insert(0, self.sudoku[x][y].get())

    def button_check_click(self):
        # kiedysco jezeli nie wygenerowany
        if self.compare_sudoku():
            self.text_message.set(Message('check_t').text)
        else:
            self.text_message.set(Message('check_f').text)

    def button_answer_click(self):
        self.text_message.set(Message('answer').text)
        # co jezeli nie znajdujemy rozwa
        # kiedys wypisz rozwa ale tylko na czerwono gdzie zle lub puste

        self.update_sudoku_solution()

        self.clean_sudoku()
        for i in range(9):
            for j in range(9):
                if self.sudoku_solution[i][j] != 0:
                    self.sudoku[j][i].insert(0, self.sudoku_solution[i][j])

    def sudoku_interface(self):
        self.frame_sudoku.grid(row=1, column=1, padx=self.padding, pady=self.padding)

        for i in range(9):
            for j in range(9):
                # self.sudoku[i][j].insert(0, i)

                self.sudoku[i][j].grid(column=i, row=j, padx=self.padding, pady=self.padding)

                if j == 3 or j == 6:
                    self.sudoku[i][j].grid(pady=(self.padding + 15, self.padding))

                if i == 3 or i == 6:
                    self.sudoku[i][j].grid(padx=(self.padding + 15, self.padding))


def main():
    interface = Interface()
    interface.app_interface()


if __name__ == "__main__":
    main()
