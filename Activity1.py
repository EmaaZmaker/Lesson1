from tkinter import *
window=Tk()
window.geometry("400x300")
window.title("main")
def top_win():
    top=Toplevel()
    top.geometry("180x100")
    top.title("Toplevelwindow")
    label=Label(top,text="this is top level window")
    label.pack()
    top.mainloop()
btn=Button(window,text="click here to open another window",command=top_win)
btn.pack()
window.mainloop()
