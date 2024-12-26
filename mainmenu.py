import tkinter as tk
from cProfile import label
from tkinter import *
from datetime import date
import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", passwd="Kushal3008@", database="ShopLens")
cursor = db.cursor()
from register import registerProduct
from salesGraph import viewGraph
billAmount = 0

def mainMenu():
    global billAmount
    #Creating a desktop
    window = tk.Tk()
    window.geometry("1920x1024")
    window.title("ShopLens")

    #Creating Menubar to register product

    menubar = tk.Menu(window)
    window.config(menu=menubar)
    optmenu =tk.Menu(menubar,tearoff=0)
    salesMenu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Options",menu=optmenu)
    menubar.add_cascade(label="Sales",menu=salesMenu)
    salesMenu.add_command(label="View Sales Graph",command=lambda :viewGraph())
    optmenu.add_command(label="Register Product",command=lambda :registerProduct())

    #Adding GUI for creating bill


    lable0 = Label(text="=============================================").grid(row=0, column=0,sticky="w")
    lable1 = Label(text="Create Bill",font=('Arial',15)).grid(row=1,column=0,sticky="w",padx=120)
    lable2 = Label(text="=============================================").grid(row=2,column=0,sticky="w")
    labelCustomer = Label(text="Enter Customer Name:",font=('Arial',10)).grid(row=3,column=0,sticky="w")
    customerName = Entry(width=60)
    customerName.grid(row=4,column=0,sticky="w")
    labelProduct = Label(text="Enter Product Name:", font=('Arial', 10)).grid(row=5, column=0, sticky="w")
    ProductBox = Entry(width=60)
    labelQuantity = Label(text="Enter Quantity:", font=('Arial', 10)).grid(row=7, column=0, sticky="w")
    QuantityBox = Entry(width=60)
    ProductBox.grid(row=6, column=0,sticky="w")
    QuantityBox.grid(row=8, column=0,sticky="w")

    # Clearing box after one product is added

    def clear():

        ProductBox.delete(0,tk.END)
        QuantityBox.delete(0, tk.END)


    add1 = Button(text="Add", width=20, border=6, command=clear)
    add1.grid(padx=90, pady=10, row=9, column=0, sticky="w")

    def updateDatabase(event):
        global billAmount

        saleCustomer = customerName.get().lower()
        saleProduct = str(ProductBox.get().lower())
        saleQuantity = int(QuantityBox.get())
        salesDate = date.today()
        query1 = "select Price from products where ProductName = %s;"
        cursor.execute(query1,(saleProduct,))
        result1 = cursor.fetchone()
        if result1:
            salesPrice = int(result1[0])
        else:
            salesPrice = 0

        salesAmount = saleQuantity * salesPrice
        query3 = "select Quantity from Products where ProductName = %s;"
        cursor.execute(query3,(saleProduct,))
        result2 = cursor.fetchone()
        if result2:
            stockUpdate = int(result2[0]) - saleQuantity
        else:
            stockUpdate = 0

        billAmount += salesAmount
        query2 = "insert into sales(CustomerName,Item,ItemQuantity,PricePerUnit,Amount,Date) values (%s,%s,%s,%s,%s,%s)"
        values = [saleCustomer,saleProduct,saleQuantity,salesPrice,salesAmount,salesDate]
        cursor.execute(query2,values)
        cursor.execute(f"update Products set Quantity = {stockUpdate} where ProductName = '{saleProduct}';")
        db.commit()

        totalAmount.config(state="normal")
        totalAmount.delete(0, tk.END)  # Clear the entry before inserting new value
        totalAmount.insert(tk.END, f"Total Amount:\t{billAmount}")
        totalAmount.config(state="readonly")



        # Displaying items added in cart

        items = f"{saleProduct}\t\t\t\t\t\t\t{saleQuantity}\t\t\t\t\t\t\t{salesPrice}\t\t\t\t\t\t\t{salesAmount}"
        billarea.config(state="normal")
        billarea.insert(tk.END, items + "\n")
        billarea.config(state="disabled")


    #Adding event to update database

    add1.bind("<Button-1>",updateDatabase)

    #Addinng Textarea where bill item will be displayed


    billarea = Text(height=20,width=186,background="light blue",font=('Arial',11,"bold"))
    billarea.insert(tk.END, 297 * f"-" + "\n")
    billarea.insert(tk.END, f"Product Name\t\t\t\t\t\t\tQuantity\t\t\t\t\t\t\tPrice Per Quantity\t\t\t\t\t\t\tAmount\n")
    billarea.insert(tk.END, 297*f"-"+"\n")
    billarea.config(state="disabled")
    billarea.grid(padx=20,row=10,column=0,sticky="w")

    #Displaying Total Amount

    totalAmount = Entry(width=30, font=('Arial', 15, 'bold'),background="white")
    totalAmount.insert(tk.END, f"Total Amount:\t{billAmount}")
    totalAmount.config(state="readonly")
    totalAmount.grid(row=11, column=0, pady=20, padx=200, ipady=10)




    window.mainloop()



if __name__ == "__main__":
    mainMenu()
