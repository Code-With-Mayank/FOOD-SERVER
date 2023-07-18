from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Food Ordering Interface")
root.configure(bg="#7A7A67")

Tops = Frame(root,bg="green",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'algerian' ,50, 'bold' ),text=" <<  -* FOOD-SERVER *- >> ",bg="#4B4B00",fg="#FFFFD7",bd=12,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'Monotype Corsiva' ,16, 'bold' ),text=" <<  Welcome! Please make your order by viewing the Menu  >> ",fg="red",bg="#FFFF72",bd=12,anchor='w')
lblinfo.grid(row=2,column=0)
lblinfo = Label(Tops, font=( 'BODONI MT' ,18, 'bold' ),text=localtime,bg="#000080",fg="white",anchor=W)
lblinfo.grid(row=1,column=0)

#---------------Calculator------------------
text_Input=StringVar()
operator =""

txtdisplay = Entry(f2,font=('arial' ,20,'bold'), textvariable=text_Input , bd= 5 ,insertwidth= 7 ,bg="#FFFFC1",justify='right')
txtdisplay.grid(columnspan = 4)

def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup = str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980,50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*199
    costoflargefries = colfries*239
    costofburger = cob*75
    costoffilet = cofi*149
    costofcheeseburger = cochee*90
    costofdrinks = codr*35

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")


btn7=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="7",bg="powder blue", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="8",bg="powder blue", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="9",bg="powder blue", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="+",bg="powder blue", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="4",bg="powder blue", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="5",bg="powder blue", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="6",bg="powder blue", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Substraction=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="-",bg="powder blue", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="1",bg="powder blue", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="2",bg="powder blue", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="3",bg="powder blue", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="*",bg="powder blue", command=lambda: btnclick("*") )
multiply.grid(row=4,column=3)
#------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="0",bg="powder blue", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="c",bg="powder blue", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=10,width =10, fg="black", font=('ariel', 20 ,'bold'),text="=",bg="powder blue",command=eqals)
btnequal.grid(row=6,columnspan =4)

Decimal=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text=".",bg="powder blue", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="/",bg="powder blue", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)
status = Label(f1,font=('Monotype corsiva', 20,'bold'),width =30, text=" --* by Mayank Jha *--",bd= 5,fg="white",bg="#272740",relief=SUNKEN)
status.grid(row=11,columnspan = 3)

#---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()


lblreference = Label(f1, font=( 'Engravers MT' ,14, 'bold' ),text="Order No.",fg="maroon",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,14,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="light pink" ,justify='right',state="readonly")
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'Engravers MT' ,14, 'bold' ),text="Veg Combo",fg="maroon",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,14,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="light pink" ,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=( 'Engravers MT' ,14, 'bold' ),text="Non-Veg Combo",fg="maroon",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,14,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="light pink" ,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=( 'Engravers MT' ,14, 'bold' ),text="French Fries",fg="maroon",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,14,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="light pink" ,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=( 'Engravers MT' ,14, 'bold' ),text="Pizza",fg="maroon",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('ariel' ,14,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="light pink" ,justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'Engravers MT' ,14, 'bold' ),text="Cheese Burger",fg="maroon",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,14,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="light pink" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'Engravers MT' ,14, 'bold' ),text="Drinks",fg="maroon",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('ariel' ,14,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="light pink" ,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = Label(f1, font=( 'Engravers MT' ,14, 'bold' ),text="Cost",fg="maroon",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('arial' ,14,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="light pink" ,justify='right',state="readonly")
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'Engravers MT' ,14, 'bold' ),text="Service Charge",fg="maroon",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('arial' ,14,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="light pink" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'Engravers MT' ,14, 'bold' ),text="Tax",fg="maroon",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('arial' ,14,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="light pink" ,justify='right',state="readonly")
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'Engravers MT' ,14, 'bold' ),text="Subtotal",fg="maroon",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('arial' ,14,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="light pink" ,justify='right',state="readonly")
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'Engravers MT' ,14, 'bold' ),text="Total Cost",fg="maroon",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('arial' ,14,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="light pink" ,justify='right',state="readonly")
txtTotal.grid(row=5,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('book antiqua' ,16,'bold'),width=10, text="TOTAL", bg="brown",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('book antiqua' ,16,'bold'),width=10, text="RESET", bg="brown",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('book antiqua' ,16,'bold'),width=10, text="EXIT", bg="brown",command=qexit)
btnexit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List Menu")
    roo.configure(bg="#E0E0FF")

    lblinfo = Label(roo, font=('Book antiqua', 20, 'bold'), text="ITEM",bg="#E0E0FF", fg="blue", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('Book antiqua', 20, 'bold'), text="PRICE",bg="#E0E0FF", fg="blue", anchor=W)
    lblinfo.grid(row=0, column=5)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text=" Veg Combo ",bg="#E0E0FF", fg="purple", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="199",bg="#E0E0FF", fg="red", anchor=W)
    lblinfo.grid(row=1, column=5)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Non-Veg Combo", bg="#E0E0FF",fg="purple", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="249",bg="#E0E0FF", fg="red", anchor=W)
    lblinfo.grid(row=2, column=5)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="French Fries", bg="#E0E0FF",fg="purple", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="75", bg="#E0E0FF",fg="red", anchor=W)
    lblinfo.grid(row=3, column=5)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza",bg="#E0E0FF", fg="purple", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="149",bg="#E0E0FF", fg="red", anchor=W)
    lblinfo.grid(row=4, column=5)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger",bg="#E0E0FF", fg="purple", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="90",bg="#E0E0FF", fg="red", anchor=W)
    lblinfo.grid(row=5, column=5)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cold Drinks",bg="#E0E0FF", fg="Purple", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35",bg="#E0E0FF", fg="red", anchor=W)
    lblinfo.grid(row=6, column=5)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('book antiqua' ,14,'bold'),width=10, text="MENU", bg="brown",command=price)
btnprice.grid(row=7, column=0)

root.mainloop()