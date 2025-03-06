from pathlib import Path
import sqlite3
import os
import tkinter as tk
from tkinter import messagebox, Frame
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, IntVar

from register import cursor


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



    notificationHolder = Frame(width=300,height=300,background="#0F3ADA")
    notificationHolder.place(x=300,y=300)

    var = [registerButton, salesButton, dateRangeButton, employeeButton, backButton]
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
        switch_to_EmpPass()