from tkinter import *
from tkinter import ttk
root=Tk()


f0=ttk.Frame(root)
f0.pack()
f0.config(width=200,height=200,relief=RIDGE)

f1=ttk.Frame(root)
f1.pack()
f1.config(width=200,height=200,relief=RIDGE)

f2=ttk.Frame(root)
f2.pack()
f2.config(width=200,height=200,relief=RIDGE)

text=ttk.Entry(f0,text='').pack()

b1=ttk.Button(f1,text='1').grid(row=0,column=0)
b2=ttk.Button(f1,text='2').grid(row=0,column=1)
b3=ttk.Button(f1,text='3').grid(row=0,column=2)
b4=ttk.Button(f1,text='4').grid(row=1,column=0)
b5=ttk.Button(f1,text='5').grid(row=1,column=1)
b6=ttk.Button(f1,text='6').grid(row=1,column=2)
b7=ttk.Button(f1,text='7').grid(row=2,column=0)
b8=ttk.Button(f1,text='8').grid(row=2,column=1)
b9=ttk.Button(f1,text='9').grid(row=2,column=2)
b0=ttk.Button(f1,text='0').grid(row=3,column=0)
b1=ttk.Button(f1,text='.').grid(row=3,column=1)
b2=ttk.Button(f1,text='=').grid(row=3,column=2)

b3=ttk.Button(f2,text='B3').pack()
b4=ttk.Button(f2,text='B4').pack()
b5=ttk.Button(f2,text='B5').pack()
