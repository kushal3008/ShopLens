import tkinter as tk
from tkinter import *

from register import registerProduct
def mainMenu():
    #Creating a desktop
    window = tk.Tk()
    window.geometry("1920x1024")
    window.title("ShopLens")
    #Creating Menubar to register product
    menubar = tk.Menu(window)
    window.config(menu=menubar)
    optmenu =tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Options",menu=optmenu)
    optmenu.add_command(label="Register Product",command=lambda :registerProduct())

    #Adding GUI for creating bill


    lable0 = Label(text="===========================================").grid(row=0, column=0)
    lable1 = Label(text="Create Bill",font=('Arial',15)).grid(row=1,column=0)
    lable2 = Label(text="===========================================").grid(row=2,column=0)
    labelCustomer = Label(text="Enter Customer Name:",font=('Arial',10)).grid(row=3,column=0,sticky="w")
    customerName = Entry(width=60).grid(row=4,column=0)
    labelProduct = Label(text="Enter Product Name:", font=('Arial', 10)).grid(row=5, column=0, sticky="w")
    ProductBox = Entry(width=60)
    labelQuantity = Label(text="Enter Quantity:", font=('Arial', 10)).grid(row=7, column=0, sticky="w")
    QuantityBox = Entry(width=60)
    templable = Label().grid(row=9,column=0)
    ProductBox.grid(row=6, column=0)
    QuantityBox.grid(row=8, column=0)

    # Clearing box after one product is added
    def clear():
        ProductBox.delete(0,tk.END)
        QuantityBox.delete(0, tk.END)


    add1 = Button(text="Add",width=20,border=6,command=clear).grid(row=11,column=0)


    window.mainloop()




if __name__ == "__main__":
    mainMenu()