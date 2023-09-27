import random

class Minesweeper:
    def __init__(self, size, mines):
        self.size = size
        self.mines = mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.revealed = [[False for _ in range(size)] for _ in range(size)]
        self.flagged = [[False for _ in range(size)] for _ in range(size)]
        self.place_mines()
        self.calculate_numbers()

    def place_mines(self):
        mine_positions = random.sample(range(self.size * self.size), self.mines)
        for pos in mine_positions:
            row, col = divmod(pos, self.size)
            self.board[row][col] = 'M'

    def calculate_numbers(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 'M':
                    continue
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        new_row, new_col = row + dx, col + dy
                        if 0 <= new_row < self.size and 0 <= new_col < self.size:
                            if self.board[new_row][new_col] == 'M':
                                count += 1
                self.board[row][col] = str(count) if count > 0 else ' '

    def reveal_cell(self, row, col):
        """
        Reveal a cell on the Minesweeper board.
        """
        self.revealed[row][col] = True  # Sets the cell as revealed

    def flag_cell(self, row, col):
        """
        Toggle a flag on a cell on the Minesweeper board.
        """
        if not self.revealed[row][col]:  # Check if the cell is not revealed
            self.flagged[row][col] = not self.flagged[row][col]  # This line toggles the flag
            print(f"Flagged status of cell ({row}, {col}): {self.flagged[row][col]}")
