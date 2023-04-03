from tkinter import *
from tkinter.filedialog import *
import tkinter as tk

def saveFile():
    new_file = asksaveasfile(mode = "w", filetype = [("text files", ".txt")])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode = "r", filetype = [("text files", "*.txt")])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)

def clearFile():
    entry.delete(1.0, END)
    
canvas = tk.Tk()
canvas.geometry("600x800")
canvas.title("Not Defteri")
canvas.config(bg = "white")
top = Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = "nw")

button1 = Button(canvas, text = "Aç", bg = "white", command = openFile)
button1.pack(in_ = top, side = LEFT)

button2 = Button(canvas, text = "Kaydet", bg = "white", command = saveFile)
button2.pack(in_ = top, side = LEFT)

button3 = Button(canvas, text = "Yeni", bg = "white", command = clearFile)
button3.pack(in_ = top, side = LEFT)

button4 = Button(canvas, text = "Çıkış", bg = "white", command = exit)
button4.pack(in_ = top, side = LEFT)

entry = Text(canvas, wrap = WORD, bg = "#F9DDA4", font = ("Times New Roman", 15))
entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

canvas.mainloop()