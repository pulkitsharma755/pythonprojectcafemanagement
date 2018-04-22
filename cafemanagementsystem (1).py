from tkinter import *
import random
import time;
import datetime

root = Tk()
root.geometry("1350x750+0+0")
root.title("cafe management system")
root.configure(background='pink')

Tops = Frame(root, width=1350, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width=440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

ft2 = Frame(f2, width=440, height=650, bd=12, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width=440, height=50, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1a = Frame(f1, width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=6, relief="raise")

f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=330, bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=330, bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background="black")
f1.configure(background="black")
f2.configure(background="black")


# costofitems
def CostofItem():
    Item1 = float(E_Latte.get())
    Item2 = float(E_Espresso.get())
    Item3 = float(E_Iced_Latte.get())
    Item4 = float(E_Vale_coffee.get())
    Item5 = float(E_Black_coffee.get())
    Item6 = float(E_Cappuccino.get())
    Item7 = float(E_African_Coffee.get())
    Item8 = float(E_American_coffee.get())

    Item9 = float(E_Pineapple_cake.get())
    Item10 = float(E_Apple_cake.get())
    Item11 = float(E_Black_forest.get())
    Item12 = float(E_Boston_cream_cake.get())
    Item13 = float(E_Chocolate_cake.get())
    Item14 = float(E_Pan_cakes.get())
    Item15 = float(E_Coffee_cake.get())
    Item16 = float(E_Red_Valvet_cake.get())

    PriceofDrinks = (Item1 * 1.2) + (Item2 * 1.99) + (Item3 * 2.05) \
                    + (Item4 * 1.89) + (Item5 * 1.99) + (Item6 * 2.99) + (Item7 * 2.39) + (Item8 * 1.29)
    PriceofCakes = (Item9 * 1.35) + (Item10 * 2.2) + (Item11 * 1.99) \
                   + (Item12 * 1.49) + (Item13 * 1.8) + (Item14 * 1.8) + (Item15 * 1.6) + (Item16 * 1.99)

    DrinksPrice = "$", str("%.2f" % (PriceofDrinks))
    CakesPrice = "$", str("%.2f" % (PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "$", str("%.2f" % (1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "$", str("%.2f" % (PriceofDrinks + PriceofDrinks + PriceofCakes + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "$", str("%.2f" % ((PriceofCakes + PriceofDrinks + 1.59) * 0.15))
    PaidTax.set(Tax)
    TT = ((PriceofDrinks + PriceofCakes + 1.59) * 0.15)
    TC = "$", str("%.2f" % (PriceofDrinks + PriceofCakes + 1.59 + TT))
    TotalCost.set(TC)


#
def qExit():
    qExit = messagebox.askyesno("quit system", "do you want to quit?")
    if qExit > 0:
        root.destroy()
        return


def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)


# receipt
def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, "Receipt Ref:\t\t\t" + Receipt_Ref.get() + "\t\t" + DateofOrder.get() + "\n")
    txtReceipt.insert(END, "Items\t\t\t\t\t" + "cost of items\n\n")
    txtReceipt.insert(END, "Latte: \t\t\t\t\t" + E_Latte.get() + "\n")
    txtReceipt.insert(END, "Espresso: \t\t\t\t\t" + E_Espresso.get() + "\n")
    txtReceipt.insert(END, "Iced_Latte: \t\t\t\t\t" + E_Iced_Latte.get() + "\n")
    txtReceipt.insert(END, "Vale_coffee: \t\t\t\t\t" + E_Vale_coffee.get() + "\n")
    txtReceipt.insert(END, "Black_coffee: \t\t\t\t\t" + E_Black_coffee.get() + "\n")
    txtReceipt.insert(END, "Cappuccino: \t\t\t\t\t" + E_Cappuccino.get() + "\n")
    txtReceipt.insert(END, "African_Coffee: \t\t\t\t\t" + E_African_Coffee.get() + "\n")
    txtReceipt.insert(END, "American_coffee: \t\t\t\t\t" + E_American_coffee.get() + "\n")
    txtReceipt.insert(END, "Pineapple_cake: \t\t\t\t\t" + E_Pineapple_cake.get() + "\n")
    txtReceipt.insert(END, "Apple_cake: \t\t\t\t\t" + E_Apple_cake.get() + "\n")
    txtReceipt.insert(END, "Black_forest: \t\t\t\t\t" + E_Black_forest.get() + "\n")
    txtReceipt.insert(END, "Boston_cream_cake: \t\t\t\t\t" + E_Boston_cream_cake.get() + "\n")
    txtReceipt.insert(END, "Chocolate_cake: \t\t\t\t\t" + E_Chocolate_cake.get() + "\n")
    txtReceipt.insert(END, "Pan_cakes: \t\t\t\t\t" + E_Pan_cakes.get() + "\n")
    txtReceipt.insert(END, "Coffee_cake: \t\t\t\t\t" + E_Coffee_cake.get() + "\n")
    txtReceipt.insert(END, "Red_Valvet_cake: \t\t\t\t\t" + E_Red_Valvet_cake.get() + "\n")
    txtReceipt.insert(END, "cost of drinks: \t\t" + CostofDrinks.get() + "\Tax Paid:\t\t" + PaidTax.get() + "\n")
    txtReceipt.insert(END, "cost of cakes: \t\t" + CostofCakes.get() + "\tSubTotal:\t\t" + SubTotal.get() + "\n")
    txtReceipt.insert(END, "Service charge: \t\t" + ServiceCharge.get() + "\tTotal cost:\t\t" + TotalCost.get() + "\n")


# heading
lb1Info = Label(Tops, font=("arial", 70, "bold"), text="Cafe Management Systems", bd=10, anchor="w")
lb1Info.grid(row=0, column=0)

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

E_Latte = StringVar()
E_Espresso = StringVar()
E_Iced_Latte = StringVar()
E_Vale_coffee = StringVar()
E_Black_coffee = StringVar()
E_Cappuccino = StringVar()
E_African_Coffee = StringVar()
E_American_coffee = StringVar()
E_Pineapple_cake = StringVar()
E_Apple_cake = StringVar()
E_Black_forest = StringVar()
E_Boston_cream_cake = StringVar()
E_Chocolate_cake = StringVar()
E_Pan_cakes = StringVar()
E_Coffee_cake = StringVar()
E_Red_Valvet_cake = StringVar()

E_Latte.set("0")
E_Espresso.set("0")
E_Iced_Latte.set("0")
E_Vale_coffee.set("0")
E_Black_coffee.set("0")
E_Cappuccino.set("0")
E_African_Coffee.set("0")
E_American_coffee.set("0")
E_Pineapple_cake.set("0")
E_Apple_cake.set("0")
E_Black_forest.set("0")
E_Boston_cream_cake.set("0")
E_Chocolate_cake.set("0")
E_Pan_cakes.set("0")
E_Coffee_cake.set("0")
E_Red_Valvet_cake.set("0")


# calculator
def chkbutton_value():
    if (var1.get() == 1):
        txtLatte.configure(state=NORMAL)
    elif (var1.get() == 0):
        txtLatte.configure(state=DISABLED)
        E_Latte.set("0")
    if (var2.get() == 1):
        txtEspresso.configure(state=NORMAL)
    elif (var2.get() == 0):
        txtEspresso.configure(state=DISABLED)
        E_Espresso.set("0")
    if (var3.get() == 1):
        txtIced_Latte.configure(state=NORMAL)
    elif (var3.get() == 0):
        txtIced_Latte.configure(state=DISABLED)
        E_Iced_Latte.set("0")
    if (var4.get() == 1):
        txtVale_coffee.configure(state=NORMAL)
    elif (var4.get() == 0):
        txtVale_coffee.configure(state=DISABLED)
        E_Vale_coffee.set("0")
    if (var5.get() == 1):
        txtBlack_coffee.configure(state=NORMAL)
    elif (var5.get() == 0):
        txtBlack_coffee.configure(state=DISABLED)
        E_Black_coffee.set("0")
    if (var6.get() == 1):
        txtCappuccino.configure(state=NORMAL)
    elif (var6.get() == 0):
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0")
    if (var7.get() == 1):
        txtAfrican_Coffee.configure(state=NORMAL)
    elif (var7.get() == 0):
        txtAfrican_Coffee.configure(state=DISABLED)
        E_African_Coffee.set("0")
    if (var8.get() == 1):
        txtAmerican_coffee.configure(state=NORMAL)
    elif (var8.get() == 0):
        txtAmerican_coffee.configure(state=DISABLED)
        E_American_coffee.set("0")
    if (var9.get() == 1):
        txtPineapple_cake.configure(state=NORMAL)
    elif (var9.get() == 0):
        txtPineapple_cake.configure(state=DISABLED)
        E_Pineapple_cake.set("0")
    if (var10.get() == 1):
        txtApple_cake.configure(state=NORMAL)
    elif (var10.get() == 0):
        txtApple_cake.configure(state=DISABLED)
        E_Apple_cake.set("0")
    if (var11.get() == 1):
        txtChocolate_cake.configure(state=NORMAL)
    elif (var11.get() == 0):
        txtChocolate_cake.configure(state=DISABLED)
        E_Chocolate_cake.set("0")
    if (var12.get() == 1):
        txtBlack_forest.configure(state=NORMAL)
    elif (var12.get() == 0):
        txtBlack_forest.configure(state=DISABLED)
        E_Black_forest.set("0")
    if (var13.get() == 1):
        txtBoston_cream_cake.configure(state=NORMAL)
    elif (var13.get() == 0):
        txtBoston_cream_cake.configure(state=DISABLED)
        E_Boston_cream_cake.set("0")
    if (var14.get() == 1):
        txtPan_cakes.configure(state=NORMAL)
    elif (var14.get() == 0):
        txtPan_cakes.configure(state=DISABLED)
        E_Pan_cakes.set("0")
    if (var15.get() == 1):
        txtCoffee_cake.configure(state=NORMAL)
    elif (var15.get() == 0):
        txtCoffee_cake.configure(state=DISABLED)
        E_Coffee_cake.set("0")
    if (var16.get() == 1):
        txtRed_Valvet_cake.configure(state=NORMAL)
    elif (var16.get() == 0):
        txtRed_Valvet_cake.configure(state=DISABLED)
        E_Red_Valvet_cake.set("0")


# variables===========================================================
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder.set(time.strftime("%d/%m/%y"))
var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")

# drinks
Latte = Checkbutton(f1aa, text="Latte \t\t", variable=var1, onvalue=1, offvalue=0, font=("arial", 18, "bold"),
                    command=chkbutton_value).grid(row=0, sticky=W)
Espresso = Checkbutton(f1aa, text="Espresso \t\t", variable=var2, onvalue=1, offvalue=0, font=("arial", 18, "bold"),
                       command=chkbutton_value).grid(row=1, sticky=W)
Iced_Latte = Checkbutton(f1aa, text="Iced Latte \t\t", variable=var3, onvalue=1, offvalue=0, font=("arial", 18, "bold"),
                         command=chkbutton_value).grid(row=2, sticky=W)
Vale_coffee = Checkbutton(f1aa, text="Vale coffee \t\t", variable=var4, onvalue=1, offvalue=0,
                          font=("arial", 18, "bold"), command=chkbutton_value).grid(row=3, sticky=W)
Black_coffee = Checkbutton(f1aa, text="Black coffee \t\t", variable=var5, onvalue=1, offvalue=0,
                           font=("arial", 18, "bold"), command=chkbutton_value).grid(row=4, sticky=W)
Cappuccino = Checkbutton(f1aa, text="Cappuccino \t\t", variable=var6, onvalue=1, offvalue=0, font=("arial", 18, "bold"),
                         command=chkbutton_value).grid(row=5, sticky=W)
African_Coffee = Checkbutton(f1aa, text="African Coffee \t\t", variable=var7, onvalue=1, offvalue=0,
                             font=("arial", 18, "bold"), command=chkbutton_value).grid(row=6, sticky=W)
American_coffee = Checkbutton(f1aa, text="American coffee \t\t", variable=var8, onvalue=1, offvalue=0,
                              font=("arial", 18, "bold"), command=chkbutton_value).grid(row=7, sticky=W)

# cakes
Pineapple_cake = Checkbutton(f1ab, text="Pineapple cake \t\t", variable=var9, onvalue=1, offvalue=0,
                             font=("arial", 18, "bold"), command=chkbutton_value).grid(row=0, sticky=W)
Apple_cake = Checkbutton(f1ab, text="Apple cake \t\t", variable=var10, onvalue=1, offvalue=0,
                         font=("arial", 18, "bold"), command=chkbutton_value).grid(row=1, sticky=W)
Black_forest = Checkbutton(f1ab, text="Black forest \t\t", variable=var11, onvalue=1, offvalue=0,
                           font=("arial", 18, "bold"), command=chkbutton_value).grid(row=2, sticky=W)
Boston_cream_cake = Checkbutton(f1ab, text="Boston cream cake \t\t", variable=var12, onvalue=1, offvalue=0,
                                font=("arial", 18, "bold"), command=chkbutton_value).grid(row=3, sticky=W)
Chocolate_cake = Checkbutton(f1ab, text="Chocolate cake \t\t", variable=var13, onvalue=1, offvalue=0,
                             font=("arial", 18, "bold"), command=chkbutton_value).grid(row=4, sticky=W)
Pan_cakes = Checkbutton(f1ab, text="Pan cakes \t\t", variable=var14, onvalue=1, offvalue=0, font=("arial", 18, "bold"),
                        command=chkbutton_value).grid(row=5, sticky=W)
Coffee_cake = Checkbutton(f1ab, text="Coffee cake \t\t", variable=var15, onvalue=1, offvalue=0,
                          font=("arial", 18, "bold"), command=chkbutton_value).grid(row=6, sticky=W)
Red_Valvet_cake = Checkbutton(f1ab, text="Red Valvet cake \t\t", variable=var16, onvalue=1, offvalue=0,
                              font=("arial", 18, "bold"), command=chkbutton_value).grid(row=7, sticky=W)

# ================================================================================================================
txtLatte = Entry(f1aa, font=("arial", 16, "bold"), bd=8, width=6, justify="left", textvariable=E_Latte, state=DISABLED)
txtLatte.grid(row=0, column=1)
txtEspresso = Entry(f1aa, font=("arial", 16, "bold"), bd=8, width=6, justify="left", textvariable=E_Espresso,
                    state=DISABLED)
txtEspresso.grid(row=1, column=1)
txtIced_Latte = Entry(f1aa, font=("arial", 16, "bold"), bd=8, width=6, justify="left", textvariable=E_Iced_Latte,
                      state=DISABLED)
txtIced_Latte.grid(row=2, column=1)
txtVale_coffee = Entry(f1aa, font=("arial", 16, "bold"), bd=8, width=6, justify="left", textvariable=E_Vale_coffee,
                       state=DISABLED)
txtVale_coffee.grid(row=3, column=1)
txtBlack_coffee = Entry(f1aa, font=("arial", 16, "bold"), bd=8, width=6, justify="left", textvariable=E_Black_coffee,
                        state=DISABLED)
txtBlack_coffee.grid(row=4, column=1)
txtCappuccino = Entry(f1aa, font=("arial", 16, "bold"), bd=8, width=6, justify="left", textvariable=E_Cappuccino,
                      state=DISABLED)
txtCappuccino.grid(row=5, column=1)
txtAfrican_Coffee = Entry(f1aa, font=("arial", 16, "bold"), bd=8, width=6, justify="left",
                          textvariable=E_African_Coffee, state=DISABLED)
txtAfrican_Coffee.grid(row=6, column=1)
txtAmerican_coffee = Entry(f1aa, font=("arial", 16, "bold"), bd=8, width=6, justify="left",
                           textvariable=E_American_coffee, state=DISABLED)
txtAmerican_coffee.grid(row=7, column=1)

txtPineapple_cake = Entry(f1ab, font=("arial", 16, "bold"), bd=8, width=6, justify="left",
                          textvariable=E_Pineapple_cake, state=DISABLED)
txtPineapple_cake.grid(row=0, column=1)
txtApple_cake = Entry(f1ab, font=("arial", 16, "bold"), bd=8, width=6, justify="left", textvariable=E_Apple_cake,
                      state=DISABLED)
txtApple_cake.grid(row=1, column=1)
txtBlack_forest = Entry(f1ab, font=("arial", 16, "bold"), bd=8, width=6, justify="left", textvariable=E_Black_forest,
                        state=DISABLED)
txtBlack_forest.grid(row=2, column=1)
txtBoston_cream_cake = Entry(f1ab, font=("arial", 16, "bold"), bd=8, width=6, justify="left",
                             textvariable=E_Boston_cream_cake, state=DISABLED)
txtBoston_cream_cake.grid(row=3, column=1)
txtChocolate_cake = Entry(f1ab, font=("arial", 16, "bold"), bd=8, width=6, justify="left",
                          textvariable=E_Chocolate_cake, state=DISABLED)
txtChocolate_cake.grid(row=4, column=1)
txtPan_cakes = Entry(f1ab, font=("arial", 16, "bold"), bd=8, width=6, justify="left", textvariable=E_Pan_cakes,
                     state=DISABLED)
txtPan_cakes.grid(row=5, column=1)
txtCoffee_cake = Entry(f1ab, font=("arial", 16, "bold"), bd=8, width=6, justify="left", textvariable=E_Coffee_cake,
                       state=DISABLED)
txtCoffee_cake.grid(row=6, column=1)
txtRed_Valvet_cake = Entry(f1ab, font=("arial", 16, "bold"), bd=8, width=6, justify="left",
                           textvariable=E_Red_Valvet_cake, state=DISABLED)
txtRed_Valvet_cake.grid(row=7, column=1)

txtLatte.configure(state=DISABLED)
txtEspresso.configure(state=DISABLED)
txtIced_Latte.configure(state=DISABLED)
txtVale_coffee.configure(state=DISABLED)
txtBlack_coffee.configure(state=DISABLED)
txtCappuccino.configure(state=DISABLED)
txtAfrican_Coffee.configure(state=DISABLED)
txtAmerican_coffee.configure(state=DISABLED)
txtPineapple_cake.configure(state=DISABLED)
txtApple_cake.configure(state=DISABLED)
txtBlack_forest.configure(state=DISABLED)
txtBoston_cream_cake.configure(state=DISABLED)
txtChocolate_cake.configure(state=DISABLED)
txtPan_cakes.configure(state=DISABLED)
txtCoffee_cake.configure(state=DISABLED)
txtRed_Valvet_cake.configure(state=DISABLED)

# cost items information
lb1CostofDrinks = Label(f2aa, font=("arial", 16, "bold"), text="Cost of Drinks", bd=8, anchor="w")
lb1CostofDrinks.grid(row=2, column=0, sticky=W)
txtCostofDrinks = Entry(f2aa, font=("arial", 16, "bold"), textvariable=CostofDrinks, bd=8, insertwidth=2,
                        justify="left")
txtCostofDrinks.grid(row=2, column=1)

lb1CostofCakes = Label(f2aa, font=("arial", 16, "bold"), text="cost of cakes", bd=8, anchor="w")
lb1CostofCakes.grid(row=3, column=0, sticky=W)
txtCostofCakes = Entry(f2aa, font=("arial", 16, "bold"), textvariable=CostofCakes, bd=8, insertwidth=2, justify="left")
txtCostofCakes.grid(row=3, column=1)

lb1ServiceCharge = Label(f2aa, font=("arial", 16, "bold"), text="service charge", bd=8, anchor="w")
lb1ServiceCharge.grid(row=4, column=0, sticky=W)
txtServiceCharge = Entry(f2aa, font=("arial", 16, "bold"), textvariable=ServiceCharge, bd=8, insertwidth=2,
                         justify="left")
txtServiceCharge.grid(row=4, column=1)

# paymnent information
lb1PaidTax = Label(f2ab, font=("arial", 16, "bold"), text="paid tax", bd=8)
lb1PaidTax.grid(row=2, column=0, sticky=W)
txtPaidTax = Entry(f2ab, font=("arial", 16, "bold"), bd=8, insertwidth=2, justify="left", textvariable=PaidTax)
txtPaidTax.grid(row=2, column=1)

lb1SubTotal = Label(f2ab, font=("arial", 16, "bold"), text="sub total", bd=8)
lb1SubTotal.grid(row=3, column=0, sticky=W)
txtSubTotal = Entry(f2ab, font=("arial", 16, "bold"), bd=8, insertwidth=2, justify="left", textvariable=SubTotal)
txtSubTotal.grid(row=3, column=1)

lb1TotalCost = Label(f2ab, font=("arial", 16, "bold"), text="total cost", bd=8)
lb1TotalCost.grid(row=4, column=0, sticky=W)
txtTotalCost = Entry(f2ab, font=("arial", 16, "bold"), bd=8, insertwidth=2, justify="left", textvariable=TotalCost)
txtTotalCost.grid(row=4, column=1)

# ft2
lb1Receipt = Label(ft2, font=("arial", 12, "bold"), text="Receipt:", bd=2, anchor="w")
lb1Receipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(ft2, width=59, height=22, bg="white", bd=8, font=("arial", 11, "bold"))
txtReceipt.grid(row=1, column=0)

# buttons
btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=("arial", 16, "bold"), width=5, text="Total",
                  command=CostofItem).grid(row=0, column=0)
btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=("arial", 16, "bold"), width=5, text="Receipt",
                  command=Receipt).grid(row=0, column=1)
btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=("arial", 16, "bold"), width=5, text="Reset",
                  command=Reset).grid(row=0, column=2)
btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=("arial", 16, "bold"), width=5, text="Exit",
                  command=qExit).grid(row=0, column=3)

root.mainloop()

