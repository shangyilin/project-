import cell

class BlueBot:
    def __init__(self, row, col):
        self.cell = cell.Cell(row, col)
        self.color = "🔵"
        self.icon = "🤖"

    def pick_move(self, arena):
        moves = arena.get_valid_moves(self.cell)

        best = self.cell
        best_score = -10**9

        for m in moves:
            score = 0

            if m != self.cell:
                score += 5
            else:
                score -= 3

            sym = arena.get_symbol(m)
            if sym == arena.blank:
                score += 2
            elif sym == self.color:
                score -= 1
            elif sym == "🟥":
                score -= 2

            mobility = len(arena.get_valid_moves(m))
            score += 0.3 * mobility

            if score > best_score:
                best_score = score
                best = m

        return best
