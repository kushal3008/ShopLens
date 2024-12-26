import tkinter as tk
from tkinter import Label, Image, PhotoImage
import matplotlib.pyplot as plt
from PIL import Image,ImageTk
import mysql.connector
from matplotlib.pyplot import connect, title

db = mysql.connector.connect(host="localhost", user="root", passwd="Kushal3008@", database="ShopLens")
cursor = db.cursor()

def viewGraph():
    query = "select Item as Product, Sum(ItemQuantity) as TotalQuantity from sales group by Item"
    cursor.execute(query)
    data =cursor.fetchall()
    if data:
        products = [row[0] for row in data]
        quantities = [row[1] for row in data]
        plt.figure(figsize=(10, 6), num="Graph")
        plt.bar(products, quantities, color='skyblue')
        plt.xlabel('Product', fontsize=12)
        plt.ylabel("Quantity Sold", fontsize=12)
        plt.title("Most Sold Product", fontsize=16)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout
        image = plt.show()
    else:
        templabel = Label(text="!!!No Sale Data Available!!!")

    salesImage = tk.Label(image=image)
    salesImage.grid(row=0,column=0)

