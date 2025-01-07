import tkinter as tk
from tkinter import Label, Image, PhotoImage
import matplotlib.pyplot as plt
from PIL import Image,ImageTk
import mysql.connector
from matplotlib.pyplot import connect, title

db = mysql.connector.connect(host="localhost", user="root", passwd="Kushal3008@", database="ShopLens")
cursor = db.cursor()
def viewGraph():
    query = "select Item as Product, Sum(Quantity) as TotalQuantity from sales group by Item"
    cursor.execute(query)
    data =cursor.fetchall()
    window2 = tk.Tk()
    window2.geometry("800x800")
    if data:
        products = [row[0] for row in data]
        quantities = [row[1] for row in data]
        plt.figure(figsize=(10, 6), num="Sales Graph")
        plt.bar(products, quantities, color='skyblue')
        plt.xlabel('Product', fontsize=12)
        plt.ylabel("Quantity Sold", fontsize=12)
        plt.title("Most Sold Product", fontsize=16)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig("graph.png")
    else:
        templabel = Label(window2,text="!!!No Sale Data Available!!!")
    image1 = Image.open("graph.png")
    photo = ImageTk.PhotoImage(image1)
    salesImage = tk.Label(image=photo)
    salesImage.pack()
    cursor.close()
    db.close()
    window2.mainloop()
