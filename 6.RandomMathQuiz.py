from turtle import *
from random import *

pd()
clear()

a = randint(1, 100)
b = randint(1, 100)

c = ['+', '×']
d = c[randint(0, 1)]

question = f"{a} {d} {b} = ?"
text = textinput("Hint", question)
text = int(text)

if d == c[0]:
    A = a + b
    if text == A:
        write("Yes, you are right!", font=("Times New Roman", 25, "normal"))
    else:
        write("Sorry, you are wrong.", font=("Times New Roman", 25, "normal"))
    print(A)
    print(text)
else:
    B = a * b
    if text == B:
        write("Yes, you are right!", font=("Times New Roman", 25, "normal"))
    else:
        write("Sorry, you are wrong.", font=("Times New Roman", 25, "normal"))
    print(B)
    print(text)

done()