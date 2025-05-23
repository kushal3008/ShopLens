import sqlite3
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.pyplot import connect, title
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image,ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Kushal\OneDrive\Desktop\ShopLens\build\assets\mostSold")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def employeePassword(canvas,switch_to_adminMainmenu,shopname):
    canvas.configure(bg="#A5D1E1")
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        71.0,
        fill="#0F3ADA",
        outline="")

    canvas.create_rectangle(
        370.0,
        142.0,
        1070.0,
        742.0,
        fill="#0F3ADA",
        outline="")

    image_image_1 = PhotoImage(
        file=r"C:\Users\Kushal\OneDrive\Desktop\ShopLens\build\assets\frame0\image_1.png")
    image_1 = canvas.create_image(
        1404.0,
        35.0,
        image=image_image_1
    )
    canvas.image = image_image_1

    backButton = Button(
        text="Back",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: deleteforAdminMainMenu(),
        bg="#0F3ADA",
        fg="#FFFFFF",
        font=("Inter", 20, "bold")
    )

    backButton.place(x=0, y=10)

    adminPassBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial', 16),
        show="*"
    )

    adminPassBox.place(
        x=497.5,
        y=276.0,
        width=445.0,
        height=37.0
    )

    changeButton= Button(
        text="Check",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :checkAdminPass(),
        relief="flat",
        bg="#A5D1E1",
        fg="#000000",
        font=("Inter", 20, "bold")
    )

    changeButton.place(width=200,height=50,x=620,y=358)
    employeePassBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial', 16),
        show="*",
        state="disabled"
    )

    employeePassBox.place(
        x=497.5,
        y=510.0,
        width=445.0,
        height=37.0
    )

    canvas.create_text(
        497.5,
        226.0,
        anchor="nw",
        text="Enter Admin Password",
        fill="#FFFFFF",
        font=("Inter", 18, "bold")
    )

    canvas.create_text(
        497.5,
        460.0,
        anchor="nw",
        text="Enter Employee Password",
        fill="#FFFFFF",
        font=("Inter", 18, "bold")
    )

    confirmButton = Button(
        text="Confirm",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda :changePass(),
        bg="#A5D1E1",
        fg="#000000",
        font=("Inter", 20, "bold"),
        state="disabled"
    )

    canvas.create_text(
        503.0,
        10.0,
        anchor="nw",
        text="Employee Password",
        fill="#FFFFFF",
        font=('Inter', 34, 'bold')
    )

    confirmButton.place(width=200,height=50,x=620,y=592)


    var = [backButton,employeePassBox,changeButton,adminPassBox,confirmButton]

    def checkAdminPass():
        con = sqlite3.connect(f"ShopLens.db")
        cursor = con.cursor()
        adminpass = str(adminPassBox.get()).strip()
        query = f"select Password from User where Shopname = '{shopname}'"
        cursor.execute(query)
        data = cursor.fetchone()
        if data[0] == adminpass:
            employeePassBox.configure(state="normal")
            confirmButton.configure(state="normal")
        else:
            messagebox.showerror(title="Wrong Password",message="Enter correct admin Password")
        con.close()
        cursor.close()

    def changePass():
        confirmButton.configure(state="normal")
        EmployeePass = str(employeePassBox.get()).strip()
        con = sqlite3.connect("ShopLens.db")
        cursor = con.cursor()
        query1 = f"select EmployeePass from User where Shopname = '{shopname}' "
        cursor.execute(query1)
        data1 = cursor.fetchone()
        if data1 == EmployeePass:
            messagebox.showerror(title="Same Password",message="This password already exists.")
        elif data1 == "":
            messagebox.showerror(title="Empty Field",message="Password field is empty.")
        else:
            cursor.execute(f"Update User set EmployeePass = '{EmployeePass}' where Shopname = '{shopname}'")
            con.commit()
            adminPassBox.delete(0,tk.END)
            employeePassBox.delete(0,tk.END)
            confirmButton.configure(state="disabled")
            employeePassBox.configure(state="disabled")
            messagebox.showinfo(title="Password Changed",message="Password Changed Successfully.")
        con.close()
        cursor.close()


    def deleteforAdminMainMenu():
        for i in var:
            i.destroy()
        switch_to_adminMainmenu(shopname)