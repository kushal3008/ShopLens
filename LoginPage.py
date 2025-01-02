
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import sqlite3
import os
from SignInPage import signinPage
from main_menu import mainScreen
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



ASSETS_PATH = os.path.join("C:/Users/Kushal/OneDrive/Desktop/ShopLens/build/assets/frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def loginPage(canvas,switch_to_signin,switch_to_mainScreen):
    con = sqlite3.connect("ShopLens.db")
    cursor = con.cursor()
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
        fill="#0F3ADA",
        outline="")

    canvas.create_text(
        498.0,
        357.0,
        anchor="nw",
        text="Enter Your Password",
        fill="#FFFFFF",
        font=("Inter Bold", 29 * -1)
    )

    canvas.create_text(
        498.0,
        247.0,
        anchor="nw",
        text="Enter Your Email",
        fill="#FFFFFF",
        font=("Inter Bold", 29 * -1)
    )

    canvas.create_text(
        652.0,
        107.0,
        anchor="nw",
        text="Login",
        fill="#FFFFFF",
        font=("Inter Bold", 50 * -1)
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

    # Checking Credentials
    def login():
        email = str(emailBox.get().lower().strip())
        password = str(passwordBox.get().lower().strip())
        con = sqlite3.connect("ShopLens.db")
        cursor = con.cursor()
        cursor.execute(f"select UserID from User where Email = '{email}' and Password = '{password}'")
        data = cursor.fetchone()
        if data:
            deleteforMain()
        else:
            canvas.create_text(
        572.0,
        193.0,
        anchor="nw",
        text="Invalid Email or Password",
        fill="#FFFFFF",
        font=("Inter Bold", 24 * -1)
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
        font=("Inter",29,"bold"),
        relief="flat",
        bg="#A5D1E1"
    )
    loginButton.place(
        x=590.0,
        y=554.0,
        width=261.0,
        height=75.0
    )

    # button_image_2 = PhotoImage(
    #     file=relative_to_assets("button_2.png"))
    signinButton = Button(
        text="Dont have an account? Sign in",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :delete(var),
        font=("Inter", 20, "bold"),
        relief="flat",
        bg="#0F3ADA",
        fg="#FFFFFF",
        foreground="#FFFFFF"
    )
    signinButton.place(
        x=495.0,
        y=468.0,
        width=450.0,
        height=50.0
    )
    con.close()
    var = [signinButton,loginButton,emailBox,passwordBox]
    def delete(var):
        for i in var:
            i.destroy()
        switch_to_signin()
    def deleteforMain():
        for i in var:
            i.destroy()
        switch_to_mainScreen()


    #window.resizable(False, False)
    # window.mainloop()

if __name__ == "__main__":
    loginPage()