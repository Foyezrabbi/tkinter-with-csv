from csv import *
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("People and Contact")
root.geometry("380x350")
root.configure(bg='yellow')
main_lst = []


def add():
    lst = [name.get(), contact.get()]
    main_lst.append(lst)
    messagebox.showinfo("Information", "The data has been added successfully")


def save():
    with open("People_and_Contact.csv", "w") as file:
        write = writer(file)
        write.writerow(["Name", "Contact"])
        write.writerows(main_lst)
        messagebox.showinfo("Information", "Saved succesfully")


def clear():
    name.delete(0, END)
    contact.delete(0, END)


label1 = Label(root, text="Name: ", padx=25, pady=15)
label3 = Label(root, text="Contact: ", padx=20, pady=10)

name = Entry(root, width=30, borderwidth=3)
contact = Entry(root, width=30, borderwidth=3)

save = Button(root, text="Save", padx=20, pady=10, command=save)
add = Button(root, text="Add", padx=20, pady=10, command=add)
clear = Button(root, text="Clear", padx=18, pady=10, command=clear)
Exit = Button(root, text="Exit", padx=20, pady=10, command=root.quit)

label1.grid(row=0, column=0)
label3.grid(row=2, column=0)

name.grid(row=0, column=1)
contact.grid(row=2, column=1)
save.grid(row=4, column=0, columnspan=2)
add.grid(row=3, column=0, columnspan=2)
clear.grid(row=5, column=0, columnspan=2)
Exit.grid(row=6, column=0, columnspan=2)

root.mainloop()
