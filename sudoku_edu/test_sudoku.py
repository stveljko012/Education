from unittest import TestCase
from sudoku import *

class TestSudoku(TestCase):

    def test_001_sudoku_case(self):
        pass

    def test_is_sudoku_squere(self):
        self.assertTrue(Sudoku([[1, 2, 4], [2, 4, 1], [4, 1, 2]]).is_square())
        self.assertTrue(Sudoku([[1, 2, 3, 4, 5], [2, 3, 1, 5, 6], [4, 5, 2, 1, 3], [3, 4, 5, 2, 1], [5, 6, 4, 3, 2]]).is_square())
        self.assertFalse(Sudoku([[1, 2, 4, 5], [2, 4, 1], [4, 1, 2]]).is_square())
        self.assertFalse(Sudoku([[1, 2, 4], [2, 4, 1], [4, 1, 2], [1, 2, 4]]).is_square())

        self.assertTrue(Sudoku([[8, 3, 7, 1, 9, 4, 6, 2, 5],
                                [5, 4, 9, 6, 2, 3, 7, 8, 1],
                                [6, 2, 1, 7, 8, 5, 9, 3, 4],
                                [2, 5, 6, 8, 1, 7, 4, 9, 3],
                                [4, 1, 3, 5, 6, 9, 2, 7, 8],
                                [9, 7, 8, 3, 4, 2, 5, 1, 6],
                                [1, 6, 4, 2, 7, 8, 3, 5, 9],
                                [7, 9, 5, 4, 3, 1, 8, 6, 2],
                                [3, 8, 2, 9, 5, 6, 1, 4, 7]]).is_valid_elements())

    def test_is_valid_elements(self):

        self.assertTrue(Sudoku([[1, 2, 4], [2, 4, 1], [4, 1, 2]]).is_valid_elements())
        self.assertFalse(Sudoku([[1, '2', 4], [2, 4, 1], [4, 1, 2]]).is_valid_elements())
        self.assertFalse(Sudoku([[1, 2, 4], [2, '4', 1], [4, 1, 2]]).is_valid_elements())
        self.assertFalse(Sudoku([[1, 2, 4], [2, 4, 1], [4, '1', 2]]).is_valid_elements())

        self.assertTrue(Sudoku([[8, 3, 7, 1, 9, 4, 6, 2, 5],
                                [5, 4, 9, 6, 2, 3, 7, 8, 1],
                                [6, 2, 1, 7, 8, 5, 9, 3, 4],
                                [2, 5, 6, 8, 1, 7, 4, 9, 3],
                                [4, 1, 3, 5, 6, 9, 2, 7, 8],
                                [9, 7, 8, 3, 4, 2, 5, 1, 6],
                                [1, 6, 4, 2, 7, 8, 3, 5, 9],
                                [7, 9, 5, 4, 3, 1, 8, 6, 2],
                                [3, 8, 2, 9, 5, 6, 1, 4, 7]]).is_valid_elements())

    def test_is_n_symbols_equal_n(self):
        self.assertTrue(Sudoku([[1, 2, 4], [1, 4, 1], [4, 1, 2]]).is_n_symbols())
        self.assertFalse(Sudoku([[1, 2, 4], [2, 4, 3], [4, 1, 2]]).is_n_symbols())
        self.assertFalse(Sudoku([[1, 2, 4], [2, 4, 3], [4, 1, 2]]).is_n_symbols())

        self.assertTrue(Sudoku([[8, 3, 7, 1, 9, 4, 6, 2, 5],
                                [5, 4, 9, 6, 2, 3, 7, 8, 1],
                                [6, 2, 1, 7, 8, 5, 9, 3, 4],
                                [2, 5, 6, 8, 1, 7, 4, 9, 3],
                                [4, 1, 3, 5, 6, 9, 2, 7, 8],
                                [9, 7, 8, 3, 4, 2, 5, 1, 6],
                                [1, 6, 4, 2, 7, 8, 3, 5, 9],
                                [7, 9, 5, 4, 3, 1, 8, 6, 2],
                                [3, 8, 2, 9, 5, 6, 1, 4, 7]]).is_n_symbols())



    def test_check_sudoku(self):
        self.assertTrue(Sudoku([[1, 2, 3],[2, 3, 1],[3, 1, 2]]).check_sudoku())
        self.assertTrue(Sudoku([[1, 2, 3], [2, 3, 1], [3, 1, 2]]).check_sudoku())
        self.assertTrue(Sudoku([[1, 2, 3], [2, 3, 1], [3, 1, 2]]).check_sudoku())

        self.assertTrue(Sudoku([[8, 3, 7, 1, 9, 4, 6, 2, 5],
                                [5, 4, 9, 6, 2, 3, 7, 8, 1],
                                [6, 2, 1, 7, 8, 5, 9, 3, 4],
                                [2, 5, 6, 8, 1, 7, 4, 9, 3],
                                [4, 1, 3, 5, 6, 9, 2, 7, 8],
                                [9, 7, 8, 3, 4, 2, 5, 1, 6],
                                [1, 6, 4, 2, 7, 8, 3, 5, 9],
                                [7, 9, 5, 4, 3, 1, 8, 6, 2],
                                [3, 8, 2, 9, 5, 6, 1, 4, 7]]).check_sudoku())

        self.assertFalse(Sudoku([[1, 2, 3, 4], [2, 3, 1, 3], [3, 1, 2, 3], [4, 4, 4, 4]]).check_sudoku())
        self.assertFalse(Sudoku([[1, 2, 4], [1, 4, 2], [4, 1, 2]]).check_sudoku())
        self.assertFalse(Sudoku([[1, 2, 4], [4, 2, 1], [4, 1, 2]]).check_sudoku())
        self.assertFalse(Sudoku([[1, 2, 3, 4], [2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 1, 2]]).check_sudoku())










