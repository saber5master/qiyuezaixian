import tkinter as tk

window = tk.Tk()
window.title('saber')
window.geometry('300x500')

canvas = tk.Canvas(window, bg = '#66ccff', height = 100, width = 200)
image_file = tk.PhotoImage(file = 'D:\git_code\pycode\html\本地播放器\image\头像.jpg')
image = canvas.create_image(0, 0, anchor = 'nw', image = image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill = 'red')

canvas.pack()
# b = tk.Button(window, text = 'move', command = moveit).pack()

window.mainloop()