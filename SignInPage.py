from pathlib import Path
import sqlite3
from sendWelcomeEmail import send_welcome_email
import os
from tkinter import messagebox
from tkinter import *
from warnings import catch_warnings

from mysql.connector import IntegrityError

ASSETS_PATH = os.path.join("C:/Users/Kushal/OneDrive/Desktop/ShopLens/build/assets/frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def signinPage(canvas,switch_to_login):
    # Creating database to store user data
    canvas.configure(bg="#5D6795")
    con = sqlite3.connect("ShopLens.db")
    cursor = con.cursor()
    query = "create table if not exists User(UserId integer primary key autoincrement, UserName varchar(255), Email varchar(255) Unique, Password varchar(255), ShopName varchar(255),EmployeePass varchar(255));"
    cursor.execute(query)

    # Creating UI

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


    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        720.0,
        338.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        370.0,
        46.0,
        1070.0,
        742.0,
        fill="#A5D1E1",
        outline="")

    canvas.create_text(
        498.0,
        520.0,
        anchor="nw",
        text="Enter Your Shop Name",
        fill="#000000",
        font=("Inter",20,"bold")
    )

    canvas.create_text(
        498.0,
        404.0,
        anchor="nw",
        text="Enter Your Username",
        fill="#000000",
        font=("Inter",20,"bold")
    )

    canvas.create_text(
        498.0,
        288.0,
        anchor="nw",
        text="Enter Your Password",
        fill="#000000",
        font=("Inter",20,"bold")
    )

    canvas.create_text(
        498.0,
        172.0,
        anchor="nw",
        text="Enter Your Email",
        fill="#000000",
        font=("Inter",20,"bold")
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        720.5,
        226.5,
        image=entry_image_1
    )
    signEmailBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial', 16)
    )
    signEmailBox.place(
        x=498.0,
        y=207.0,
        width=445.0,
        height=37.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        720.5,
        342.5,
        image=entry_image_2
    )
    signPassBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial', 16),
        show="*"
    )
    signPassBox.place(
        x=498.0,
        y=323.0,
        width=445.0,
        height=37.0
    )

    # Adding View effect in Password Box

    val = IntVar()
    check = Checkbutton(variable=val, onvalue=1, offvalue=0, bg="#A5D1E1", command=lambda: passwordView())
    check.place(x=498, y=370, width=10, height=10)
    canvas.create_text(
        510.0,
        365.0,
        anchor="nw",
        text="Show Password",
        fill="#000000",
        font=("Inter", 12, "bold")
    )
    def passwordView():
        if (val.get() == 1):
            signPassBox.configure(show="")
        else:
            signPassBox.configure(show="*")

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        720.5,
        458.5,
        image=entry_image_3
    )
    signUserBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial', 16)
    )
    signUserBox.place(
        x=498.0,
        y=439.0,
        width=445.0,
        height=37.0
    )

    backButton = Button(
        text="Back",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: delete(var),
        bg="#5D6795",
        fg="#FFFFFF",
        font=("Inter", 20, "bold")
    )

    backButton.place(x=0, y=10)

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        720.5,
        574.5,
        image=entry_image_4
    )
    shopnameBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial', 16)
    )
    shopnameBox.place(
        x=498.0,
        y=555.0,
        width=445.0,
        height=37.0
    )

    def passwordcheck(password):
        if len(password) > 8:
            cap = spc = char = num = 0
            for i in password:
                if i.isupper() == True:
                    cap = 1
                elif i.isdigit() == True:
                    num = 1
                elif i.isalpha() == True:
                    char = 1
                else:
                    spc = 1
            if char == cap == spc == num == 1:
                return True
            else:
                messagebox.showerror(title="Error",message="Password must contain a capital letter, a small letter, a number and a special character.")
        else:
            messagebox.showerror(title="Error", message="Enter password of minimum length 8.")

    # Inserting values
    def insertUserDetails():
        # Fetching values from GUI

        email = str(signEmailBox.get().lower().strip())
        password = str(signPassBox.get().strip())
        username = str(signUserBox.get().strip())
        shopname = str(shopnameBox.get().strip())
        if passwordcheck(password) == True:
            query1 = "insert into User(UserName, Email, Password, ShopName) values(?,?,?,?)"
            values = [username, email, password, shopname]
            cursor.execute(f"select * from User where Email = '{email}';")
            result1 = cursor.fetchall()
            if email == "":
                messagebox.showerror(title="Error",message="Enter Email.")
            elif password == "":
                messagebox.showerror(title="Error",message="Enter Password.")
            elif username == "":
                messagebox.showerror(title="Error",message="Enter Username.")
            elif shopname == "":
                messagebox.showerror(title="Error",message="Enter Shopname.")
            elif result1:
                messagebox.showinfo(title="Email Exists",message="Email already exist.")
            else:
                cursor.execute(query1, values)
                con.commit()
                cursor.execute(f"select Shopname from user where Email = '{email}';")
                dataName = cursor.fetchone()
                sqlite3.connect(f"{shopname}.db")
                con.commit()
                cursor.execute(f"select * from User where Email = '{email}';")
                result = cursor.fetchall()
                if result:
                    send_welcome_email(username,shopname,email)
                    delete(var)
                    con.close()
                else:
                    insertUserDetails()


    # button_image_1 = PhotoImage(
    #     file=relative_to_assets("button_1.png"))
    signButton = Button(
        text="Sign Up",
        borderwidth=0,
        highlightthickness=0,
        command=insertUserDetails,
        font=("Inter", 24, "bold"),
        relief="flat"
    )

    signButton.place(
        x=599.0,
        y=636.0,
        width=261.0,
        height=75.0
    )

    canvas.create_text(
        640.0,
        66.0,
        anchor="nw",
        text="Sign Up",
        fill="#000000",
        font=("Inter",36,"bold")
    )
    var = [signButton,signEmailBox,signUserBox,signPassBox,shopnameBox,check,backButton]
    def delete(var):
        for i in var:
            i.destroy()
        switch_to_login()
    #window.resizable(False, False)
    #window.mainloop()

if __name__ == "__main__":
    signinPage()
