from Tkinter import *

root = Tk()

Label(root,text='Hello world').pack()

Button(root,text='QUIT',command=root.destroy).pack()

mainloop()
