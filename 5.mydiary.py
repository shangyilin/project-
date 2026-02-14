import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *

root = Tk()
root.title('Diary Notebook')
root.geometry('320x400')

# Insert line
def insert_line():
    text_area.insert(INSERT, '\n' + 42 * '-')

# Insert hearts
def insert_hearts():
    text_area.insert(INSERT, '\n' + 29 * '♥')

scrollbar = Scrollbar(root)  # Scrollbar
text_area = Text(root, width=42, height=20)  # Multi-line text box
btn_line = Button(root, text='Insert Line', width=10, command=insert_line)
btn_hearts = Button(root, text='Insert Hearts', width=10, command=insert_hearts)

text_area.place(x=0, y=0)
scrollbar.place(x=300, height=270)
btn_line.place(x=60, y=300)
btn_hearts.place(x=170, y=300)

scrollbar.config(command=text_area.yview)
text_area.config(yscrollcommand=scrollbar.set)


# ------------------ Menu ------------------

def open_file():
    global filename
    filename = askopenfilename(defaultextension='.txt')
    if filename == '':
        filename = None
    else:
        text_area.delete(1.0, END)
        file_obj = open(filename, 'r')
        text_area.insert(1.0, file_obj.read())
        file_obj.close()
        root.title('Diary Notebook: ' + os.path.basename(filename))

def save_file():
    global filename
    try:
        file_obj = open(filename, 'w')
        content = text_area.get(1.0, END)
        file_obj.write(content)
        file_obj.close()
        messagebox.showinfo('Notice', 'Saved successfully!')
    except:
        save_as()

def save_as():
    global filename
    f = asksaveasfilename(initialfile='Untitled.txt',
                          defaultextension='.txt')
    if f != '':
        filename = f
        file_obj = open(f, 'w')
        content = text_area.get(1.0, END)
        file_obj.write(content)
        file_obj.close()
        messagebox.showinfo('Notice', 'Saved successfully!')
        root.title('Diary Notebook: ' + os.path.basename(filename))


# Create menu
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Close')
menu_bar.add_cascade(label='File', menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About')
help_menu.add_command(label='Author')
menu_bar.add_cascade(label='Help', menu=help_menu)

root.config(menu=menu_bar)

root.mainloop()
