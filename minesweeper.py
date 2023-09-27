import random

class Minesweeper:
    def __init__(self, size, mines):
        self.size = size
        self.mines = mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.revealed = [[False for _ in range(size)] for _ in range(size)]
        self.flagged = [[False for _ in range(size)] for _ in range(size)]
        self.first_click = True
        self.game_over = False

    def place_mines(self, exclude_row, exclude_col):
        mine_positions = random.sample(range(self.size * self.size), self.mines)
        for pos in mine_positions:
            row, col = divmod(pos, self.size)
            if row == exclude_row and col == exclude_col:
                continue
            self.board[row][col] = 'M'

    def check_win(self):
        for row in range(self.size):
            for col in range(self.size):
                if not self.revealed[row][col] and self.board[row][col] != 'M':
                    return False
        return True


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

    def debug_output(self):
        print("Board:")
        for row in self.board:
            print(row)
        print("Revealed:")
        for row in self.revealed:
            print(row)
        print("Flagged:")
        for row in self.flagged:
            print(row)

    def reveal_cell(self, row, col):
        if self.first_click:
            self.place_mines(row, col)  # Place mines, excluding the first clicked cell
            self.calculate_numbers()
            self.first_click = False  # Set first_click to False

        if self.game_over:
            return

        if self.revealed[row][col]:
            return

        self.revealed[row][col] = True  # Set the cell as revealed

        if self.board[row][col] == 'M':
            self.game_over = True  # Game is over if a mine is revealed
            return

        if self.board[row][col] == ' ':
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_row, new_col = row + dx, col + dy
                    if 0 <= new_row < self.size and 0 <= new_col < self.size:
                        if not self.revealed[new_row][new_col]:
                            self.reveal_cell(new_row, new_col)

    def flag_cell(self, row, col):
        print("Before flag_cell:")
        self.debug_output()

        if not self.revealed[row][col]:
            self.flagged[row][col] = not self.flagged[row][col]

        print("After flag_cell:")
        self.debug_output()