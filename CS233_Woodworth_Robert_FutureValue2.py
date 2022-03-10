#!/usr/bin/env python3
# Rob Woodworth CS223 Future Value 1/19/22
from tkinter import *
root = Tk()
root.title("RobBank Future Values")
root.geometry("300x420")

Label(root, text="\nWelcome to RobBank").pack()
Label(root, text="Number of years to invest for:").place(x=35, y=80)
yearsBox = Entry(root)
yearsBox.place(x=55, y=105, width=50)
Label(root, text="Monthly investment amount:").place(x=35, y=125)
monthBox = Entry(root)
monthBox.place(x=55, y=150, width=50)
Label(root, text="Future Value Amount:").place(x=35, y=175)

lbl1 = Label(root, text="")
lbl1.place(x=35, y=200)
lbl2 = Label(root, text="")
lbl2.place(x=35, y=220)


def compute():
    interest = 1.00791667 ** int(int(yearsBox.get()) * 12)
    value = float(monthBox.get()) * float(interest) * 72
    lbl1["text"] = f"In the year {2022 + int(yearsBox.get())},"
    lbl2["text"] = f"your investment will be worth ${value:,.2f}"


def clear():
    yearsBox.delete(0, END)
    monthBox.delete(0, END)
    lbl1['text'] = ""
    lbl2['text'] = ""


def convert():
    lbl3["text"] = f"Monthly interest is 0.791%"


Button(root, width=9, text="Calculate", command=compute).place(x=25, y=265)
Button(root, width=9, text="Clear", command=clear).place(x=110, y=265)
Button(root, width=9, text="Exit", command=quit).place(x=200, y=265)
Label(root, text="Yearly interest rate is 9.5%").place(x=75, y=325)
Button(root, width=19, text="Convert to monthly",
       command=convert).place(x=65, y=350)
lbl3 = Label(root, text="")
lbl3.place(x=75, y=380)

root.mainloop()
