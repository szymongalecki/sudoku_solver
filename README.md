# Classic 9x9 Sudoku solver
Small Python project to not get rusty, ingredients:
- OOP
- Input validation
- Type annotations
- Assignment vs Copy vs Deepcopy
- Private and Dunder methods
- Built-in functions
- Passing functions as arguments
- List comprehensions
- Set theory
- Navigating 2D array
- Recursion with backtracking
### Algorithm
```python
def solve(self) -> bool:
        """Solve Sudoku defined by a grid if possible"""
       
        # Get next entry to fill
        if self.__next():
            r, c = self.__next()
        else:
            # Reached the end of Sudoku
            return True

        # Set of possible digits for that entry
        digits = self.__possible(r, c)

        for d in digits:
            # Assign digit to entry
            self.grid[r][c] = d

            # If this digit is part of correct solution, return true << Recursion >>
            if self.solve():
                return True

            # This digit was not part of correct solution, reset entry << Backtracking >>
            self.grid[r][c] = 0

        # No solution exists
        return False
```

### Sources
- Inspired by : [Codewars Kata](https://www.codewars.com/kata/5296bc77afba8baa690002d7)
- What is Sudoku : [Sudoku](https://en.wikipedia.org/wiki/Sudoku)
