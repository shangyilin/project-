from tkinter import *  # Pinball game canvas
import random
import time


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)

        self.canvas.move(self.id, 245, 100)

        # Randomize the initial speed
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

        # Cache canvas size for wall collision checks
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    # Reset ball position/speed so the game can be played again
    def reset(self):
        self.canvas.coords(self.id, 245, 100, 260, 115)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    # Check if the ball hits the paddle
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                return True
        return False

    # Move the ball and see if it bounces
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        if self.hit_paddle(pos) == True:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    # Reset paddle for replay
    def reset(self):
        self.canvas.coords(self.id, 200, 300, 300, 310)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

    # Update paddle position
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        # Stop moving if the paddle reaches the left/right boundary
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    # Set paddle speed
    def turn_left(self, evt):
        self.x = -5

    def turn_right(self, evt):
        self.x = 5

class setup:
    def setup_game(self):
        self.text = self.canvas.create_text(
            260, 200,
            text='Click left mouse button to start the game',
            font=('Helvetica', 36)
        )
        self.canvas.bind('<Button-1>', lambda start_game: self.start_game())


# Main program
tk = Tk()
tk.title("Pinball Game")
tk.resizable(False,False)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'green')
ball = Ball(canvas, paddle, 'yellow')

canvas.create_text(10, 10, anchor="nw", text="Use the arrow keys (↑ ↓ ← →) to move.", font=("Helvetica", 14))

game_over_text_id = None
can_restart = False

# Restart game when user clicks left mouse button
def restart_game(event=None):
    global game_over_text_id, can_restart
    if can_restart:
        if game_over_text_id is not None:
            canvas.delete(game_over_text_id)
            game_over_text_id = None

        # Reset paddle and ball to replay
        paddle.reset()
        ball.reset()


# restart function
canvas.bind('<Button-1>', restart_game)

# Main game loop
while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        # When game ends, display notification and restart
        if game_over_text_id is None:
            game_over_text_id = canvas.create_text(
                250, 200,
                text="Game Over\nClick left mouse button to play again",
                font=('Helvetica', 24)
            )
            can_restart = True

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
