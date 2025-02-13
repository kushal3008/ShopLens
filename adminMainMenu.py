from pathlib import Path
import sqlite3
import os
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, IntVar
def admin_menu(canvas,switch_to_mostsold,switch_to_register,switch_to_daterange,shopname):
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

    var = [registerButton, salesButton, dateRangeButton]

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

