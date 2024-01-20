import random

class CrosswordGenerator:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def generate_crossword(self):
        # Place words randomly in the grid
        for word in self.words:
            self.place_word(word)

        # Fill remaining spaces with black squares
        self.fill_black_squares()

        # Display the crossword puzzle
        self.display_grid()

    def place_word(self, word):
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            self.place_horizontal(word)
        elif direction == 'vertical':
            self.place_vertical(word)

    def place_horizontal(self, word):
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, self.cols - len(word))
        for i in range(len(word)):
            self.grid[row][col + i] = word[i]

    def place_vertical(self, word):
        row = random.randint(0, self.rows - len(word))
        col = random.randint(0, self.cols - 1)
        for i in range(len(word)):
            self.grid[row + i][col] = word[i]

    def fill_black_squares(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == ' ' and random.random() < 0.2:
                    self.grid[i][j] = '#'

    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))

# Example Usage
if __name__ == "__main__":
    crossword = CrosswordGenerator(rows=10, cols=10)
    crossword.add_word("PYTHON")
    crossword.add_word("JAVA")
    crossword.add_word("C++")
    crossword.add_word("HTML")
    crossword.generate_crossword()
