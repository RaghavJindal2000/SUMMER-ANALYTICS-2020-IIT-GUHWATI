from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk


class Win1:
    __bookname = ""
    __pricebook = ""


    def setbook(self,book):
        self.__bookname=book

    def setprice(self,pprice):
        self.__pricebook=pprice

    def checkname(self,book):
        if self.__bookname==book:
            return True
        return False


llistbook = [["little girl", "$29.99"],
             ["Blue Sky", "$49.99"],
             ["White", "$19.99"]]
row=[]

def bookadd(llistbook,name,pr):
    bb=Win1()
    bb.setbook(name)
    bb.setprice(pr)
    row.append(bb)
    llistbook.append(row)



def addbook():
    bookadd(llistbook,bookname.get(),price.get())
    bookname.delete('0', 'end')
    price.delete('0', 'end')


def deletebook():
        c = tree1.selection()
        tree1.delete(c)


def editbook():
    c = tree1.selection()
    values1 = tuple(tree1.item(c)['values'])
    bookname.insert('end', values1[0])
    price.insert('end', values1[1])

def showinfoadmin():
    def back():
        window01.destroy()


    window01 = Tk()
    c = tree1.selection()
    valuesadmin = tuple(tree1.item(c)['values'])
    T = Text(window01, height=20, width=45)
    T.pack()
    T.insert(END, "{0}\nPrice: {1}\n".format(valuesadmin[0],valuesadmin[1]))

    backb = Button(window01, text="Back", command=back)
    backb.pack()


    window01.mainloop()

window1 = Tk()
window1.geometry('800x600')
window1.title("Admin")
tree1 = Treeview(window1, show="headings")
tree1["columns"] = ("one", "two", "three")
tree1.column("one", width=150)
tree1.column("two", width=90)
tree1.column("three", width=40)
tree1.heading("one", text="Book Name")
tree1.heading("two", text="Price")

for item in llistbook:
    tree1.insert('', 'end', values=item)

tree1.pack(padx=5, pady=10, side=LEFT)
B1admin = Button(window1, text="Information", command=showinfoadmin)
B1admin.place(x = 00,y = 10)

bottdel = Button(window1,text = "Delete Book",command =deletebook)
bottdel .place(x = 00,y = 40)

bottedit = Button(window1,text = "Edit Book",command =editbook)
bottedit .place(x = 00,y =70)


# bottadminlogin = Button(window1,text = "ADMINLOGIN",command =Win2)
# bottadminlogin .place(x=70,y=70)

lblbook =Label(window1, text="Book Name")
lblbook.place(x = 440,y = 130)
bookname = Entry(window1, width=20)
bookname.place(x = 440,y = 150)

lblprice = Label(window1, text="price")
lblprice.place(x = 440,y = 180)
price = Entry(window1, width=20)
price.place(x = 440,y = 200)


bottadd = Button(window1,text = "Add Book",command =addbook)
bottadd .place(x = 440,y = 470)

window1.mainloop()

# class Win2: 

#     def command1(event):
#         if entry1.get() =='admin' and entry2.get() =='9837':
#             root.deiconify()
#             top.destroy()

#     def command2():
#         top.destroy()
#         root.destroy()
#         sys.exit()

# root= Tk()
# top= Toplevel()

# top.geometry('380x260')
# top.title('Login Screen')
# top.configure(background='white')
# lbl1=Label(top,text='Username:',font=('Helvetica',10))
# entry1=Entry(top)
# lbl2=Label(top,text='Password', font=('Helvetica',10))
# entry2=Entry(top,show="*")
# button2=Button(top,text='Cancel',command=lambda:command2())

# entry2.bind('<Return>',command1)

# lbl1.pack()
# entry1.pack()
# lbl2.pack()
# entry2.pack()
# button2.pack()


# root.title("Login Screen")
# root.configure(background='white')
# root.geometry('855x650')

# root.withdraw()
# root.mainloop()