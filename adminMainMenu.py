from pathlib import Path
import sqlite3
import os
import tkinter as tk
from tkinter import messagebox, Frame
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, IntVar



def admin_menu(canvas,switch_to_mostsold,switch_to_register,switch_to_daterange,switch_to_login,switch_to_EmpPass,shopname):
    canvas.configure(bg="#A5D1E1")
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        71.0,
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




    registerButton = Button(
        text="Register & Update",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: deleteforRegister(var),
        relief="flat",
        bg="#0F3ADA",
        fg="#FFFFFF",
        font=("Inter", 20, "bold")
    )
    registerButton.place(
        x=24.0,
        y=10.0,
        width=246.0,
        height=50.0
    )

    salesButton = Button(
        text="Sales Graph",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: deleteforMostSold(var),
        relief="flat",
        bg="#0F3ADA",
        fg="#FFFFFF",
        font=("Inter", 20, "bold")
    )
    salesButton.place(
        x=300.0,
        y=10.0,
        width=216.0,
        height=50.0
    )

    dateRangeButton = Button(
        text="Date Range",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: deleteforDateRange(var),
        relief="flat",
        bg="#0F3ADA",
        fg="#FFFFFF",
        font=("Inter", 20, "bold")
    )
    dateRangeButton.place(
        x=525.0,
        y=10.0,
        width=216.0,
        height=50.0
    )

    backButton = Button(
        text="Logout",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: deleteforlogin(var),
        bg="#0F3ADA",
        fg="#FFFFFF",
        font=("Inter", 20, "bold")
    )

    backButton.place(x=1080, y=10)

    employeeButton = Button(
        text="Employee Password",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: deleteforEmpPass(var),
        bg="#0F3ADA",
        fg="#FFFFFF",
        font=("Inter", 20, "bold")
    )

    employeeButton.place(x=760, y=10)

    # notificationHolder = Frame(width=300,height=300,background="#0F3ADA")
    # notificationHolder.place(x=300,y=300)
    notificationArea = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial', 24),
        state="disabled"
    )

    notificationArea.place(
        x=270,
        y=171,
        width=900,
        height=517
    )

    canvas.create_rectangle(
        220.0,
        121.0,
        1220.0,
        738.0,
        fill="#0F3ADA",
        outline="")

    canvas.create_text(
        594.0,
        124.0,
        anchor="nw",
        text="Notifications",
        fill="#FFFFFF",
        font=("Inter", 28, "bold")
    )

    def notifications():
        con = sqlite3.connect(f"{shopname}.db")
        cursor = con.cursor()
        cursor.execute("select ProductName from Products")
        data = cursor.fetchall()
        products = [i[0] for i in data]
        stock = []
        for i in products:
            cursor.execute(f"select Quantity from Products where ProductName = '{i}' ")
            raw_quantity = cursor.fetchone()
            currentStock = raw_quantity[0]
            cursor.execute(f"select UpdatedQuantity from Products where ProductName = '{i}' ")
            raw_quantity1 = cursor.fetchone()
            if raw_quantity1[0] != None:
                minStock = int(raw_quantity1[0] * 0.20)
                if currentStock <= minStock:
                    stock.append(i)
        for j in range(len(stock)):
            notificationArea.configure(state="normal")
            notificationArea.insert(tk.END,f"{j+1}) Quantity of {stock[j]} is less.")
            notificationArea.configure(state="disabled")
        cursor.close()
        con.close()
    notifications()


    var = [registerButton, salesButton, dateRangeButton, employeeButton, backButton,notificationArea]
    def deleteforMostSold(var):
        for i in var:
            i.destroy()
        switch_to_mostsold(shopname)

    def deleteforRegister(var):
        for i in var:
            i.destroy()
        switch_to_register(shopname)

    def deleteforDateRange(var):
        for i in var:
            i.destroy()
        switch_to_daterange(shopname)

    def deleteforlogin(var):
        for i in var:
            i.destroy()
        switch_to_login()

    def deleteforEmpPass(var):
        for i in var:
            i.destroy()
        switch_to_EmpPass(shopname)