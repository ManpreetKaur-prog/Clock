Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
from tkinter import*
from tkinter.ttk import*

from time import strftime

root=Tk()
root.title("clock"
           def time():
            string=strftime('%H: %M: %S %p')
           label.config(text=string)
           label.after(1000,time)
label=Label(root,font=('Helvetica',80),bg="black",fg="cyan");
label.pack(anchor='center')
time()
           
mainloop()
