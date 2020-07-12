from tkinter import *
import sys

def command1(event):
    if entry1.get() =='admin' and entry2.get() =='9837':
        root.deiconify()
        top.destroy()

def command2():
    top.destroy()
    root.destroy()
    sys.exit()

root= Tk()
top= Toplevel()

top.geometry('380x260')
top.title('Login Screen')
top.configure(background='white')
lbl1=Label(top,text='Username:',font=('Helvetica',10))
entry1=Entry(top)
lbl2=Label(top,text='Password', font=('Helvetica',10))
entry2=Entry(top,show="*")
button2=Button(top,text='Cancel',command=lambda:command2())

entry2.bind('<Return>',command1)

lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
button2.pack()


root.title("Main Screen")
root.configure(background='white')
root.geometry('855x650')        

root.withdraw()
root.mainloop()