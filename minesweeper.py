import random

class Minesweeper:
    def __init__(self, size=2, mines=2):
        self.size = size
        self.mines = mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
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

# Test the Minesweeper class
minesweeper = Minesweeper()
print("Minesweeper board:")
for row in minesweeper.board:
    print(" ".join(row))
