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
    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid
        self.size = 9

    def board(self):
        print(self.grid)

    def row(self, r: int) -> list[int]:
        return self.grid[r]

    def col(self, c: int) -> list[int]:
        return [d for d in [self.grid[r][c] for r in range(self.size)]]

    def block(self, r: int, c: int) -> list[int]:
        b = []
        for r in range((r // 3) * 3, ((r // 3) * 3) + 3):
            for c in range((c // 3) * 3, ((c // 3) * 3) + 3):
                b.append(self.grid[r][c])
        return b

    def possible(self, r: int, c: int) -> list[int]:
        digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        return list(
            digits - set(self.block(r, c)) - set(self.row(r)) - set(self.col(c))
        )

    def next(self) -> tuple[int, int] | None:
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == 0:
                    return (r, c)
        return None

    def solve(self):
        if self.next():
            r, c = self.next()
        else:
            return True

        digits = self.possible(r, c)
        for d in digits:
            self.grid[r][c] = d
            if self.solve():
                return True
            self.grid[r][c] = 0
        return False


s = Sudoku(puzzle)
s.solve()
s.board()


def row(puzzle: list[list[int]], r: int) -> list[int]:
    return puzzle[r]


def col(puzzle: list[list[int]], c: int) -> list[int]:
    return [digit for digit in [puzzle[r][c] for r in range(9)]]


def block(puzzle: list[list[int]], r: int, c: int):
    i = r // 3
    j = c // 3
    block = []
    for r in range(i * 3, (i * 3) + 3):
        for c in range(j * 3, (j * 3) + 3):
            block.append(puzzle[r][c])
    return block


def possible(puzzle: list[list[int]], r: int, c: int) -> list[int]:
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    return list(
        digits - set(block(puzzle, r, c)) - set(row(puzzle, r)) - set(col(puzzle, c))
    )


def next(puzzle: list[list[int]]) -> tuple[int, int] | None:
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return (r, c)
    return None


def solve(puzzle: list[list[int]]):
    if next(puzzle):
        r, c = next(puzzle)
    else:
        return True

    digits = possible(puzzle, r, c)
    for d in digits:
        puzzle[r][c] = d
        if solve(puzzle):
            return True
        puzzle[r][c] = 0
    return False


solve(puzzle)
print(puzzle)
