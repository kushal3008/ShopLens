import tkinter as tk
import mysql.connector
def updateStock():
    updStk = tk.Tk()
    updStk.geometry("300x300")
    updStk.title("Update Stock")
    itemName = tk.Entry(updStk)
    itemQuantity = tk.Entry(updStk)
    labelName = tk.Label(updStk,text="Enter Product Name")
    labelQuantity = tk.Label(updStk,text="Enter Product Quantity")
    updateButton = tk.Button(updStk,text="Update",command=lambda :databaseUpdate())
    labelName.pack()
    itemName.pack()
    labelQuantity.pack()
    itemQuantity.pack()
    updateButton.pack()
    def databaseUpdate():
        db = mysql.connector.connect(host="localhost", user="root", passwd="Kushal3008@", database="ShopLens")
        cursor = db.cursor()
        item = itemName.get().lower()
        quan = int(itemQuantity.get())
        cursor.execute(f"update products set Quantity = {quan} where ProductName = '{item}';")
        db.commit()
        tempLabel = tk.Label(updStk,text=f"Updated Quantity of {item.capitalize()} to {quan}")
        tempLabel.pack()
        cursor.close()
        db.close()

