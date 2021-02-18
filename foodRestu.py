import tkinter
from tkinter import *
import math
import parser


root = Tk()
root.title("Foodei")
root.config(background="white")
root.geometry("608x370")
#root.resizable(width=False, height=False)

calc = Frame(root)
calc.grid()




#######     Heading     #######
heading = Label(calc, text="Foodie Resturent",font=('Hgit initelvetica',20,'bold'),fg='red')
heading.grid(row=0,column=0,columnspan=10,pady=2)

######## adds #########

qty = {
    'Samosa' : 1,
    'Momo' : 1,
    'Cabbage' :1,
    'Beans' : 1,
    'Tikiya' : 1,
    'Eggrol' : 1,
    'Pigs' : 1,
    'Cattle' : 1,
    'Eggs' : 1,
    'Burger' : 1,
    'OnianRing' : 1,
    'Idli' : 1,
    'Sandwich' : 1,
    'Pizza' : 1,
    'Olan' : 1,
    'Roll' : 1,
}

def add(name,f_id,price):
    global qty
    
    if qty[name] > 1:
        order.delete(f_id)
        order.insert(f_id, "{} x  {} = \t{}".format(name,qty[name],qty[name]*price))
        
    else:
        order.insert(f_id, "{} x  {} = \t{}".format(name,qty[name],qty[name]*price))
    total_amount = qty[name]* price
    qty[name] += 1
    print(total_amount)
    

#######    1st row  Button    #######
button1 = Button(calc, text="Samosa",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('Samosa',0,7))
button1.grid(row=1, column=0,pady=4,padx=3)

button2 = Button(calc, text="Momo",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('Momo',1,40))
button2.grid(row=1, column=1)

button3 = Button(calc, text="Cabbage",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('Cabbage',2,50))
button3.grid(row=1, column=3)

button4 = Button(calc, text="Beans",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('Beans',3,70))
button4.grid(row=1, column=4)

########    list    ######
order = Listbox(calc, width=30,height=18,bd=3)
order.grid(row=1, column=5,padx=10,rowspan=44,pady=40)

#######   2nd row  Button    #######
button5 = Button(calc, text="Tikiya",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('Tikiya',4,15))
button5.grid(row=2, column=0,pady=4,padx=3)

button6 = Button(calc, text="Eggrol",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3, command=lambda: add('Eggrol',5,49))
button6.grid(row=2, column=1)

button7 = Button(calc, text="Pigs",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('Pigs',6,80))
button7.grid(row=2, column=3)

button8 = Button(calc, text="Cattle",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="green", bd=3,command=lambda: add('Cattle',7,101))
button8.grid(row=2, column=4)

#######   3rd  row Button    #######
button9 = Button(calc, text="Eggs",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('Eggs',8,725))
button9.grid(row=3, column=0,pady=4,padx=3)

button10 = Button(calc, text="Burger",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('Burger',9,66))
button10.grid(row=3, column=1)

button11 = Button(calc, text="OnianRing",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('OnianRing',10,77))
button11.grid(row=3, column=3)

button12 = Button(calc, text="Idli",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('Idli',11,45))
button12.grid(row=3, column=4)

#######   4th  row Button    #######
button13 = Button(calc, text="Sandwich",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('Sandwich',12,150))
button13.grid(row=4, column=0,pady=4,padx=3)

button14 = Button(calc, text="Pizza",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('Pizza',13,75))
button14.grid(row=4, column=1,padx=4)

button15 = Button(calc, text="Olan",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('Olan',14,90))
button15.grid(row=4, column=3,padx=4)

button16 = Button(calc, text="Roll",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="grey", bd=3,command=lambda: add('Roll',15,25))
button16.grid(row=4, column=4,padx=4)


#######   5th  row Button    #######
button13 = Button(calc, text="Clear",font=('Arival',13,'bold'),fg='black', width=8, height=2, background="yellow", bd=3)
button13.grid(row=5, column=0,pady=4,padx=3)

button14 = Button(calc, text="Back",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="green", bd=3)
button14.grid(row=5, column=1)

button15 = Button(calc, text="Done",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="blue", bd=3)
button15.grid(row=5, column=3)

button16 = Button(calc, text="Print",font=('Arival',13,'bold'),fg='white', width=8, height=2, background="black", bd=3)
button16.grid(row=5, column=4)
#########   List    ###

button = Label(calc, text="List of Foodie",font=('comicsansms',15,'bold','italic'),fg='green', width=11, height=1)
button.grid(row=1, column=5)


button = Label(calc, text="Total Bill",font=('Arival',15,'bold'),fg='Green', width=11, height=2, bd=4)
button.grid(row=5, column=5)

#root.attributes("-fullscreen",True)

root.mainloop()
