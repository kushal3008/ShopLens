from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sqlite3
from tkinter import messagebox
import tkinter as tk

from matplotlib.pyplot import title

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("C:/Users/Kushal/OneDrive/Desktop/ShopLens/build/assets/frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def registerProduct(canvas,shopname):

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
        345.0,
        8.0,
        anchor="nw",
        text="Register Product & Update Inventory",
        fill="#FFFFFF",
        font=("Inter", 32, "bold")
    )

    canvas.create_rectangle(
        216.0,
        314.0,
        690.0,
        734.0,
        fill="#0F3ADA",
        outline="")

    # entry_image_1 = PhotoImage(
    #     file=relative_to_assets("entry_1.png"))
    # entry_bg_1 = canvas.create_image(
    #     441.5,
    #     398.5,
    #     image=entry_image_1
    # )
    productReg = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial',16)

    )
    productReg.place(
        x=276.0,
        y=376.0,
        width=355.0,
        height=27.0
    )

    # entry_image_2 = PhotoImage(
    #     file=relative_to_assets("entry_2.png"))
    # entry_bg_2 = canvas.create_image(
    #     441.5,
    #     504.5,
    #     image=entry_image_2
    # )
    quantityReg = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial',16)
    )
    quantityReg.place(
        x=276.0,
        y=476.0,
        width=355.0,
        height=27.0
    )

    # entry_image_3 = PhotoImage(
    #     file=relative_to_assets("entry_3.png"))
    # entry_bg_3 = canvas.create_image(
    #     441.5,
    #     620.5,
    #     image=entry_image_3
    # )
    priceReg = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial',16)
    )
    priceReg.place(
        x=276.0,
        y=580.0,
        width=355.0,
        height=27.0
    )

    canvas.create_text(
        276.0,
        345.0,
        anchor="nw",
        text="Enter Product Name",
        fill="#FFFFFF",
        font=("Inter", 17, "bold")
    )

    canvas.create_text(
        276.0,
        443.0,
        anchor="nw",
        text="Enter Quantity",
        fill="#FFFFFF",
        font=("Inter", 17, "bold")
    )

    canvas.create_text(
        276.0,
        549.0,
        anchor="nw",
        text="Enter Price Per Unit",
        fill="#FFFFFF",
        font=("Inter", 17, "bold")
    )
    regButton = Button(
        text="Register",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: register(),
        relief="flat",
        bg="#A5D1E1",
        font=("Inter", 20, "bold")
    )

    regButton.place(
        x=342.0,
        y=659.0,
        width=239.0,
        height=41.0
    )

    canvas.create_text(
        326.0,
        258.0,
        anchor="nw",
        text="Register Product ",
        fill="#000000",
        font=("Inter", 24, "bold")
    )

    canvas.create_rectangle(
        750.0,
        314.0,
        1224.0,
        734.0,
        fill="#0F3ADA",
        outline="")

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        986.5,
        454.5,
        image=entry_image_4
    )
    productUpd = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial',16)
    )
    productUpd.place(
        x=809.0,
        y=440.0,
        width=355.0,
        height=27.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        986.5,
        566.5,
        image=entry_image_5
    )
    quantityUpd = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial', 16)
    )
    quantityUpd.place(
        x=809.0,
        y=552.0,
        width=355.0,
        height=27.0
    )

    canvas.create_text(
        809.0,
        412.0,
        anchor="nw",
        text="Enter Product Name",
        fill="#FFFFFF",
        font=("Inter", 17, "bold")
    )

    canvas.create_text(
        809.0,
        524.0,
        anchor="nw",
        text="Enter Quantity",
        fill="#FFFFFF",
        font=("Inter", 17, "bold")
    )

    canvas.create_text(
        855.0,
        258.0,
        anchor="nw",
        text="Update Inventory",
        fill="#000000",
        font=("Inter", 24, "bold")
    )

    updateButton = Button(
        text="Update",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: update(),
        relief="flat",
        bg="#A5D1E1",
        font=("Inter", 20, "bold")
    )
    updateButton.place(
        x=894.0,
        y=659.0,
        width=187.0,
        height=41.0
    )


    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        721.0,
        170.0,
        image=image_image_1
    )
    canvas.image = image_image_1

    # Creating function to register Product

    def register():
        con = sqlite3.connect(f"{shopname}.db")
        cursor = con.cursor()
        regProduct = str(productReg.get().lower().strip())
        regQuantity = int(quantityReg.get())
        regPrice = int(priceReg.get())
        cursor.execute(f"select ProductId from products where ProductName = '{regProduct}'; ")
        data = cursor.fetchone()
        if data:
            messagebox.showinfo(title="Product Exists",message=f"{regProduct.capitalize()} is already registered.")
        else:
            cursor.execute(f"insert into products(ProductName,Quantity,Price) values('{regProduct}',{regQuantity},{regPrice});")
            messagebox.showinfo(title="Register",message=f"Registered {regProduct.capitalize()} to database")
            con.commit()
        productReg.delete(0,tk.END)
        quantityReg.delete(0,tk.END)
        priceReg.delete(0,tk.END)
        con.close()

    # Creating function to update stock into database

    def update():
        con = sqlite3.connect(f"{shopname}.db")
        cursor = con.cursor()
        updProduct = str(productUpd.get().lower().strip())
        updQuantity = int(quantityUpd.get())
        cursor.execute(f"select Quantity from Products where ProductName = '{updProduct}';")
        data = cursor.fetchone()
        if data:
            finalQuantity = int(data[0]) + updQuantity
            cursor.execute(f"update products set Quantity = {finalQuantity} where ProductName = '{updProduct}'")
            con.commit()
            messagebox.showinfo(title="Stock Updated",message=f"Updated Stock of {updProduct.capitalize()} to {finalQuantity}")
            con.close()
        else:
            messagebox.showinfo(title="Error",message=f"Product {updProduct.capitalize()} is not registered")



if __name__  == "__main__":
    registerProduct(canvas)