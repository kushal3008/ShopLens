from pathlib import Path
import sqlite3
import os
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, IntVar

def cashierLoginPage(canvas,switch_to_cashierMainMenu,switch_to_usertype):
    canvas.configure(bg="#5D6795")
    canvas.create_rectangle(
        370.0,
        67.0,
        1070.0,
        721.0,
        fill="#A5D1E1",
        outline="")

    canvas.create_text(
        498.0,
        377.0,
        anchor="nw",
        text="Enter Your Password",
        fill="#000000",
        font=("Inter", 20, "bold")
    )

    canvas.create_text(
        525.0,
        130.0,
        anchor="nw",
        text="Employee Login",
        fill="#000000",
        font=("Inter", 36, "bold")
    )

    passwordBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial', 16),
        show="*"
    )

    passwordBox.place(
        x=498.0,
        y=412.0,
        width=445.0,
        height=37.0
    )

    shopbox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial', 16),
    )

    shopbox.place(
        x=498.0,
        y=272.0,
        width=445.0,
        height=37.0
    )

    canvas.create_text(
        498.0,
        237.0,
        anchor="nw",
        text="Enter Your Shopname",
        fill="#000000",
        font=("Inter", 20, "bold")
    )

    val = IntVar()
    check = Checkbutton(variable=val, onvalue=1, offvalue=0, bg="#A5D1E1", command=lambda: passwordView())
    check.place(x=498, y=460, width=10, height=10)
    canvas.create_text(
        510.0,
        455.0,
        anchor="nw",
        text="Show Password",
        fill="#000000",
        font=("Inter", 12, "bold")
    )

    def passwordView():
        if (val.get() == 1):
            passwordBox.configure(show="")
        else:
            passwordBox.configure(show="*")

    loginButton = Button(
        text="Login",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :login(),
        font=("Inter", 24, "bold"),
        relief="flat"
    )
    loginButton.place(
        x=590.0,
        y=554.0,
        width=261.0,
        height=75.0
    )

    backButton = Button(
        text="Back",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: deleteforUsertype(),
        bg="#5D6795",
        fg="#FFFFFF",
        font=("Inter", 20, "bold")
    )

    backButton.place(x=0, y=10)

    def login():
        con = sqlite3.connect("ShopLens.db")
        cursor = con.cursor()
        password = str(passwordBox.get()).strip()
        shopname = str(shopbox.get()).strip()
        query = f"select EmployeePass from User where Shopname = '{shopname}'"
        cursor.execute(query)
        data = cursor.fetchone()
        if shopname == "":
            messagebox.showerror(title="Error",message="Enter Shopname.")
        elif password == "":
            messagebox.showerror(title="Error",message="Enter Password.")
        else:
            if data[0] == password:
                delete_for_caahierMainMenu(var,shopname)
            else:
                messagebox.showerror(title="Error",message="Password is incorrect.")

    var = [passwordBox,shopbox,loginButton,check,backButton]
    def delete_for_caahierMainMenu(var,shopname):
        for i in var:
            i.destroy()
        switch_to_cashierMainMenu(shopname)

    def deleteforUsertype():
        for i in var:
            i.destroy()
        switch_to_usertype()