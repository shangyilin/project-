import arena
import blue_bot
import red_bot

board = arena.Arena(7)
blue = blue_bot.BlueBot(0, 0)
red = red_bot.RedBot(board.size - 1, board.size - 1)

for turn in range(50):
    new_blue_cell = blue.pick_move(board)
    new_red_cell = red.pick_move(board)

    # Bots can't move to the same cell or to their opponent's current cell.
    is_occupied = new_blue_cell == red.cell or new_red_cell == blue.cell
    if is_occupied or new_blue_cell == new_red_cell:
        print("Blocked!\n")
        continue

    board.move_bot(blue, new_blue_cell)
    board.move_bot(red, new_red_cell)

    print(board)

print("---GAME OVER---")
print(f"{blue.color} {board.count_cells(blue.color)} cells")
print(f"{red.color} {board.count_cells(red.color)} cells")
