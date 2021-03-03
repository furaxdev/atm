from tkinter import *
from tkinter import ttk
import tkinter.messagebox

root = Tk()

root.title("ATM SYSTEM")
root.geometry("840x760+280+0")
root.configure(bg="red")


def btnarr4cmd():
    btnArrowL1['state']='normal'
    return

# ============================Frames===============================


user_id = None


MainFrame = Frame(root, bd=20, width=774,
                  height=700, relief=RIDGE, background="#ee0000")
MainFrame.grid()

TopFrame1 = Frame(MainFrame, bd=7, width=734,
                  height=300, relief=RIDGE, background="#ee0000")
TopFrame1.grid(row=1, column=0, padx=12)

TopFrame2 = Frame(MainFrame, bd=7, width=734,
                  height=300, relief=RIDGE, background="#ee0000")
TopFrame2.grid(row=0, column=0, padx=12)

TopFrame2Left = Frame(TopFrame2, bd=5, width=190,
                      height=300, relief=RIDGE)
TopFrame2Left.grid(row=0, column=0, padx=12)

TopFrame2Mid = Frame(TopFrame2, bd=5, width=200,
                     height=300, relief=RIDGE)
TopFrame2Mid.grid(row=0, column=1, padx=12)

TopFrame2Right = Frame(TopFrame2, bd=5, width=190,
                       height=300, relief=RIDGE)
TopFrame2Right.grid(row=0, column=2, padx=12)

# =======================WIDGETS=====================

Midlabel1 = Label(TopFrame2Mid, text="FINGERPRINT ATM MACHINE", width=40)
Midlabel1.grid(row=0, column=0, columnspan=4)

Midlabel2 = Label(TopFrame2Mid, text="  ", width=40,)
Midlabel2.grid(row=1, column=0, columnspan=4)

Midlabel3 = Label(TopFrame2Mid, text="  ", width=40,)
Midlabel3.grid(row=2, column=0, columnspan=4)

Midlabel4 = Label(TopFrame2Mid, text="  ", width=40,)
Midlabel4.grid(row=3, column=0, columnspan=4)

Leftbutton1label = Label(
    TopFrame2Mid, text="Enter Fingerprint", width=40, height=3, anchor='w')
Leftbutton1label.grid(row=4, column=0, columnspan=2)


Leftbutton2label = Label(
    TopFrame2Mid, text="Enter Fingerprint", width=40, height=3, anchor='w')
Leftbutton2label.grid(row=5, column=0, columnspan=2)

Leftbutton3label = Label(
    TopFrame2Mid, text="Enter Fingerprint", width=40, height=3, anchor='w')
Leftbutton3label.grid(row=6, column=0, columnspan=2)

Leftbutton4label = Label(
    TopFrame2Mid, text="Enter Fingerprint", width=40, height=3, anchor='w')
Leftbutton4label.grid(row=7, column=0, columnspan=2)

Midlabel5 = Label(TopFrame2Mid, text="   ", width=40,)
Midlabel5.grid(row=8, column=0, columnspan=4)

Midlabel6 = Label(TopFrame2Mid, text="  ", width=40)
Midlabel6.grid(row=9, column=0, columnspan=4)

Midlabel7 = Label(TopFrame2Mid, text="  ", width=40)
Midlabel7.grid(row=10, column=0, columnspan=4)

Midlabel8 = Label(TopFrame2Mid, text="  ", width=40)
Midlabel8.grid(row=11, column=0, columnspan=4)

# =================LEFT BUTTONS =============================
img_arrow_Left = PhotoImage(file="lArrow.png")

btnArrowL1 = Button(TopFrame2Left, width=120, height=30,
                    state=DISABLED, image=img_arrow_Left)
btnArrowL1.grid(row=0, column=0, padx=2, pady=4)

btnArrowL2 = Button(TopFrame2Left, width=120, height=30,
                    state=DISABLED, image=img_arrow_Left)
btnArrowL2.grid(row=1, column=0, padx=2, pady=4)

btnArrowL3 = Button(TopFrame2Left, width=120, height=30,
                    state=DISABLED, image=img_arrow_Left)
btnArrowL3.grid(row=2, column=0, padx=2, pady=4)

btnArrowL4 = Button(TopFrame2Left, width=120, height=30,
                    state=DISABLED, image=img_arrow_Left)
btnArrowL4.grid(row=3, column=0, padx=2, pady=4)

# =================RIGHT BUTTONS =============================


img_arrow_Right = PhotoImage(file="rArrow.png")

btnArrowR1 = Button(TopFrame2Right, width=120, height=30,
                    state=DISABLED, image=img_arrow_Right)
btnArrowR1.grid(row=0, column=0, padx=2, pady=4)

btnArrowR2 = Button(TopFrame2Right, width=120, height=30,
                    state=DISABLED, image=img_arrow_Right)
btnArrowR2.grid(row=1, column=0, padx=2, pady=4)

btnArrowR3 = Button(TopFrame2Right, width=120, height=30,
                    state=DISABLED, image=img_arrow_Right)
btnArrowR3.grid(row=2, column=0, padx=2, pady=4)

btnArrowR4 = Button(TopFrame2Right, width=120, height=30,
                    command=btnarr4cmd, image=img_arrow_Right)
btnArrowR4.grid(row=3, column=0, padx=2, pady=4)

# ========================================PIN BUTTONS==================================


root.mainloop()
