from tkinter import *
from tkinter import ttk
from db import Database

db = Database("emplloyees.db")

app = Tk()

# creating form title
app.title("REGISTRATION FORM")
app.geometry("1366x768+0+0")
app.state("zoomed")
app.config(bg="blue")
# cerating the variable

name = StringVar()
age = StringVar()
dob = StringVar()
gender = StringVar()
number = StringVar()
addrees = StringVar()

# insert the form
entryframe = Frame(app, bg="black")
entryframe.pack(side=TOP, fill=X)
title = Label(entryframe, text="STUDENT DETAILS", font=("calibri", 15, "bold"), bg="black", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20)
# first row
lbname = Label(entryframe, text="NAME", font=("calibri", 13, "bold"), bg="black", fg="white")
lbname.grid(row=1, column=0, padx=5, pady=5, sticky="w")
txtname = Entry(entryframe, textvariable=name, font=("calibri", 15))
txtname.grid(row=1, column=1, padx=5, pady=5)

lbage = Label(entryframe, text="AGE", font=("calibri", 13, "bold"), bg="black", fg="white")
lbage.grid(row=1, column=2, padx=5, pady=5, sticky="w")
txtage = Entry(entryframe, textvariable=age, font=("calibri", 15))
txtage.grid(row=1, column=3, padx=5, pady=5)

lbdop = Label(entryframe, text="DOP", font=("calibri", 13, "bold"), bg="black", fg="white")
lbdop.grid(row=1, column=4, sticky="w")
txtdop = Entry(entryframe, textvariable=dob, font=("calibri", 15))
txtdop.grid(row=1, column=5)

# secound row
lbgender = Label(entryframe, text="AGE", font=("calibri", 13, "bold"), bg="black", fg="white")
lbgender.grid(row=2, column=0, sticky="w")
# cerating the combobox
combox = ttk.Combobox(entryframe, textvariable=gender, font=("calibri", 13), width=20, state="readonly")
combox["values"] = ("male", "female")
combox.grid(row=2, column=1)

lbnumber = Label(entryframe, text="NUMBER", font=("calibri", 13, "bold"), bg="black", fg="white")
lbnumber.grid(row=2, column=2, sticky="w")
txtnumber = Entry(entryframe, textvariable=number, font=("calibri", 15))
txtnumber.grid(row=2, column=3)
# third row
lbaddrees = Label(entryframe, text="ADDREES", font=("calibri", 13, "bold"), bg="black", fg="white")
lbaddrees.grid(row=3, column=0, sticky="w")
txtaddrees = Text(entryframe, height=5, font=("calibri", 15), width=40)
txtaddrees.grid(row=4, column=0, columnspan=4, padx=10, sticky="w")


# creating the button function
def displayall():
    for row in db.alldata():
        tv.insert("", END, values=row)
def Alldata():
    pass


def update():
    pass


def delete():
    pass


def insert():
    pass


# ceratin the button
button = Frame(entryframe, bg="black")
button.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="w")
buttonadd = Button(button, command=Alldata, text="AllDETAILS", bd=0, bg="green", fg="black", width=15,
                   font=("calibri", 15, "bold"))
buttonadd.grid(row=0, column=0, padx=5)

buttonupdate = Button(button, command=update, text="UPDATE", width=15, bd=0, bg="yellow", fg="black",
                      font=("calibri", 15, "bold"))
buttonupdate.grid(row=0, column=1, padx=5)

buttoninsert = Button(button, command=insert, text="INSERT", bd=0, bg="orange", fg="black", width=15,
                      font=("calibri", 15, "bold"))
buttoninsert.grid(row=0, column=2, padx=5)

buttondelete = Button(button, command=delete, text="DELETE", bd=0, bg="red", fg="black", width=15,
                      font=("calibri", 15, "bold"))
buttondelete.grid(row=0, column=3, padx=5)

# data show table
datatable = Frame(app, bg="white")
datatable.place(x=0, y=340, width=1370, height=500)
style = ttk.Style()
style.configure("mystyle.Treeview",font=("calibri",18),rowheight=50)#modefiy the body font
style.configure("mystyle.Treeview.Heading",font=("calibri",18)) #modify the heading



# data show in table  value cerate varibale

tv = ttk.Treeview(datatable,columns=(1, 2, 3, 4, 5, 6, 7),style="mystyle.Treeview",)
tv.heading("1", text="ID")
tv.column("1",width=2)
tv.heading("2", text="name")
tv.column("2",width=3)
tv.heading("3", text="age")
tv.column("3",width=3)
tv.heading("4", text="dob")
tv.column("4",width=3)
tv.heading("5", text="gender")
tv.column("5",width=3)
tv.heading("6", text="number")
tv.column("6",width=3)
tv.heading("7", text="addrees")
tv.column("7",width=3)
tv["show"] = "headings"
tv.pack(fill=X)

# entire programing running comment
displayall()
app.mainloop()
