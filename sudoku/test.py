import unittest
import sudoku.app
import sudoku.sudoku_base

sudoku = [[9, 8, 0, 0, 0, 2, 3, 0, 0],
          [0, 0, 3, 5, 4, 9, 0, 7, 0],
          [0, 5, 0, 8, 3, 0, 4, 9, 6],
          [8, 0, 2, 0, 0, 0, 0, 0, 4],
          [7, 0, 5, 3, 0, 0, 1, 0, 2],
          [1, 9, 6, 0, 8, 0, 5, 0, 0],
          [0, 0, 9, 0, 6, 3, 8, 5, 1],
          [3, 7, 8, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0]]

sudoku_rozw = [[9, 8, 4, 6, 7, 2, 3, 1, 5],
               [6, 1, 3, 5, 4, 9, 2, 7, 8],
               [2, 5, 7, 8, 3, 1, 4, 9, 6],
               [8, 3, 2, 1, 5, 7, 9, 6, 4],
               [7, 4, 5, 3, 9, 6, 1, 8, 2],
               [1, 9, 6, 2, 8, 4, 5, 3, 7],
               [4, 2, 9, 7, 6, 3, 8, 5, 1],
               [3, 7, 8, 4, 1, 5, 6, 2, 9],
               [5, 6, 1, 9, 2, 8, 7, 4, 3]]


class TestDatabase(unittest.TestCase):
    def test_if_add_sudoku_change_number_of_sudoku(self):
        before = sudoku_base.get_number_of_sudoku()
        sudoku_base.add_sudoku(sudoku, "test")
        after = sudoku_base.get_number_of_sudoku()

        self.assertEqual(before, after - 1)

    def test_return_sudoku_with_index_outside_db(self):
        self.assertRaises(ValueError, sudoku_base.return_array_sudoku, sudoku_base.get_number_of_sudoku() + 1)

    def test_return_sudoku_with_index_not_int(self):
        self.assertRaises(ValueError, sudoku_base.return_array_sudoku, "a")

    def test_if_sudoku_format_is_correct(self):
        self.assertRaises(ValueError, sudoku_base.add_sudoku, [[1, 2], [3, 4]], "test")

    def test_if_sudoku_format_is_correct2(self):
        self.assertRaises(ValueError, sudoku_base.add_sudoku, [["asss", 2], [3, 4]], "test")

    def test_if_sudoku_format_is_correct3(self):
        self.assertRaises(ValueError, sudoku_base.add_sudoku, [["a", 8, 4, 6, 7, 2, 3, 1, 5],
                                                               [6, 1, 3, 5, 4, 9, 2, 7, 8],
                                                               [2, 5, 7, 8, 3, 1, 4, 9, 6],
                                                               [8, 3, 2, 1, 5, 7, 9, 6, 4],
                                                               [7, 4, 5, 3, 9, 6, 1, 8, 2],
                                                               [1, 9, 6, 2, 8, 4, 5, 3, 7],
                                                               [4, 2, 9, 7, 6, 3, 8, 5, 1],
                                                               [3, 7, 8, 4, 1, 5, 6, 2, 9],
                                                               [5, 6, 1, 9, 2, 8, 7, 4, 3]], "test")


class TestSudokuSolution(unittest.TestCase):
    def test_if_solution_is_correct(self):
        s = app.SudokuSolution(sudoku)
        s.solve()

        self.assertEqual(s.sudoku, sudoku_rozw)


if __name__ == '__main__':
    unittest.main()
