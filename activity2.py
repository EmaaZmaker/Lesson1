from tkinter import *
from tkinter import messagebox
from PIL import image,ImageTk
window=Tk()
window.title("demonination calculator")
window.geometry("650x400")
window.configure(bg="light blue")
label1=Label(window,text="hey welcome to... THE DEMONINATION APPLICATION!",bg="light blue")
label1.place(relx=0.5,y=340,anchor=CENTER)
def message():
    msgbox=messagebox.showinfo("Alert","DO you want to calculate THE demonitnation count?")
    if msgbox=="okay":
        top_win()
btn1=Button(window,text="Let's get calculating!",command=message,bg="brown",fg="white")
btn1.place(x=260.y=360)
def top_win():
    top=Toplevel()
    top.title("Demonination Calculator (DC)")
    top.configure(bg="light grey")
    top.geometry("600x450")
    label=Label(top,text="Enter Total Amount",bg="light grey")
    entry=Entry(top)
    lbl=Label(top,text="Here are the numbers for each demonination!",bg="light grey")
    L1=Label(top,text="2000",bg="light grey")
    L2=Label(top,text="500",bg="light grey")
    L3=Label(top,text="100",bg="light grey")
    T1=Entry(top)
    T2=Entry(top)
    T3=Entry(top)