import time
from pathlib import Path
import sqlite3
from tkinter import messagebox
import tkinter as tk
from datetime import date
from datetime import datetime
from fpdf import FPDF
import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from tkinter import ttk
from PIL import Image,ImageTk
from fontTools.ttx import process
from matplotlib.pyplot import title


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("C:/Users/Kushal/OneDrive/Desktop/ShopLens/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
srno = 0
def mainScreen(canvas,shopname,switch_to_login):

    # Creating Table for a store
    global srno
    con = sqlite3.connect(f"{shopname}.db")
    cursor = con.cursor()
    customerTable = "create table if not exists Customers(CustomerId integer PRIMARY KEY AUTOINCREMENT,Name varchar(255),Email varchar(255) UNIQUE);"
    salesTable = "create table if not exists Sales(SalesId integer PRIMARY KEY AUTOINCREMENT, BillId integer, Item varchar(255), Quantity integer, PricePerUnit integer, Amount Integer, Date varchar(255));"
    buysTable = "create table if not exists Buys(BillId integer PRIMARY KEY AUTOINCREMENT, CustomerId integer);"
    productTable = "create table if not exists Products(ProductId integer PRIMARY KEY AUTOINCREMENT, ProductName varchar(255), Quantity integer, Price integer,UpdatedQuantity integer);"
    cursor.execute(customerTable)
    cursor.execute(salesTable)
    cursor.execute(buysTable)
    cursor.execute(productTable)
    canvas.configure(bg="#A5D1E1")
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        71.0,
        fill="#0F3ADA",
        outline="")

    canvas.create_text(
        10.0,
        95.0,
        anchor="nw",
        text="Enter Customer Name  ",
        fill="#000000",
        font=("Inter Bold", 21 * -1)
    )

    customerBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial',16)
    )
    customerBox.place(
        x=10.0,
        y=125.0,
        width=355.0,
        height=27.0
    )

    emailBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial', 16)
    )
    emailBox.place(
        x=438.0,
        y=125.0,
        width=355.0,
        height=27.0
    )

    productBox = ttk.Combobox(font=('Arial',16))
    productBox.place(
        x=10.0,
        y=201.0,
        width=355.0,
        height=27.0
    )

    quantityBox = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial', 16)
    )
    quantityBox.place(
        x=438.0,
        y=201.0,
        width=355.0,
        height=27.0
    )

    canvas.create_text(
        438.0,
        95.0,
        anchor="nw",
        text="Enter Customer Email",
        fill="#000000",
        font=("Inter Bold", 21 * -1)
    )

    canvas.create_text(
        10.0,
        169.0,
        anchor="nw",
        text="Enter Product Name",
        fill="#000000",
        font=("Inter Bold", 21 * -1)
    )

    canvas.create_text(
        438.0,
        169.0,
        anchor="nw",
        text="Enter Quantity",
        fill="#000000",
        font=("Inter Bold", 21 * -1)
    )

    canvas.create_rectangle(
        1030.0,
        699.0,
        1385.0,
        746.0,
        fill="#0F3ADA",
        outline="")

    canvas.create_text(
        1036.0,
        708.2451171875,
        anchor="nw",
        text="Total Amount:",
        fill="#FFFFFF",
        font=("Inter", 25 * -1,"bold")
    )

    canvas.create_rectangle(
        0.0,
        262.0,
        1440.0,
        314.0,
        fill="#0F3ADA",
        outline="")

    canvas.create_text(
        80.0,
        275.0,
        anchor="nw",
        text="Sr.No",
        fill="#FFFFFF",
        font=("Inter Bold", 21 * -1)
    )

    canvas.create_text(
        647.0,
        275.0,
        anchor="nw",
        text="Quantity",
        fill="#FFFFFF",
        font=("Inter Bold", 21 * -1)
    )

    canvas.create_text(
        916.0,
        275.0,
        anchor="nw",
        text="Price Per Unit",
        fill="#FFFFFF",
        font=("Inter Bold", 21 * -1)
    )

    canvas.create_text(
        359.0,
        275.0,
        anchor="nw",
        text="Product Name",
        fill="#FFFFFF",
        font=("Inter Bold", 21 * -1)
    )

    canvas.create_text(
        1233.0,
        275.0,
        anchor="nw",
        text="Amount",
        fill="#FFFFFF",
        font=("Inter Bold", 21 * -1)
    )

    billArea = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=('Arial', 16),
        state="disabled"
    )
    billArea.place(
        x=0.0,
        y=314.0,
        width=1440.0,
        height=348.0
    )

    homeButton = Button(
        text="Logout",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda :delete_for_login(var),
        bg="#0F3ADA",
        fg="#FFFFFF",
        font=("Inter", 20, "bold")
    )
    homeButton.place(x=0,y=10)



    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1404.0,
        35.0,
        image=image_image_1
    )
    canvas.image = image_image_1


    totalAmount = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        state="readonly",
        font=('Inter',20,"bold")
    )
    totalAmount.place(
        x=1220.0,
        y=699.0,
        width=165.0,
        height=50.0
    )

    generateButton = Button(
        text="Generate Bill",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: generateBill(),
        relief="flat",
        bg="#0F3ADA",
        fg="#FFFFFF",
        font=("Inter", 20, "bold")
    )
    generateButton.place(
        x=620.0,
        y=699.0,
        width=200.0,
        height=50.0
    )

    clearButton = Button(
        text="Clear Bill",
        bg="#0F3ADA",
        fg="#FFFFFF",
        font=('Inter',20,'bold'),
        relief="flat",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :clear()
    )

    clearButton.place(
        x=215,
        y=699,
        width=189,
        height=50
    )

    addButton = Button(
        text="Add",
        bg="#0F3ADA",
        fg="#FFFFFF",
        font=('Inter', 16, 'bold'),
        relief="flat",
        borderwidth=0,
        highlightthickness=0,
        command=lambda :addItems()
    )
    addButton.place(
        x=836,
        y=197,
        width=89.25732421875,
        height=37.6552734375
    )

    checkButton = Button(
        text="Check",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: addCustomer(),
        relief="flat",
        bg="#0F3ADA",
        fg="#FFFFFF",
        font=("Inter", 16, "bold")
    )
    checkButton.place(
        x=836.0,
        y=120.0,
        width=89.25732421875,
        height=37.6552734375
    )


    var = [homeButton,addButton,checkButton,clearButton,generateButton,totalAmount,billArea,customerBox,productBox,quantityBox,emailBox]
    # window.resizable(False, False)
    # window.mainloop()

    #Creating function to either add customer details

    def addCustomer():

        # Collecting data
        customerName = str(customerBox.get().lower().strip())
        email = str(emailBox.get().lower().strip())
        productName = str(productBox.get().lower().strip())
        quantity = quantityBox.get()
        purDate = str(date.today())
        if email == "":
            messagebox.showerror(title="Error",message="Enter Email.")
        elif customerName == "":
            messagebox.showerror(title="Error",message="Enter Customer Name.")
        else:
            cursor.execute(f"select CustomerId from Customers where Email = '{email}'")
            temp = cursor.fetchall()
            if temp:
                customerBox.configure(state="readonly")
                emailBox.configure(state="readonly")
            else:
                customerBox.configure(state="normal")
                emailBox.configure(state="normal")
                cursor.execute(f"insert into Customers(Name,Email) values('{customerName}','{email}');")
                con.commit()
                customerBox.configure(state="readonly")
                emailBox.configure(state="readonly")

    # Creating Function to generate bill
    def addItems():
        global srno
        customerName = str(customerBox.get().lower().strip())
        email = str(emailBox.get().lower().strip())
        productName = str(productBox.get().lower().strip())
        quantity = int(quantityBox.get())
        purDate = str(date.today())
        cursor.execute(f"select Quantity from Products where ProductName = '{productName}';")
        result = cursor.fetchone()
        if result:
            if int(result[0]) > 0:

                #Adding items

                cursor.execute(f"select Price from Products where ProductName = '{productName}'")
                data1 = cursor.fetchone()
                if data1:
                    pricePerUnit = int(data1[0])
                else:
                    pricePerUnit = 0
                amount = quantity * pricePerUnit
                cursor.execute("select BillId from buys order by BillId desc limit 1;")
                data2 = cursor.fetchone()
                if data2:
                    billId = int(data2[0]) + 1
                else:
                    billId = 0
                cursor.execute(f"insert into sales(Item,Quantity,PricePerUnit,Amount,Date,BillId) values('{productName}',{quantity},{pricePerUnit},{amount},'{purDate}',{billId});")

                # Updating Stock

                stockUpdate = int(result[0]) - quantity
                cursor.execute(f"update products set quantity = {stockUpdate} where ProductName = '{productName}';")

                cursor.execute(f"select sum(Amount) from sales where BillId = {billId};")
                data3 = cursor.fetchone()
                if data3:
                    billAmount = int(data3[0])
                else:
                    billAmount = 0
                srno += 1
                items = f"\t{srno}\t\t\t{productName}\t\t\t{quantity}\t\t\t{pricePerUnit}\t\t\t{amount}"
                billArea.configure(state="normal")
                billArea.insert(tk.END,items + "\n")
                billArea.configure(state="disabled")
                productBox.delete(0,tk.END)
                quantityBox.delete(0,tk.END)

                totalAmount.configure(state="normal")
                totalAmount.delete(0,tk.END)
                totalAmount.insert(tk.END,billAmount)
                totalAmount.configure(state="readonly")

            else:
                messagebox.showinfo(title="Stock Empty",message=f"{productName.capitalize()} is out of Stock")
        else:
            messagebox.showinfo(title="Error",message=f"{productName.capitalize()} not Registered")


    # Creating function to rollback

    def clear():
        con.rollback()
        billArea.configure(state="normal")
        billArea.delete(1.0,tk.END)
        billArea.configure(state="disabled")
        totalAmount.configure(state="normal")
        totalAmount.delete(0,tk.END)
        totalAmount.configure(state="readonly")

    def generateBill():
        con.commit()
        email = str(emailBox.get().lower().strip())
        cursor.execute(f"select CustomerId from customers where email = '{email}';")
        result = cursor.fetchone()
        if result:
            cusId = int(result[0])
        else:
            messagebox.showinfo(title="Error",message="No Customer Found")
        cursor.execute(f"insert into buys(CustomerId) values({cusId})")
        con.commit()
        customerBox.configure(state="normal")
        emailBox.configure(state="normal")
        billArea.configure(state="normal")
        emailBox.configure(state="normal")
        customerBox.delete(0,tk.END)
        emailBox.delete(0,tk.END)
        quantityBox.delete(0,tk.END)
        productBox.delete(0,tk.END)
        totalAmount.configure(state="normal")
        totalAmount.delete(0,tk.END)
        totalAmount.configure(state="readonly")
        billArea.delete(1.0,tk.END)
        customerBox.configure(state="normal")
        emailBox.configure(state="normal")
        cursor.execute(f"select BillId from buys order by BillId desc limit 1;")
        data1 = cursor.fetchone()
        if data1:
            billID = int(data1[0])
        else:
            billID = 1
        path, email = generatePDF(billID)
        send_email_with_pdf(path, email)

    # Creating function to generate bill in form of PDFs

    def generatePDF(BillId):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()

        # Add Invoice Number
        pdf.set_font(family="Times", style="B", size=32)
        pdf.cell(w=185, h=16, txt=f"{shopname.capitalize()}", ln=1, align="C")

        # Add Invoice Number
        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=8, txt=f"BillID: BID{BillId}", ln=1)

        # # Fetch and add Date
        # query = f"SELECT Date FROM sales WHERE BillId={BillId} GROUP BY Date;"
        # cursor.execute(query)
        # date = cursor.fetchall()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=8, txt=f"Date : {date}", ln=1)

        # Fetch and add Customer Name and Email
        query = f"""
        SELECT c.Name, c.Email 
        FROM customers AS c 
        INNER JOIN buys AS b ON c.CustomerId = b.CustomerId 
        WHERE b.BillId={BillId};
        """
        cursor.execute(query)
        name, email = cursor.fetchone()
        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=8, txt=f"Name : {str(name).capitalize()}", ln=1)
        pdf.cell(w=50, h=8, txt=f"Email : {email}", ln=1)

        # Add table headers
        columns = ["Item", "Quantity", "Price per Unit", "Amount"]
        pdf.ln(20)
        pdf.set_font(family="Times", style="B", size=12)
        pdf.cell(w=15, h=8, txt="", border=0, align="C")
        pdf.cell(w=50, h=8, txt=columns[0], border=1, align="C")
        pdf.cell(w=30, h=8, txt=columns[1], border=1, align="C")
        pdf.cell(w=50, h=8, txt=columns[2], border=1, align="C")
        pdf.cell(w=30, h=8, txt=columns[3], border=1, align="C", ln=1)

        # Fetch and add sales data
        query = f"""
        SELECT s.Item, s.Quantity, s.PricePerUnit, s.Amount 
        FROM sales AS s 
        WHERE s.BillId={BillId};
        """
        cursor.execute(query)
        total_sum = 0
        for row in cursor.fetchall():
            pdf.set_font(family="Times", size=10, style="B")
            pdf.cell(w=15, h=8, txt="", border=0, align="C")
            pdf.cell(w=50, h=8, txt=str(row[0]).capitalize(), border=1, align="C")
            pdf.set_font(family="Times", size=10)
            pdf.cell(w=30, h=8, txt=str(row[1]), border=1, align="C")
            pdf.cell(w=50, h=8, txt=str(row[2]), border=1, align="C")
            pdf.cell(w=30, h=8, txt=str(row[3]), border=1, align="C", ln=1)
            total_sum += row[3]

        # Add total row
        pdf.set_font(family="Times", style="B", size=12)
        pdf.cell(w=15, h=8, txt="", border=0, align="C")
        pdf.cell(w=50, h=8, txt="Total", border=1, align="C")
        pdf.cell(w=30, h=8, txt="-", border=1, align="C")
        pdf.cell(w=50, h=8, txt="-", border=1, align="C")
        pdf.cell(w=30, h=8, txt=str(total_sum), border=1, align="C", ln=1)

        # Save the PDF
        path = f"./PDFs/{BillId}.pdf"
        pdf.output(path)
        print("PDF generated successfully!")
        return (path,email)

    #Sending Email to the customer

    def send_email_with_pdf(pdf_path,receiver):
        subject = "Subject: Your Shopping Bill"
        body = "Thanks for purchase."
        host = "smtp.gmail.com"
        port = 465
        user_name = "kushal.limit@gmail.com"  # Email address
        password = "wbsi hlxp hizf xsnz"  # App password

        context = ssl.create_default_context()

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = user_name
        msg['To'] = receiver
        msg['Subject'] = subject

        # Attach the body of the email
        msg.attach(MIMEText(body, 'plain'))

        # Attach the PDF file
        with open(pdf_path, 'rb') as file:
            attach_part = MIMEApplication(file.read(), _subtype="pdf")
            attach_part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(pdf_path))
            msg.attach(attach_part)

        try:
            with smtplib.SMTP_SSL(host, port, context=context) as server:
                server.login(user_name, password)
                server.sendmail(user_name, receiver, msg.as_string())
            print("Email with PDF sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
    def delete_for_login(var):
        for i in var:
            i.destroy()
        switch_to_login()


    def fetchValue():
        try:
            current_val = productBox.get()
            cursor.execute(f"select ProductName from Products where ProductName like '%{current_val}%'")
            data = cursor.fetchall()
            products = [d[0] for d in data]
            productBox.configure(values=products)
        except Exception:
            pass

        canvas.after(1000,fetchValue)

    fetchValue()
