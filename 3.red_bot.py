import cell
import random

class RedBot:
    """A robot that moves through an arena and paints its trail red."""

    def __init__(self, row, col):
        self.cell = cell.Cell(row, col)
        self.color = "🟥"
        self.icon = "🤖"

    def pick_move(self, arena):
        """Returns a proposed Cell to move to on this turn."""
        return random.choice(arena.get_valid_moves(self.cell))
