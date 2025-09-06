from tkinter import *

def add():
    task = entrybox.get()
    if task and task != placeholder:
        listbox.insert(END, task)
        entrybox.delete(0, END)

def update():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        new_task = entrybox.get()
        if new_task:
            listbox.delete(index)
            listbox.insert(index, new_task)
            entrybox.delete(0, END)

def delete():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

def clear_entry(event):
    if entrybox.get() == placeholder:
        entrybox.delete(0, END)
        entrybox.config(fg="black")

def fill_entry(event):
    if entrybox.get() == "":
        entrybox.insert(0, placeholder)
        entrybox.config(fg='grey')

window = Tk()
window.title("To Do List App")
window.configure(bg='#FFF7ED')
window.geometry("480x500")

try:
    icon = PhotoImage(file='logo.png')
    window.iconphoto(True, icon)
except Exception as e:
    print("File not Found")

label = Label(window, text="To Do List", font=('Comic Neue', 30, 'bold'), fg='#78350F', bg='#FCA5A5')

entrybox = Entry(window, bg="#FCE7F3", font=('Comic Neue', 15), bd=1)

placeholder = "Enter the Task here"
entrybox.insert(0, placeholder)
entrybox.bind("<FocusIn>", clear_entry)
entrybox.bind("<FocusOut>", fill_entry)

listbox = Listbox(window, bg='#D1FAE5', font=('Comic Neue', 15), bd=1, relief=SUNKEN)

frame_btn = Frame(window, bg='#FFF7ED')
add_btn = Button(frame_btn, text="ADD", command=add, font=('Comic Neue', 10, 'bold'), fg='#1E3A8A', bg='#93C5FD', bd=1)
update_btn = Button(frame_btn, text="UPDATE", command=update, font=('Comic Neue', 10, 'bold'), fg='#1E3A8A', bg='#93C5FD', bd=1)
delete_btn = Button(frame_btn, text="DELETE", command=delete, font=('Comic Neue', 10, 'bold'), fg='#1E3A8A', bg='#93C5FD', bd=1, relief=RAISED)

window.columnconfigure(0, weight=5)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=4)

label.grid(row=0, column=0, columnspan=2, sticky='WE')
entrybox.grid(row=1, column=0, columnspan=2, padx=10, ipady=10, sticky='WE')
listbox.grid(row=2, column=0, padx=10, pady=10, sticky='NEWS')
frame_btn.grid(row=2, column=1, padx=10, pady=10, sticky='NEWS')

frame_btn.columnconfigure(0, weight=1)
frame_btn.rowconfigure(0, weight=1, uniform='r')
frame_btn.rowconfigure(1, weight=1, uniform='r')
frame_btn.rowconfigure(2, weight=1, uniform='r')

add_btn.grid(row=0, column=0, padx=10, ipady=10, sticky='We')
update_btn.grid(row=1, column=0, padx=10, ipady=10, sticky='We')
delete_btn.grid(row=2, column=0, padx=10, ipady=10, sticky='We')

window.mainloop()