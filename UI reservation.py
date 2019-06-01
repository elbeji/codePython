from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.title(' Ticket Reservation')
style=ttk.Style()
style.theme_use('classic')
#full name
ttk.Label(root, text= "Full name :").grid(row=0,column=0,padx=10,pady=10)
EntryFullName=ttk.Entry(root,width=30, font=('Arial',16)).grid(row=0,column=1, columnspan=2,pady=10)
#Gender
ttk.Label(root, text=" Gender :").grid(row=1,column=0)
SpanGender=StringVar()
ttk.Radiobutton(root,text="Male",variable=SpanGender, value="Male").grid(row=1,column=1)
ttk.Radiobutton(root,text="Female",variable=SpanGender, value="Female").grid(row=1,column=2)
#comment
ttk.Label(root, text= "Comment  :").grid(row=2,column=0,padx=10,pady=10)
txtComment=Text(root,width=30, heigh=10, font=('Arial',16))
txtComment.grid(row=2, column=1,columnspan=2)
#button list and submit
buSubmit=ttk.Button(root,text="Submit")
buSubmit.grid(row=3,column=3)
buList=ttk.Button(root,text="List")
buList.grid(row=3,column=2)

#action for submit and list
def BuSubmit():
    print("FullName     :{}".format(EntryFullName.getText(0,'end')))
    print("Gender       :{}".format(SpanGender.get()))
    print("Comments     :{}".format(txtComment.get(1.0,'end')))
    EntryFullName.Delete(0,'end')
    txtComment.Delete(1.0,'end')

buSubmit.config(command=BuSubmit)

          





root.mainloop()
