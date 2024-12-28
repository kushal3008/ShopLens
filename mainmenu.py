import tkinter as tk
from cProfile import label
from tkinter import *
from tkinter import messagebox
from datetime import date
import mysql.connector
from register import registerProduct, cursor
from salesGraph import viewGraph
billAmount = 0
def mainMenu():
    global billAmount,billID

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
    labelEmail = Label(text="Enter Customers Email")
    labelEmail.grid(row=5,column=0,sticky="w")
    emailBox = Entry(width=60)
    emailBox.grid(row=6,column=0,sticky="w")
    labelProduct = Label(text="Enter Product Name:", font=('Arial', 10)).grid(row=7, column=0, sticky="w")
    ProductBox = Entry(width=60)
    labelQuantity = Label(text="Enter Quantity:", font=('Arial', 10)).grid(row=9, column=0, sticky="w")
    QuantityBox = Entry(width=60)
    ProductBox.grid(row=8, column=0,sticky="w")
    QuantityBox.grid(row=10, column=0,sticky="w")
    generateButton = Button(text="Generate Bill",width=20,border=10,font=("Arial",13,"bold"),command=lambda :generateBill())
    generateButton.grid(row=13,column=0,sticky="w",padx=680,ipady=4)
    checkButton = Button(text="Check",border=6,font=("Arial",10,"bold"),command=lambda :customers())
    checkButton.grid(row=6,column=0,sticky="w",padx=400)


    add1 = Button(text="Add", width=20, border=6,font=("Arial",10,"bold"))
    add1.grid(padx=90, pady=10, row=11, column=0, sticky="w")

    def updateDatabase(event):
        global billAmount
        db = mysql.connector.connect(host="localhost", user="root", passwd="Kushal3008@", database="ShopLens")
        cursor = db.cursor()
        saleProduct = str(ProductBox.get().lower().strip())
        saleQuantity = int(QuantityBox.get())
        salesDate = date.today()
        cursor.execute(f"select Price from products where ProductName = '{saleProduct}';")
        result1 = cursor.fetchone()
        if result1:
            salesPrice = int(result1[0])
        else:
            salesPrice = 0

        salesAmount = saleQuantity * salesPrice
        cursor.execute(f"select Quantity from Products where ProductName = '{saleProduct}';")
        result2 = cursor.fetchone()
        if int(result2[0]) > 0:
            stockUpdate = int(result2[0]) - saleQuantity
            billAmount += salesAmount
            cursor.execute("select BillId from buys order by BillId desc limit 1;")
            result3 = cursor.fetchone()
            if result3:
                billID = int(result3[0]) + 1
            else:
                billID = 1000
            query2 = "insert into sales(BillId,Item,Quantity,PricePerUnit,Amount,Date) values (%s,%s,%s,%s,%s,%s)"
            values = [billID, saleProduct, saleQuantity, salesPrice, salesAmount, salesDate]
            cursor.execute(query2, values)
            cursor.execute(f"update Products set Quantity = {stockUpdate} where ProductName = '{saleProduct}';")
            db.commit()

            # Displaying total amount of the purchase

            totalAmount.config(state="normal")
            totalAmount.delete(0, tk.END)  # Clear the entry before inserting new value
            totalAmount.insert(tk.END, f"Total Amount:\t{billAmount}")
            totalAmount.config(state="readonly")

            # Displaying items added in cart

            items = f"{saleProduct}\t\t\t\t\t\t\t{saleQuantity}\t\t\t\t\t\t\t{salesPrice}\t\t\t\t\t\t\t{salesAmount}"
            billarea.config(state="normal")
            billarea.insert(tk.END, items + "\n")
            billarea.config(state="disabled")
            ProductBox.delete(0, tk.END)
            QuantityBox.delete(0, tk.END)
            cursor.close()
            db.close()
        elif int(result2[0]) == 0:
            messagebox.showinfo(message=f"!!{saleProduct.capitalize()} is out of stock!!")
            ProductBox.delete(0, tk.END)
            QuantityBox.delete(0, tk.END)
        else:
            ProductBox.delete(0, tk.END)
            QuantityBox.delete(0, tk.END)

    #Adding event to update database

    add1.bind("<Button-1>",updateDatabase)

    #Addinng Textarea where bill item will be displayed

    billarea = Text(height=20,width=186,background="light blue",font=('Arial',11,"bold"))
    billarea.config(state="normal")
    billarea.insert(tk.END, 297 * f"-" + "\n")
    billarea.insert(tk.END, f"Product Name\t\t\t\t\t\t\tQuantity\t\t\t\t\t\t\tPrice Per Quantity\t\t\t\t\t\t\tAmount\n")
    billarea.insert(tk.END, 297*f"-"+"\n")
    billarea.config(state="disabled")
    billarea.grid(padx=20,row=12,column=0,sticky="w")

    #Displaying Total Amount

    totalAmount = Entry(width=30, font=('Arial', 15, 'bold'),background="white")
    totalAmount.insert(tk.END, f"Total Amount:\t{billAmount}")
    totalAmount.config(state="readonly")
    totalAmount.grid(row=13, column=0, pady=20, padx=200, ipady=10, sticky="e")

    #Add customer detail to database

    def customers():
        db = mysql.connector.connect(host="localhost", user="root", passwd="Kushal3008@", database="ShopLens")
        cursor = db.cursor()
        query1 = "insert into Customers(Name,Email) values (%s,%s);"
        saleCustomer = customerName.get().lower()
        salesEmail = emailBox.get().lower()
        cursor.execute(f"select * from customers where Email = '{salesEmail}'")
        temp = cursor.fetchone()
        if temp:
            emailfound = Label(text="!!Email Found!!",font=("Arial",10,"bold"))
            emailfound.grid(row=6,column=0,padx=500,sticky="w")
        else:
            values1 = [saleCustomer, salesEmail]
            cursor.execute(query1, values1)
            emailadded = Label(text="!!New Customer Added!!", font=("Arial", 10, "bold"))
            emailadded.grid(row=6, column=0, padx=500, sticky="w")
            db.commit()


        cursor.close()
        db.close()


    # Generate Bill and send to email

    def generateBill():
        db = mysql.connector.connect(host="localhost", user="root", passwd="Kushal3008@", database="ShopLens")
        cursor = db.cursor()
        salesEmail = emailBox.get().lower()
        cursor.execute(f"select CustomerId from customers where Email = '{salesEmail}'")
        result = cursor.fetchone()
        if result:
            customerID = int(result[0])
        else:
            messagebox.showerror(title="Error",message="No Customer Found")
        cursor.execute(f"insert into buys(CustomerId) values ({customerID})")
        db.commit()
        ProductBox.delete(0, tk.END)
        QuantityBox.delete(0, tk.END)
        emailBox.delete(0,tk.END)
        customerName.delete(0,tk.END)
        billarea.config(state="normal")
        billarea.delete("4.0",tk.END)
        billarea.config(state="disabled")
        cursor.close()
        db.close()

    window.mainloop()



if __name__ == "__main__":
    mainMenu()
