from pathlib import Path
import sqlite3
import os
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, IntVar

def userType(canvas,switch_to_cashier,switch_to_admin):
    canvas.configure(bg="#5D6795")

    canvas.place(x = 0, y = 0)


    canvas.create_rectangle(
        370.0,
        67.0,
        1070.0,
        721.0,
        fill="#A5D1E1",
        outline="")

    cashierButton = Button(
        text="Login as Employee",
        borderwidth=0,
        highlightthickness=0,
        font=("Inter", 24, "bold"),
        relief="flat",
        command=lambda :deleteforcashier()
    )

    adminButton = Button(
        text="Login as Admin",
        borderwidth=0,
        highlightthickness=0,
        font=("Inter", 24, "bold"),
        relief="flat",
        command=lambda: deleteforadmin()
    )



    cashierButton.place(x=520,y=227,width=400,height=100)
    adminButton.place(x=520,y=467,width=400,height=100)

    var = [cashierButton, adminButton]
    def deleteforcashier():
        for i in var:
            i.destroy()
        switch_to_cashier()

    def deleteforadmin():
        for i in var:
            i.destroy()
        switch_to_admin()

