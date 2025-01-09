import sqlite3
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.pyplot import connect, title
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image,ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Kushal\OneDrive\Desktop\ShopLens\build\assets\dateRange")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def dateRange(canvas,shopname,switch_to_mainmenu):
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
        585.0,
        10.0,
        anchor="nw",
        text="Date By Range",
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

    canvas.create_text(
        57.0,
        129.0,
        anchor="nw",
        text="Start Date",
        fill="#000000",
        font=('Inter', 16, 'bold')
    )

    canvas.create_text(
            57.0,
            219.0,
            anchor="nw",
            text="End Date",
            fill="#000000",
            font=('Inter', 16, 'bold')
        )

    homeButton = Button(text="Home", bg="#0F3ADA", fg="#FFFFFF", font=('Inter', 20, 'bold'), borderwidth=0,
                        highlightthickness=0,command=lambda :deleteforMainmenu())
    homeButton.place(x=0, y=13, width=114, height=40)

    startDate = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=('Arial', 16)
    )
    startDate.place(
        x=143.5,
        y=169.5,
        width=173.0,
        height=27.0
    )
    endDate = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=('Arial', 16)
    )
    endDate.place(
        x=143.5,
        y=257.5,
        width=173.0,
        height=27.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1404.0,
        35.0,
        image=image_image_1
    )
    canvas.image = image_image_1


    var = [homeButton]
    def deleteforMainmenu():
        for i in var:
            i.destroy()
        switch_to_mainmenu(shopname)

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
        plt.savefig("Sales2.png")
        image2 = Image.open("Sales2.png")
        resizeImage = image2.resize((800,600))
        sales_image = ImageTk.PhotoImage(resizeImage)
        imageSales = canvas.create_image(720, 429.5, image=sales_image)
        canvas.sales_image = sales_image
    else:
        templabel = Label(text="!!!No Sale Data Available!!!")
    con.close()
