import sqlite3
from pathlib import Path
import random
import time
from tkinter import messagebox, Label
from sendOtp import send_email
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from matplotlib.pyplot import title

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Kushal\OneDrive\Desktop\ShopLens\build\assets\resetPassword")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def resetPassword(canvas,email,switch_to_login):
    def otpGenerate(email):
        otp = ""
        for i in range(6):
            otp += str(random.randint(0, 9))
        send_email(otp, email)
        return otp
    otp = otpGenerate(email)
    canvas.configure(bg="#5D6795")
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        370.0,
        46.0,
        1070.0,
        742.0,
        fill="#A5D1E1",
        outline="")

    canvas.create_text(
        497.0,
        463.0,
        anchor="nw",
        text="Re-enter New Password",
        fill="#000000",
        font=("Inter",20,"bold")
    )

    canvas.create_text(
        497.0,
        347.0,
        anchor="nw",
        text="Enter New Password",
        fill="#000000",
        font=("Inter",20,"bold")
    )

    canvas.create_text(
        497.0,
        231.0,
        anchor="nw",
        text="Enter OTP",
        fill="#000000",
        font=("Inter",20,"bold")
    )



    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        719.5,
        285.5,
        image=entry_image_1
    )
    otpBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ('Arial',16)
    )
    otpBox.place(
        x=497.0,
        y=266.0,
        width=445.0,
        height=37.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        719.5,
        401.5,
        image=entry_image_2
    )
    newBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Arial",16)
    )
    newBox.place(
        x=497.0,
        y=382.0,
        width=445.0,
        height=37.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        719.5,
        517.5,
        image=entry_image_3
    )
    reEnterBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial',16)
    )
    reEnterBox.place(
        x=497.0,
        y=498.0,
        width=445.0,
        height=37.0
    )

    confirmButton = Button(
        text="Confirm",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: reset(),
        relief="flat",
        font=("Inter",24,"bold")
    )
    confirmButton.place(
        x=589.0,
        y=606.0,
        width=261.0,
        height=75.0
    )

    canvas.create_text(
        523.0,
        84.0,
        anchor="nw",
        text="Reset Your Password",
        fill="#000000",
        font=("Inter",28,"bold")
    )
    backButton = Button(
        text="Back",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: deleteforlogin(var),
        bg="#5D6795",
        fg="#FFFFFF",
        font=("Inter", 20, "bold")
    )

    backButton.place(x=0, y=10)

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

    var = [backButton,confirmButton,reEnterBox,newBox,otpBox]
    def reset():
        con = sqlite3.connect("ShopLens.db")
        cursor = con.cursor()
        enteredOtp = str(otpBox.get().strip())
        newPass = str(newBox.get().strip())
        reEnterPass = str(reEnterBox.get().strip())
        if passwordcheck() == True:
            if enteredOtp == "":
                messagebox.showerror(title="Error",message="Enter OTP.")
            elif newPass == "":
                messagebox.showerror(title="Error",message="Enter Password.")
            elif reEnterPass =="":
                messagebox.showerror(title="Error",message="Re-enter Password.")
            else:
                if enteredOtp == otp:
                    if newPass == reEnterPass:
                        cursor.execute(f"UPDATE user set Password = '{newPass}' where email = '{email}'")
                        con.commit()
                        for i in var:
                            i.destroy()
                        switch_to_login()
                        messagebox.showinfo(title="Password Changed",message="Password has been changed.")
                    else:
                        messagebox.showerror(title="Error",message="Passwords do not match.")
                else:
                    messagebox.showerror(title="Error",message="Invalid OTP.")
                con.close()

    def deleteforlogin(var):
        for i in var:
            i.destroy()
        switch_to_login()

