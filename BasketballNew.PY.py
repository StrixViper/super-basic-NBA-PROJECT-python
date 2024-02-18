from ast import Delete
from ipaddress import collapse_addresses
import math
from tkinter import *
from tkinter.tix import COLUMN

root =  Tk()
root.title("Noam Calculator")



title_label = Label(root, text="Noam Calculator ", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

search = Entry(root, width=35, borderwidth=5, )
search.grid(row=1, column=0, columnspan=5, padx=10, pady=20)


#search.insert(0, "") 



#function that take the number and inseert into the input box
def button_click(number):

   current = search.get()
   search.delete(0, END)  #delete what's in the box
   search.insert(0, str(current) + str(number))   #add the current and the new one as a string

def button_clear():
    search.delete(0, END)


def button_add():
    first_number = search.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    search.delete(0, END)


def button_equal():
    second_number = search.get()
    search.delete(0, END) 


    if math=="addition":
      search.insert(0, f_num + int(second_number))

    if math=="minus":
      search.insert(0, f_num - int(second_number))

    if math=="multiplication":
      search.insert(0, f_num * int(second_number))

    if math=="division":
      search.insert(0, f_num / int(second_number))


def button_minus():
    first_number = search.get()
    global f_num
    global math
    math = "minus"
    f_num = int(first_number)
    search.delete(0, END)

def button_mul():
    first_number = search.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    search.delete(0, END)

def button_div():
    first_number = search.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    search.delete(0, END)


    #hover functions
def button_hover0(e):
    button_0["bg"] = "skyblue"
def button_hover1(e):
    button_1["bg"] = "skyblue"
def button_hover2(e):
    button_2["bg"] = "skyblue"
def button_hover3(e):
    button_3["bg"] = "skyblue"
def button_hover4(e):
    button_4["bg"] = "skyblue"
def button_hover5(e):
    button_5["bg"] = "skyblue"
def button_hover6(e):
    button_6["bg"] = "skyblue"
def button_hover7(e):
    button_7["bg"] = "skyblue"
def button_hover8(e):
    button_8["bg"] = "skyblue"
def button_hover9(e):
    button_9["bg"] = "skyblue"
def button_hover_add(e):
    button_add["bg"] = "skyblue"
def button_hover1_equal(e):
    button_equal["bg"] = "skyblue"
def button_hover_clear(e):
    button_clear["bg"] = "skyblue"
def button_hover_minus(e):
    button_minus["bg"] = "skyblue"
def button_hover_mul(e):
    button_mul["bg"] = "skyblue"
def button_hover_div(e):
    button_div["bg"] = "skyblue"







    #hover functions
def button_leave0(e):
    button_0["bg"] = "SystemButtonFace"
def button_leave1(e):
    button_1["bg"] = "SystemButtonFace"
def button_leave2(e):
    button_2["bg"] = "SystemButtonFace"
def button_leave3(e):
    button_3["bg"] = "SystemButtonFace"
def button_leave4(e):
    button_4["bg"] = "SystemButtonFace"
def button_leave5(e):
    button_5["bg"] = "SystemButtonFace"
def button_leave6(e):
    button_6["bg"] = "SystemButtonFace"
def button_leave7(e):
    button_7["bg"] = "SystemButtonFace"
def button_leave8(e):
    button_8["bg"] = "SystemButtonFace"
def button_leave9(e):
    button_9["bg"] = "SystemButtonFace"
def button_leave_add(e):
    button_add["bg"] = "SystemButtonFace"
def button_leave_equal(e):
    button_equal["bg"] = "SystemButtonFace"
def button_leave_clear(e):
    button_clear["bg"] = "SystemButtonFace"
def button_leave_minus(e):
    button_minus["bg"] = "SystemButtonFace"
def button_leave_mul(e):
    button_mul["bg"] = "SystemButtonFace"
def button_leave_div(e):
    button_div["bg"] = "SystemButtonFace"





#define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))


button_add = Button(root, text="+", padx=39, pady=53, command=button_add)
button_equal = Button(root, text="=", padx=135, pady=20, command=button_equal)
button_clear = Button(root, text="C", padx=87, pady=20, command=button_clear)
button_minus = Button(root, text="-", padx=40, pady=20, command=button_minus)
button_mul = Button(root, text="X", padx=40, pady=20, command=button_mul)
button_div = Button(root, text=":", padx=40, pady=20, command=button_div)



#put the buttons on the screen

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)

button_0.grid(row=5,column=0)


button_add.grid(row=5, column=3, rowspan=2)
button_equal.grid(row=6, column=0,columnspan=3)
button_clear.grid(row=5, column=1, columnspan=2)
button_minus.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)


button_0.bind("<Enter>", button_hover0)
button_0.bind("<Leave>", button_leave0)

button_1.bind("<Enter>", button_hover1)
button_1.bind("<Leave>", button_leave1)

button_2.bind("<Enter>", button_hover2)
button_2.bind("<Leave>", button_leave2)

button_3.bind("<Enter>", button_hover3)
button_3.bind("<Leave>", button_leave3)

button_4.bind("<Enter>", button_hover4)
button_4.bind("<Leave>", button_leave4)

button_5.bind("<Enter>", button_hover5)
button_5.bind("<Leave>", button_leave5)

button_6.bind("<Enter>", button_hover6)
button_6.bind("<Leave>", button_leave6)

button_7.bind("<Enter>", button_hover7)
button_7.bind("<Leave>", button_leave7)

button_8.bind("<Enter>", button_hover8)
button_8.bind("<Leave>", button_leave8)

button_9.bind("<Enter>", button_hover9)
button_9.bind("<Leave>", button_leave9)

button_add.bind("<Enter>", button_hover_add)
button_add.bind("<Leave>", button_leave_add)

button_minus.bind("<Enter>", button_hover_minus)
button_minus.bind("<Leave>", button_leave_minus)

button_mul.bind("<Enter>", button_hover_mul)
button_mul.bind("<Leave>", button_leave_mul)

button_div.bind("<Enter>", button_hover_div)
button_div.bind("<Leave>", button_leave_div)

button_equal.bind("<Enter>", button_hover1_equal)
button_equal.bind("<Leave>", button_leave_equal)

button_clear.bind("<Enter>", button_hover_clear)
button_clear.bind("<Leave>", button_leave_clear)


root.mainloop()