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
    def __init__(self, grid: list[list[int]]) -> Sudoku:
        """Create new Sudoku instance"""
        self.grid = copy.deepcopy(grid)
        self.size = 9
        self.valid = False
        # Tests for valid Sudoku
        if not Sudoku.__valid_dimensions(grid):
            print("ERROR: Invalid dimensions")
            return
        if not Sudoku.__integer_entries(grid):
            print("ERROR: Not all entries are integers")
            return
        if not Sudoku.__valid_integers(grid):
            print("ERROR: Not all integers in range 0-9")
            return
        if not Sudoku.__unique_solution(grid):
            print("ERROR: Too few entries (< 17)")
            return
        if self.__col_duplicates():
            print("ERROR: Duplicate entries in column")
            return
        if self.__row_duplicates():
            print("ERROR: Duplicate entries in row")
            return
        if self.__block_duplicates():
            print("ERROR: Duplicate entries in block")
            return
        self.valid = True

    def __str__(self) -> str:
        """String representation of Sudoku object"""
        s = ""
        for row in self.grid:
            s += f"{row}\n"
        return s

    def __valid_dimensions(grid: list[list[int]]) -> bool:
        try:
            if len(grid) != 9 or len(grid[0]) != 9:
                return False
        except TypeError:
            return False
        else:
            return True

    def __integer_entries(grid: list[list[int]]) -> bool:
        """Check if all entries are integers"""
        return all(isinstance(d, (int)) for d in sum(grid, []))

    def __valid_integers(grid: list[list[int]]) -> bool:
        """Check if all entries are in range 0-9"""
        return all(d in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) for d in sum(grid, []))

    def __unique_solution(grid: list[list[int]]) -> bool:
        """Check if Sudoku has a unique solution - must have at least 17 entries"""
        return 81 - sum(grid, []).count(0) >= 17

    def __duplicates(self, f: function) -> bool:
        """Check if there are duplicates in collection returned by provided function"""
        for i in range(self.size):
            no_zeros = [d for d in f(i) if d != 0]
            if len(no_zeros) != len(set(no_zeros)):
                return True
        return False

    def __row_duplicates(self) -> bool:
        """Check if there are duplicated digits in rows"""
        return self.__duplicates(self.__row)

    def __col_duplicates(self) -> bool:
        """Check if there are duplicated digits in columns"""
        return self.__duplicates(self.__col)

    def __block_duplicates(self):
        """Check if there are duplicated digits in blocks"""
        return self.__duplicates(self.__blocks)

    def __row(self, r: int) -> list[int]:
        """Return r row of Sudoku"""
        return self.grid[r]

    def __col(self, c: int) -> list[int]:
        """Return c column of Sudoku"""
        return [d for d in [self.grid[r][c] for r in range(self.size)]]

    def __block(self, r: int, c: int) -> list[int]:
        """Return 3x3 block of digit in row r and column c"""
        b = []
        for r in range((r // 3) * 3, ((r // 3) * 3) + 3):
            for c in range((c // 3) * 3, ((c // 3) * 3) + 3):
                b.append(self.grid[r][c])
        return b

    def __blocks(self, i: int):
        """Return i 3x3 block of Sudoku"""
        b = []
        for r in range(3):
            for c in range(3):
                b.append(self.__block(r * 3, c * 3))
        return b[i]

    def __possible(self, r: int, c: int) -> list[int]:
        """Return list of possible digits to fill empty space in row r and column c"""
        digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        return list(
            digits - set(self.__block(r, c)) - set(self.__row(r)) - set(self.__col(c))
        )

    def __next(self) -> tuple[int, int] | None:
        """Return coordinates (r, c) of the next empty space, if it exists"""
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == 0:
                    return (r, c)
        return None

    def solve(self) -> bool:
        """Solve Sudoku defined by a grid if possible"""

        # do not solve invalid Sudoku
        if not self.valid:
            return False

        # get next empty field in Sudoku
        if self.__next():
            # there is an empty field
            r, c = self.__next()
        else:
            # there is no empty field, reached the end
            return True

        # set of possible digits for empty field in row r and column c
        digits = self.__possible(r, c)
        for d in digits:
            # assign possible digit for empty field
            self.grid[r][c] = d
            # if this digit is correct return true (Recursion)
            if self.solve():
                return True
            # otherwise reset it (Backtracking)
            self.grid[r][c] = 0
        return False


if __name__ == "__main__":
    s = Sudoku(puzzle)
    print(f"Sudoku:\n{s}")
    s.solve()
    print(f"Solution:\n{s}")
