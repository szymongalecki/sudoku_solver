from __future__ import annotations
import copy

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


class Sudoku:
    def __init__(self, grid: list[list[int]]) -> Sudoku | None:
        """Create new Sudoku instance"""
        self.grid = copy.deepcopy(grid)
        self.size = 9
        # reset grid and size if Sudoku is incorrect
        if self.col_duplicates() or self.row_duplicates() or self.block_duplicates():
            self.grid = []
            self.size = 0

    def __new__(cls, grid: list[list[int]]) -> Sudoku | None:
        """Basic tests for valid Sudoku"""
        # Sudoku is a 9x9 grid
        if len(grid) != 9 or len(grid[0]) != 9:
            return None
        # Sudoku must have at least 17 entries
        if 81 - sum(grid, []).count(0) < 17:
            return None
        return super(Sudoku, cls).__new__(cls)

    def __str__(self) -> str:
        """String representation of Sudoku object"""
        s = ""
        for row in self.grid:
            s += f"{row}\n"
        return s

    def duplicates(self, f: function) -> bool:
        """Check if there are duplicates in collection returned by provided function"""
        for i in range(self.size):
            no_zeros = [d for d in f(i) if d != 0]
            if len(no_zeros) != len(set(no_zeros)):
                return True
        return False

    def row_duplicates(self) -> bool:
        """Check if there are duplicated digits in rows"""
        return self.duplicates(self.row)

    def col_duplicates(self) -> bool:
        """Check if there are duplicated digits in columns"""
        return self.duplicates(self.col)

    def block_duplicates(self):
        """Check if there are duplicated digits in blocks"""
        return self.duplicates(self.blocks)

    def row(self, r: int) -> list[int]:
        """Return r row of Sudoku"""
        return self.grid[r]

    def col(self, c: int) -> list[int]:
        """Return c column of Sudoku"""
        return [d for d in [self.grid[r][c] for r in range(self.size)]]

    def block(self, r: int, c: int) -> list[int]:
        """Return 3x3 block of digit in row r and column c"""
        b = []
        for r in range((r // 3) * 3, ((r // 3) * 3) + 3):
            for c in range((c // 3) * 3, ((c // 3) * 3) + 3):
                b.append(self.grid[r][c])
        return b

    def blocks(self, i: int):
        """Return i 3x3 block of Sudoku"""
        b = []
        for r in range(3):
            for c in range(3):
                b.append(self.block(r * 3, c * 3))
        return b[i]

    def possible(self, r: int, c: int) -> list[int]:
        """Return list of possible digits to fill empty space in row r and column c"""
        digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        return list(
            digits - set(self.block(r, c)) - set(self.row(r)) - set(self.col(c))
        )

    def next(self) -> tuple[int, int] | None:
        """Return coordinates (r, c) of the next empty space, if it exists"""
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == 0:
                    return (r, c)
        return None

    def solve(self):
        """Solve Sudoku defined by a grid"""
        if self.next():
            # there is an empty field in Sudoku
            r, c = self.next()
        else:
            # there is no empty field in Sudoku, reached the end
            return True
        # set of possible digits for empty field in row r and column c
        digits = self.possible(r, c)
        for d in digits:
            # assign possible digit for empty field
            self.grid[r][c] = d
            # if this digit is correct return true
            if self.solve():
                return True
            # otherwise reset it
            self.grid[r][c] = 0
        return False


s = Sudoku(puzzle)
print(s)
s.solve()
print(s)
