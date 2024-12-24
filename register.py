import tkinter as tk
from tkinter.ttk import Button, Label
import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", passwd="Kushal3008@", database="ShopLens")
cursor = db.cursor()
def registerProduct():
    def add():
        products = productName.get().lower()
        quan = int(quantity.get())
        price = int(priceBox.get())
        query = "insert into Products(ProductName,Quantity,Price) values(%s,%s,%s)"
        values = [products,quan,price]
        cursor.execute(query,values)
        db.commit()
        success = Label(regProduct,text="!!!Product Added Successfully!!!",font=15)
        success.pack()

    regProduct = tk.Tk()
    regProduct.geometry("500x500")
    regProduct.title("Register Product")
    productName = tk.Entry(regProduct)
    quantity = tk.Entry(regProduct)
    priceBox = tk.Entry(regProduct)
    labelProName = tk.Label(regProduct,text="Enter Product Name")
    labelQuan = tk.Label(regProduct, text="Enter Quantity")
    labelPrice = tk.Label(regProduct, text="Enter Price")
    addButton = Button(regProduct,text="Add Product",command=add)
    labelProName.pack()
    productName.pack()
    labelQuan.pack()
    quantity.pack()
    labelPrice.pack()
    priceBox.pack()
    addButton.pack()