import cell

class Arena:
    """An arena where robots compete to paint the most cells their color."""

    def __init__(self, size):
        self.size = size
        self.blank = "⬜"

        # Fill in the map with all blank cells.
        self._map = []
        for row in range(self.size):
            self._map.append([self.blank] * self.size)

    def get_symbol(self, pos):
        """Returns symbol at the given map Cell, or None if out of bounds."""
        if not self.is_in_bounds(pos):
            return None

        return self._map[pos.row][pos.col]

    def get_valid_moves(self, pos):
        """Returns a list of possible Cells to move to from the given Cell."""
        cells = []

        # Can stay put or move one square up, down, left, right, or diagonal.
        for row_diff in [-1, 0, 1]:
            for col_diff in [-1, 0, 1]:
                new_cell = cell.Cell(pos.row + row_diff, pos.col + col_diff)

                if not self.is_in_bounds(new_cell):
                    continue

                cells.append(new_cell)

        return cells

    def is_in_bounds(self, pos):
        """Returns True if the given Cell is within the bounds of the map."""
        return 0 <= pos.row < self.size and 0 <= pos.col < self.size

    def move_bot(self, bot, new_cell):
        """Paints the bot's current Cell and moves the bot to the new Cell."""
        if new_cell not in self.get_valid_moves(bot.cell):
            return False

        self._map[bot.cell.row][bot.cell.col] = bot.color
        bot.cell = new_cell
        self._map[bot.cell.row][bot.cell.col] = bot.icon
        return True

    def count_cells(self, color):
        """Returns the number of cells painted the given color."""
        count = 0
        for row in range(self.size):
            for col in range(self.size):
                if self._map[row][col] == color:
                    count += 1

        return count

    def __str__(self):
        result = []
        for row in self._map:
            result.append(" ".join(row))

        return "\n".join(result) + "\n"
