class Cell:
    """A position on a map identified by its row and column."""

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return False

        return self.row == other.row and self.col == other.col

    def __str__(self):
        return f"({self.row}, {self.col})"
