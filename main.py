from tkinter import *

root = Tk()
root.geometry("400x400")

Label(root, text="your first number:").grid(row=0, column=0)
Label(root, text="your second number:").grid(row=1, column=0)

label3 = Label(root)

label3.grid(row=3, column=1)

first_no = IntVar()
second_no = IntVar()


entry1 = Entry(root, textvariable=first_no).grid(row=0, column=1)
entry2 = Entry(root, textvariable=second_no).grid(row=1, column=1)


def add():
    sumation = first_no.get() + second_no.get()
    label3.config(text="your final number is:" + str(sumation))

mybutton = Button(root, text=("Calculate!"), command=add).grid(row=2, column=1)

root.mainloop()