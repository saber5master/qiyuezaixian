import tkinter as tk

window = tk.Tk()
window.title('saber')
window.geometry('300x500')

var1 = tk.StringVar()
l = tk.Label(window, bg = 'yellow', width = 4, textvariable = var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(window, text = 'print_selection', width = 15, height = 2, command = print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(window, listvariable = var2)
lsit_items = [1,2,3,4]
for item in lsit_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.pack()

window.mainloop()