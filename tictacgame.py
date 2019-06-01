from tkinter import *
from tkinter import ttk

ActivePlayer=1 #set active player
p1=[]
p2=[]



root=Tk()
root.title("Tic tac : Player 1 ")
style=ttk.Style()
style.theme_use('classic')


bu1=ttk.Button(root,text=' ')
bu1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
bu1.config(command=lambda:BuClick(1))

bu2=ttk.Button(root,text=' ')
bu2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
bu2.config(command=lambda:BuClick(2))

bu3=ttk.Button(root,text=' ')
bu3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
bu3.config(command=lambda:BuClick(3))


bu4=ttk.Button(root,text=' ')
bu4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
bu4.config(command=lambda:BuClick(4))

bu5=ttk.Button(root,text=' ')
bu5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
bu5.config(command=lambda:BuClick(5))

bu6=ttk.Button(root,text=' ')
bu6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
bu6.config(command=lambda:BuClick(6))

bu7=ttk.Button(root,text=' ')
bu7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
bu7.config(command=lambda:BuClick(7))

bu8=ttk.Button(root,text=' ')
bu8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
bu8.config(command=lambda:BuClick(8))

bu9=ttk.Button(root,text=' ')
bu9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
bu9.config(command=lambda:BuClick(9))


def BuClick(id):
    global Activeplayer
    global p1
    global p2
    
    if (ActivePlayer==1) :
        setLayout(id,'X')
        p1.append(id)
        root.title("Player 2 play now")
        ActivePlayer=2
        #print("P1:{}".format(p1))
    elif (ActivePlayer==2) :
        setLayout(id ,'O')
        p2.append(id)
        root.title("Player 1 play now")
        ActivePlayer=1
        #print("P2:{}".format(p2))
        
def setLayout(id,texte):
    if (id==1):
        bu1.config(text=texte)
        bu1.state('disabled')
    elif id==2:
        bu2.config(text=texte)
        bu2.state('disabled')
    elif id==3:
        bu3.config(text=texte)
        bu3.state('disabled')
    elif id==4:
        bu4.config(text=texte)
        bu4.state('disabled')
    elif id==5:
        bu5.config(text=texte)
        bu5.state('disabled')
    elif id==6:
        bu6.config(text=texte)
        bu6.state('disabled')
    elif id==7:
        bu7.config(text=texte)
        bu7.state('disabled')
    elif id==8:
        bu8.config(text=texte)
        bu8.state('disabled')
    elif id==9:
        bu9.config(text=texte)
        bu9.state('disabled')
   #print(texte)# to do set button text

#def checkwiner():

root.mainloop()
