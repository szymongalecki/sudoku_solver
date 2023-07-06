from sudoku import Sudoku
from copy import deepcopy

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

solution = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


def test_solve():
    """Test correct Sudoku with unique solution"""
    s = Sudoku(puzzle)
    assert s.solve() == True and s.grid == solution


def test_solve_valid_dimensions():
    """Test incorrect Sudoku with invalid dimensions"""
    s = Sudoku(puzzle[:5])
    assert s.solve() == False


def test_solve_integer_entries():
    """Test incorrect Sudoku with string entry"""
    p = deepcopy(puzzle)
    p[0][0] = "A"
    s = Sudoku(p)
    assert s.solve() == False


def test_solve_valid_integers():
    """Test incorrect Sudoku with integers outside of 0-9 range"""
    p = deepcopy(puzzle)
    p[0][0] = 23
    s = Sudoku(p)
    assert s.solve() == False


def test_solve_unique_solution():
    """Test incorrect Sudoku with too few entries to have a unique solution"""
    zeros = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)]
    s = Sudoku(zeros)
    assert s.solve() == False


def test_solve_col_duplicates():
    "Test incorrect Sudoku with duplicate entries in column"
    p = deepcopy(puzzle)
    p[0][0] = 6
    s = Sudoku(p)
    assert s.solve() == False


def test_solve_row_duplicates():
    "Test incorrect Sudoku with duplicate entries in row"
    p = deepcopy(puzzle)
    p[0][0] = 3
    s = Sudoku(p)
    assert s.solve() == False


def test_solve_block_duplicates():
    "Test incorrect Sudoku with duplicate entries in 3x3 block"
    p = deepcopy(puzzle)
    p[0][0] = 9
    s = Sudoku(p)
    assert s.solve() == False
