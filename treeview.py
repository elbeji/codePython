from tkinter import *
from tkinter import ttk
root=Tk()

tv=ttk.Treeview(root)
tv.pack()
tv.heading('#0',text='Name')

tv.insert('','1','item1',text='Mahdi')
tv.insert('','2','item2',text='Houda')
tv.insert('','3','item3',text='Mourad')
tv.insert('','4','item4',text='Maram')

tv.insert('item1','0','item5',text='DOUDOU')
tv.insert('item1','0','item6',text='MAROUMA')
tv.insert('item2','0','item7',text='Mahdouch')
tv.insert('item3','0','item8',text='BOU OMRIN')


tv.detach('item8')
tv.move('item8','item4','0')

tv.delete('item6')
tv.configure(column=('age'))
tv.heading('age',text='Family age')

tv.set('item1','age','1.5')
tv.set('item2','age','32')
tv.set('item3','age','40')

tv.column('age',width=70,anchor='center')

def selectitem(event):
    print(tv.selection())
tv.bind('TreeviewSelect',selectitem)










    
