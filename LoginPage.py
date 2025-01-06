
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import sqlite3
import os
from tkinter import messagebox
from SignInPage import signinPage
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, IntVar

from try2 import cursor

ASSETS_PATH = os.path.join("C:/Users/Kushal/OneDrive/Desktop/ShopLens/build/assets/frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def loginPage(canvas,switch_to_signin,switch_to_mainScreen,switch_to_reset):
    global shopname
    canvas.configure(bg="#5D6795")
    # window = Tk()
    #
    # window.geometry("1440x788")
    # window.configure(bg = "#5D6794")


    # canvas = Canvas(
    #     window,
    #     bg = "#5D6794",
    #     height = 788,
    #     width = 1440,
    #     bd = 0,
    #     highlightthickness = 0,
    #     relief = "ridge"
    # )

    canvas.place(x = 0, y = 0)


    canvas.create_rectangle(
        370.0,
        67.0,
        1070.0,
        721.0,
        fill="#A5D1E1",
        outline="")

    canvas.create_text(
        498.0,
        357.0,
        anchor="nw",
        text="Enter Your Password",
        fill="#000000",
        font=("Inter",20,"bold")
    )

    canvas.create_text(
        498.0,
        247.0,
        anchor="nw",
        text="Enter Your Email",
        fill="#000000",
        font=("Inter",20,"bold")
    )

    canvas.create_text(
        652.0,
        107.0,
        anchor="nw",
        text="Login",
        fill="#000000",
        font=("Inter",36,"bold")
    )


    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        720.5,
        301.5,
        image=entry_image_1
    )
    emailBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial',16)
    )
    emailBox.place(
        x=498.0,
        y=282.0,
        width=445.0,
        height=37.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        720.5,
        411.5,
        image=entry_image_2
    )
    passwordBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial',16),
        show="*"
    )
    passwordBox.place(
        x=498.0,
        y=392.0,
        width=445.0,
        height=37.0
    )

    # Adding View effect in Password Box

    val = IntVar()
    check = Checkbutton(variable=val, onvalue=1, offvalue=0, bg="#A5D1E1",command=lambda :passwordView())
    check.place(x=498, y=440, width=10, height=10)
    canvas.create_text(
        510.0,
        435.0,
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

    # Checking Credentials
    def login():
        global shopname
        email = str(emailBox.get().lower().strip())
        password = str(passwordBox.get().strip())
        con = sqlite3.connect("ShopLens.db")
        cursor = con.cursor()
        cursor.execute(f"select Shopname from User where Email = '{email}' and Password = '{password}'")
        data = cursor.fetchone()
        if data:
            deleteforMain(var,data[0])
        else:
            canvas.create_text(
        572.0,
        193.0,
        anchor="nw",
        text="Invalid Email or Password",
        fill="#000000",
        font=("Inter",16,"bold")
    )
            emailBox.delete(0, 'end')
            passwordBox.delete(0, 'end')


    # button_image_1 = PhotoImage(
    #     file=relative_to_assets("button_1.png"))
    loginButton = Button(
        text="Login",
        borderwidth=0,
        highlightthickness=0,
        command=login,
        font=("Inter",24,"bold"),
        relief="flat"
    )
    loginButton.place(
        x=590.0,
        y=554.0,
        width=261.0,
        height=75.0
    )

    # button_image_2 = PhotoImage(
    #     file=relative_to_assets("button_2.png"))

    forgotPass = Button(
        text="Forgot Password?",
        borderwidth=0,
        highlightthickness=0,
        font = ("Inter", 12, "bold","underline"),
        relief = "flat",
        bg = "#A5D1E1",
        fg = "#000000",
        command=lambda :deleteforReset(var)
    )
    forgotPass.place(x=801,y=437,width=141,height=19)

    signinButton = Button(
        text="Dont have an account? Sign in",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :delete(var),
        font=("Inter", 16, "bold"),
        relief="flat",
        bg="#A5D1E1",
        fg="#000000"
    )
    signinButton.place(
        x=544.0,
        y=502.0,
        width=353.0,
        height=29.0
    )
    var = [signinButton,loginButton,emailBox,passwordBox,check,forgotPass]
    def delete(var):
        for i in var:
            i.destroy()
        switch_to_signin()

    def deleteforMain(var,shopname):
        for i in var:
            i.destroy()
        switch_to_mainScreen(shopname)

    def deleteforReset(var):
        con = sqlite3.connect("ShopLens.db")
        cursor = con.cursor()
        email = str(emailBox.get().lower().strip())
        if email == "":
            messagebox.showerror(title="Error",message="Enter Email First")
        else:
            for i in var:
                i.destroy()
            switch_to_reset(email)
        con.close()


    #window.resizable(False, False)
    # window.mainloop()

if __name__ == "__main__":
    loginPage()