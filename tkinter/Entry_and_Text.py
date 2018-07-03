import tkinter as tk

window = tk.Tk()
window.title('saber')
window.geometry('300x500')

e = tk.Entry(window, show='*')
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert', var)

def insert_end():
    var = e.get()
    # t.insert('end', var)
    t.insert(1.1, var) # 第一行 第一列

b1 = tk.Button(window, text='insert point', width = 15, height = 2, bg = '#66ccff', command = insert_point)
b1.pack()

b2 = tk.Button(window, text = 'insert_end', width = 15, height = 2, bg = '#66ccff', command = insert_end)
b2.pack()

t = tk.Text(window, height = 2, font = ('微软雅黑'))
t.pack()

window.mainloop()