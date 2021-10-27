from tkinter import *


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = " "
    text_Input.set(" ")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = " "


cal = Tk()
cal.title("Calculator")
operator = ""

text_Input = StringVar()
textDisplay = Entry(cal, font=("arial", 20, "bold"), textvariable=text_Input, bd=30, insertwidth=4,
                    bg="powder blue", justify="right").grid(columnspan=4)

btn7 = Button(cal, padx=16, bd=8, fg="black", bg="powder blue", command=lambda: btnClick(7), font=("arial", 20, "bold"),
              text="7").grid(row=1,
                             column=0)
btn8 = Button(cal, padx=16, bd=8, fg="black", bg="powder blue", command=lambda: btnClick(8), font=("arial", 20, "bold"),
              text="8").grid(row=1,
                             column=1)
btn9 = Button(cal, padx=16, bd=8, fg="black", bg="powder blue", command=lambda: btnClick(9), font=("arial", 20, "bold"),
              text="9").grid(row=1,
                             column=2)
btnAdd = Button(cal, padx=16, bd=8, fg="black", bg="powder blue", command=lambda: btnClick("+"),
                font=("arial", 20, "bold"), text="+").grid(row=1,
                                                           column=3)
# ======================================================================================================================
btn4 = Button(cal, padx=16, bd=8, fg="black", bg="powder blue", command=lambda: btnClick(4), font=("arial", 20, "bold"),
              text="4").grid(row=2,
                             column=0)
btn5 = Button(cal, padx=16, bd=8, fg="black", bg="powder blue", command=lambda: btnClick(5), font=("arial", 20, "bold"),
              text="5").grid(row=2,
                             column=1)
btn6 = Button(cal, padx=16, bd=8, fg="black", bg="powder blue", command=lambda: btnClick(6), font=("arial", 20, "bold"),
              text="6").grid(row=2,
                             column=2)
btnMin = Button(cal, padx=20, bd=8, fg="black", bg="powder blue", command=lambda: btnClick("-"),
                font=("arial", 20, "bold"), text="-").grid(row=2,
                                                           column=3)
# =======================================================================================================================

btn1 = Button(cal, padx=16, bd=8, fg="black", bg="powder blue", command=lambda: btnClick(1), font=("arial", 20, "bold"),
              text="1").grid(row=3,
                             column=0)
btn2 = Button(cal, padx=16, bd=8, fg="black", bg="powder blue", command=lambda: btnClick(2), font=("arial", 20, "bold"),
              text="2").grid(row=3,
                             column=1)
btn3 = Button(cal, padx=16, bd=8, fg="black", bg="powder blue", command=lambda: btnClick(3), font=("arial", 20, "bold"),
              text="3").grid(row=3,
                             column=2)
btnMul = Button(cal, padx=20, bd=8, fg="black", bg="powder blue", command=lambda: btnClick("/"),
                font=("arial", 20, "bold"), text="/").grid(row=3,
                                                           column=3)
# =======================================================================================================================

btn0 = Button(cal, padx=16, bd=8, fg="black", bg="powder blue", command=lambda: btnClick(0), font=("arial", 20, "bold"),
              text="0").grid(row=4,
                             column=0)
btnDot = Button(cal, padx=20, bd=8, fg="black", bg="powder blue", command=lambda: btnClick("."),
                font=("arial", 20, "bold"), text=".").grid(row=4,
                                                           column=1)
btnEqu = Button(cal, padx=16, bd=8, fg="black", bg="powder blue", font=("arial", 20, "bold"), text="=",
                command=btnEqualsInput).grid(row=4,
                                             column=2)
btnClr = Button(cal, padx=16, bd=8, fg="black", bg="powder blue", font=("arial", 20, "bold"), text="C",
                command=btnClearDisplay).grid(row=4,
                                              column=3)

cal.mainloop()
