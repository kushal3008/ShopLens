import sqlite3
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.pyplot import connect, title
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,ttk
from PIL import Image,ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Kushal\OneDrive\Desktop\ShopLens\build\assets\mostSold")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def mostSoldGraph(canvas,shopname,switch_to_mainmenu):
    canvas.configure(bg="#A5D1E1")
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        71.0,
        fill="#0F3ADA",
        outline="")

    canvas.create_text(
        608.0,
        10.0,
        anchor="nw",
        text="Sales Graph",
        fill="#FFFFFF",
        font=('Inter', 34,'bold')
    )

    canvas.create_rectangle(
        0.0,
        13.0,
        114.0,
        53.0,
        fill="#0F3ADA",
        outline="")

    homeButton = Button(text="Home", bg="#0F3ADA", fg="#FFFFFF", font=('Inter', 20, 'bold'), borderwidth=0,
                        highlightthickness=0,command=lambda :deleteforMainmenu())
    homeButton.place(x=0, y=13, width=114, height=40)

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1404.0,
        35.0,
        image=image_image_1
    )
    canvas.image = image_image_1

    canvas.create_rectangle(
        320.0,
        129.5,
        1120.0,
        729.5,
        fill="#FFFFFF",
        outline=""
    )

    graphBox = ttk.Combobox(
        font=('Arial', 16),
        state="readonly",
        values= ["Sales Graph","Customer Sales","Stock Graph"]
    )
    graphBox.place(
        x=57.0,
        y=152.0,
        width=173.0,
        height=27.0
    )

    generateButton = Button(
        text="Generate",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: graphs(),
        bg="#0F3ADA",
        fg="#FFFFFF",
        font=("Inter", 20, "bold")
    )

    generateButton.place(
        x=57.0,
        y=209.0,
        width=173.0,
        height=50.0
    )




    var = [homeButton,generateButton,graphBox]
    def deleteforMainmenu():
        for i in var:
            i.destroy()
        switch_to_mainmenu(shopname)

    con = sqlite3.connect(f"{shopname}.db")
    cursor = con.cursor()
    def sales():
        con = sqlite3.connect(f"{shopname}.db")
        cursor = con.cursor()
        query = "select Item as Product, Sum(Quantity) as TotalQuantity from Sales group by Item"
        cursor.execute(query)
        data = cursor.fetchall()
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
            plt.savefig("Sales.png")
            image2 = Image.open("Sales.png")
            resizeImage = image2.resize((800,600))
            sales_image = ImageTk.PhotoImage(resizeImage)
            imageSales = canvas.create_image(720, 429.5, image=sales_image)
            canvas.sales_image = sales_image
        con.close()

    def customer():
        con = sqlite3.connect(f"{shopname}.db")
        cursor = con.cursor()
        cursor.execute("select CustomerId from Customers")
        cusName = []
        totalAmount = []
        customerid = cursor.fetchall()
        for i in customerid:
            cursor.execute(f"select BillId from Buys where CustomerId = {i[0]} ")
            billId = cursor.fetchall()
            cursor.execute(f"select Name from customers where CustomerId = {i[0]}")
            customername = cursor.fetchone()
            cusName.append(customername[0])
            sum = 0
            for j in billId:
                cursor.execute(f"select Amount from Sales where BillId = {j[0]} ")
                amount = cursor.fetchone()
                sum = sum + amount[0]
            totalAmount.append(sum)
        plt.figure(figsize=(10, 6), num="Customer")
        plt.bar(cusName, totalAmount, color='skyblue')
        plt.xlabel('Customers', fontsize=12)
        plt.ylabel("Total Bill Value", fontsize=12)
        plt.title("Customers Purchase Data", fontsize=16)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig("Customer.png")
        image3 = Image.open("Customer.png")
        resizeImage2 = image3.resize((800, 600))
        cus_image = ImageTk.PhotoImage(resizeImage2)
        imageSales = canvas.create_image(720, 429.5, image=cus_image)
        canvas.cus_image = cus_image
    con.close()


    def stock():
        con = sqlite3.connect(f"{shopname}.db")
        cursor = con.cursor()
        query = "select ProductName as Product, Quantity as TotalStock from Products order by Quantity desc"
        cursor.execute(query)
        data3 = cursor.fetchall()
        if data3:
            products1 = [row[0] for row in data3]
            quantities1 = [row[1] for row in data3]
            plt.figure(figsize=(10, 6), num="Stock")
            plt.bar(products1, quantities1, color='skyblue')
            plt.xlabel('Product', fontsize=12)
            plt.ylabel("Stock Remaining", fontsize=12)
            plt.title("Stock Details", fontsize=16)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig("Stock.png")
            image3 = Image.open("Stock.png")
            resizeImage3 = image3.resize((800, 600))
            stock_image = ImageTk.PhotoImage(resizeImage3)
            imageStock = canvas.create_image(720, 429.5, image=stock_image)
            canvas.stock_image = stock_image
        con.close()


    def graphs():
        match(str(graphBox.get().strip())):
            case "Sales Graph": sales()
            case "Customer Sales": customer()
            case "Stock Graph": stock()



    con.close()
