import tkinter as tk
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Калькулятор площади треугольника")
window.geometry("500x450")
window.mainloop()

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)
frame.pack(fill=Y)
method_lbl = Label(
   frame,
   text="Выберите способ расчета площади"
)
method_lbl.grid(row=1, column=1)