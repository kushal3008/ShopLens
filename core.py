from tkinter import Tk, Canvas, Button
from adminPage import loginPage
from SignInPage import signinPage
from main_menu import mainScreen
from register_update import registerProduct
from resetPass import resetPassword
from mostSold import mostSoldGraph
from datebyrange import dateRange
from usertype import userType
from cashierlogin import cashierLoginPage
from adminMainMenu import admin_menu

def main():
    # Initialize the main Tkinter window
    window = Tk()
    window.geometry("1440x788")
    window.title("ShopLens")
    window.configure(bg="#0F3ADA")

    # Create a shared canvas to manage both pages
    canvas = Canvas(
        window,
        bg="#A5D1E1",
        height=788,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.pack()

    #Function where the main code starts
    def show_usertype():
        canvas.delete("all")
        userType(canvas,show_cashierloginpage,show_adminloginPage)

    def show_cashierloginpage():
        canvas.delete("all")
        cashierLoginPage(canvas,show_cashierMainmenu)

    def show_adminMainmenu(shopname):
        canvas.delete("all")
        admin_menu(canvas,show_mostSold,show_register,show_dateRange,shopname)

    # Function to switch to the admin login page
    def show_adminloginPage():
        canvas.delete("all")  # Clear the canvas for the new page
        loginPage(canvas, show_signin, show_adminMainmenu,show_forget)

    # Function to switch to the sign-in page
    def show_signin():
        canvas.delete("all")  # Clear the canvas for the new page
        signinPage(canvas, show_login)

    def show_cashierMainmenu(shopname):
        canvas.delete("all")
        mainScreen(canvas,shopname,show_cashierloginpage)

    def show_register(shopname):
        canvas.delete("all")
        registerProduct(canvas,shopname,show_adminMainmenu)

    def show_forget(email):
        canvas.delete("all")
        resetPassword(canvas,email,show_adminloginPage)

    def show_mostSold(shopname):
        canvas.delete("all")
        mostSoldGraph(canvas,shopname,show_adminMainmenu)

    def show_dateRange(shopname):
        canvas.delete("all")
        dateRange(canvas,shopname,show_adminMainmenu)

    # Initially, show the login page
    show_usertype()

    # Run the Tkinter main loop
    window.resizable(False,False)
    window.mainloop()


if __name__ == "__main__":
    main()
