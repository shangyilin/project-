from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Taylor Swift Login")
root.geometry("300x200")

BG = "misty rose"
ACCENT = "purple"

root.configure(bg=BG)

num = 0
username = "Taylor Swift"
password = "19891213"

v1 = StringVar()
v1.set("Attempts: " + str(num))

lab0 = Label(root, textvariable=v1, font=("Arial", 10), fg="black", bg=BG)
lab0.place(x=210, y=5)

lab1 = Label(root, text="Username:", font=("Arial", 10), fg="black", bg=BG)
lab1.place(x=60, y=60)

lab2 = Label(root, text="Password:", font=("Arial", 10), fg="black", bg=BG)
lab2.place(x=60, y=100)

e1 = Entry(root, width=15, bg="white")
e2 = Entry(root, show="*", width=15, bg="white")
e1.place(x=120, y=60)
e2.place(x=120, y=100)

def login():
    lab0.destroy()
    lab1.destroy()
    lab2.destroy()
    e1.destroy()
    e2.destroy()
    b1.destroy()
    b2.destroy()

    lab3 = Label(root, text="✨ Welcome to Taylor’s World ✨", font=("Arial", 13), fg=ACCENT, bg=BG)
    lab3.place(x=25, y=80)

def b1fun():
    global num
    if e1.get() == username and e2.get() == password:
        messagebox.showinfo("Notice", "Login successful!")
        login()
    else:
        messagebox.showerror("Error", "Incorrect username or password!")
        num += 1
        v1.set("Attempts: " + str(num))

def b2fun():
    e1.delete(0, "end")
    e2.delete(0, "end")
    e1.focus()

b1 = Button(root, text="OK", font=("Arial", 10), width=5, height=1, command=b1fun, bg="plum")
b1.place(x=100, y=140)

b2 = Button(root, text="Reset", font=("Arial", 10), width=5, height=1, command=b2fun)
b2.place(x=160, y=140)

root.mainloop()
