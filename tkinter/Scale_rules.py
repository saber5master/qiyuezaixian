import tkinter as tk

window = tk.Tk()
window.title('saber')
window.geometry('300x500')

l = tk.Label(window, bg = '#66ccff', font = ('微软雅黑', 15), width = 20, text = 'empty')
l.pack()

def print_selection(v):
    l.config(text = 'you have selected ' + v) #

s = tk.Scale(window, label = 'try me', font = ('微软雅黑', 10), from_ = 5, to = 11, orient = tk.HORIZONTAL, length = 200, showvalue = 0, tickinterval = 3, resolution = 0.01, command = print_selection)
s.pack()

window.mainloop()