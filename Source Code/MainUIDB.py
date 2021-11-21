from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

import DatabaseMain

#USERNAME AND PASSWORD OF DIRECTOR
default_name = ("director")       #USER FIELD
default_pass = ("123")            #PASSWORD FIELD

#WINDOW OBJECTS
root = Tk()
loginWindow = Toplevel(root)
root.withdraw()

#ATTRIBUTE FIELDS
ID = StringVar()
NAME = StringVar()
DESCRIPTION = StringVar()
UNIT = StringVar()
QUANTITY = StringVar()
DATE = StringVar()

def login():
    loginWindow.title("Login Prompt")
    nameLabel = Label(loginWindow, text='name: ', width = 10)
    passLabel = Label(loginWindow, text='password: ', width = 10)
    nameField = Entry(loginWindow, width = 50)
    passField = Entry(loginWindow, show ='*', width = 50)
    loginButt = Button(loginWindow, text="LOGIN", width=49, command = lambda:loginButton(loginWindow, nameField, passField))
    nameLabel.pack(padx = 0, pady = 0)
    nameField.pack(padx = 0, pady = 0)
    passLabel.pack(padx = 0, pady = 0)
    passField.pack(padx = 0, pady = 0)
    loginButt.pack(padx = 0, pady = 0)

    loginButt.focus_set()
    loginWindow.resizable(False, False)
    loginWindow.iconbitmap('cogwheel.ico')
    loginWindow.protocol("WM_DELETE_WINDOW", on_closing)

def on_closing():
    choice = messagebox.askquestion("QUIT PROGRAM", "ARE YOU SURE?")
    if choice == 'yes':
        loginWindow.destroy()
        root.destroy()
    else:
        pass


def loginButton(window, nameField, passField):
    if nameField.get() == default_name and passField.get() == default_pass:
        messagebox.showinfo("LOGIN", "WELCOME DIRECTOR!!!")
        window.destroy()
        root.deiconify()
    else:
        messagebox.showwarning("WRONG INPUT", "WRONG USERNAME OR PASSWORD")

login()

#LAYOUT FOR TITLE AND BUTTONS
mainFrame = Frame(root, bg='powderblue')
titleFrame = Frame(mainFrame)
buttonFrame = Frame(mainFrame)
bottomFrame = Frame(mainFrame)
mainFrame.pack()
titleFrame.pack(side=TOP)
buttonFrame.pack(side=TOP)
bottomFrame.pack(side=BOTTOM)

img = PhotoImage(file="companyimage.png")
imageLabel = Label(titleFrame, image = img, bg = 'black')
imageLabel.pack()

#BUTTONS FOR PROGRAMS
insertButt = Button(buttonFrame, text = 'ADD new record(s)', width = 100, bd=5, command = lambda:add_records())
updateButt = Button(buttonFrame, text = 'UPDATE from existing record(s)', width = 100, bd=5, command = lambda:update_records())
deleteButt = Button(buttonFrame, text = 'DELETE from existing record(s)', width = 100, bd=5, command = lambda:delete_records())
viewButt = Button(buttonFrame, text = 'VIEW existing record(s)', width = 100, bd=5, command = lambda:view_records())
insertButt.pack()
updateButt.pack()
deleteButt.pack()
viewButt.pack()

saveButt = Button(buttonFrame, text = "SAVE", width = 50, command = lambda:save_window())
exitButt = Button(buttonFrame, text = 'EXIT', width = 50, command = lambda:exit_window())
saveButt.pack(side=LEFT)
exitButt.pack(side=RIGHT)


#COMMANDS FOR BUTTONS

#===============================ADD=========================================
def add_records():
    #Main Window, Labels and Entry Fields
    main = Toplevel(root)
    idnum = Entry(main, textvariable = ID)
    name = Entry(main, textvariable = NAME)
    desc = Entry(main, textvariable = DESCRIPTION)
    unit = Entry(main, textvariable = UNIT)
    quantity = Entry(main, textvariable = QUANTITY)
    date = Entry(main, textvariable = DATE)

    #Button For Adding Records
    add = Button(main, text='ADD RECORD', command = lambda:insertrecord(main))

    #LABEL NAMES
    lbl1 = Label(main, text = 'ID: ')
    lbl2 = Label(main, text = 'NAME: ')
    lbl3 = Label(main, text='DESCRIPTION: ')
    lbl4 = Label(main, text='UNIT: ')
    lbl5 = Label(main, text='QUANTITY: ')
    lbl6 = Label(main, text='DATE: ')

    idnum.grid(row=0, column=1)
    lbl1.grid(row=0, column=0)
    name.grid(row=1, column=1)
    lbl2.grid(row=1, column=0)
    desc.grid(row=2, column=1)
    lbl3.grid(row=2, column=0)
    unit.grid(row=3, column=1)
    lbl4.grid(row=3, column=0)
    quantity.grid(row=4, column=1)
    lbl5.grid(row=4, column=0)
    date.grid(row=5, column=1)
    lbl6.grid(row=5, column=0)
    add.grid(row=6, column=1)

    main.title("ADD RECORDS")
    falseResizable(main)
    main.grab_set()
    setIcon(main)

def insertrecord(main):
    items = (ID.get(), NAME.get(), DESCRIPTION.get(), UNIT.get(), QUANTITY.get(), DATE.get())
    DatabaseMain.insert_table(items)
    clearfields()
    main.destroy()

#===============================UPDATE=========================================
def update_records():
    # Main Window, Labels and Entry Fields
    main = Toplevel(root)
    idnum = Entry(main, textvariable=ID)
    name = Entry(main, textvariable=NAME)
    desc = Entry(main, textvariable=DESCRIPTION)
    unit = Entry(main, textvariable=UNIT)
    quantity = Entry(main, textvariable=QUANTITY)
    date = Entry(main, textvariable=DATE)

    # Button For Adding Records
    add = Button(main, text='UPDATE', command=lambda: updaterecord(main))

    # LABEL NAMES
    lbl1 = Label(main, text='ID to be changed: ')
    lbl2 = Label(main, text='NEW NAME: ')
    lbl3 = Label(main, text='NEW DESCRIPTION: ')
    lbl4 = Label(main, text='NEW UNIT: ')
    lbl5 = Label(main, text='NEW QUANTITY: ')
    lbl6 = Label(main, text='NEW DATE: ')

    idnum.grid(row=0, column=1)
    lbl1.grid(row=0, column=0)
    name.grid(row=1, column=1)
    lbl2.grid(row=1, column=0)
    desc.grid(row=2, column=1)
    lbl3.grid(row=2, column=0)
    unit.grid(row=3, column=1)
    lbl4.grid(row=3, column=0)
    quantity.grid(row=4, column=1)
    lbl5.grid(row=4, column=0)
    date.grid(row=5, column=1)
    lbl6.grid(row=5, column=0)
    add.grid(row=6, column=1)

    main.title("UPDATE RECORDS")
    falseResizable(main)
    main.grab_set()
    setIcon(main)

def updaterecord(main):
    items = (NAME.get(), DESCRIPTION.get(), UNIT.get(), QUANTITY.get(), DATE.get(), ID.get())
    DatabaseMain.selectkey_table_upd(ID.get(), items)
    clearfields()
    main.destroy()

#===============================DELETE=========================================
def delete_records():
    main = Toplevel(root)
    idnum = Entry(main, textvariable=ID)
    lbl1 = Label(main, text='Value of ID to be deleted: ')
    add = Button(main, text='DELETE', command=lambda: delrecord(main))

    lbl1.grid(row=0, column=0)
    idnum.grid(row=0, column=1)
    add.grid(row=1, column=1)

    main.title("DELETION OPERATION")
    falseResizable(main)
    main.grab_set()
    setIcon(main)

def delrecord(main):
    DatabaseMain.selectkey_table_del(ID.get())
    clearfields()
    main.destroy()

#===============================VIEW=========================================
def view_records():
    main = Toplevel(root, bg='gray')
    tv = Treeview(main, columns=(1, 2, 3, 4, 5, 6), show="headings", height = 5)
    rows = DatabaseMain.get_table()

    tv.heading(1, text = "ID")
    tv.heading(2, text = "ITEM NAME")
    tv.heading(3, text = "ITEM DESCRIPTION")
    tv.heading(4, text="ITEM UNIT")
    tv.heading(5, text="ITEM QUANTITY")
    tv.heading(6, text="DATE CREATED")

    for row in rows:
        tv.insert('', 'end', values = row)

    tv.pack()

    main.title("INVENTORY LIST")
    main.grab_set()
    setIcon(main)

def destroy_window():
    pass

def exit_window():
    root.destroy()

def save_window():
    choice = messagebox.askquestion("WARNING", "ARE YOU SURE?")
    if choice == 'yes':
        DatabaseMain.con.commit()

def falseResizable(window):
    window.resizable(False, False)

def setIcon(window):
    window.iconbitmap("cogwheel.ico")

def clearfields():
    ID.set("")
    NAME.set("")
    DESCRIPTION.set("")
    UNIT.set("")
    QUANTITY.set("")
    DATE.set("")

#ROOT WINDOW CONFIGURATION
root.configure(background = "gray")
root.geometry("800x360")
root.resizable(False, False)
root.title("Inventory System")
root.iconbitmap("cogwheel.ico")
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()


