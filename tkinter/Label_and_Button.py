import tkinter as tk

window = tk.Tk()
window.title('五更琉璃')
window.geometry('200x500') # 宽 x 高

var = tk.StringVar()

l = tk.Label(window, textvariable = var, bg = '#66ccff', font = ('微软雅黑', 12), width = 15, height = 2)
l.pack() #将小部件放置到主窗口中

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('寄刀片')
    else:
        on_hit = False
        var.set('')
        var.set('')

b = tk.Button(window, text = '伏见老贼丧天良', bg = 'white', width = 15, height = 2, command = hit_me)
b.pack()

#进入消息循环
window.mainloop()