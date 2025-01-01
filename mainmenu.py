import tkinter as tk
from cProfile import label
from tkinter import *
from tkinter import messagebox
from datetime import date
import mysql.connector
from register import registerProduct, cursor
from salesGraph import viewGraph
from updatestock import updateStock
from fpdf import FPDF
import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
def mainMenu():
    global billID

    #Creating a desktop
    window = tk.Tk()
    window.geometry("1920x1024")
    window.title("ShopLens")

    #Creating Menubar to register product

    menubar = tk.Menu(window)
    window.config(menu=menubar)
    optmenu =tk.Menu(menubar,tearoff=0)
    salesMenu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Options",menu=optmenu)
    menubar.add_cascade(label="Sales",menu=salesMenu)
    salesMenu.add_command(label="View Sales Graph",command=lambda :viewGraph())
    optmenu.add_command(label="Register Product",command=lambda :registerProduct())
    optmenu.add_command(label="Update Inventory",command=lambda :updateStock())

    #Adding GUI for creating bill

    lable0 = Label(text="=============================================").grid(row=0, column=0,sticky="w")
    lable1 = Label(text="Create Bill",font=('Arial',15)).grid(row=1,column=0,sticky="w",padx=120)
    lable2 = Label(text="=============================================").grid(row=2,column=0,sticky="w")
    labelCustomer = Label(text="Enter Customer Name:",font=('Arial',10)).grid(row=3,column=0,sticky="w")
    customerName = Entry(width=60)
    customerName.grid(row=4,column=0,sticky="w")
    labelEmail = Label(text="Enter Customers Email")
    labelEmail.grid(row=5,column=0,sticky="w")
    emailBox = Entry(width=60)
    emailBox.grid(row=6,column=0,sticky="w")
    labelProduct = Label(text="Enter Product Name:", font=('Arial', 10)).grid(row=7, column=0, sticky="w")
    ProductBox = Entry(width=60)
    labelQuantity = Label(text="Enter Quantity:", font=('Arial', 10)).grid(row=9, column=0, sticky="w")
    QuantityBox = Entry(width=60)
    ProductBox.grid(row=8, column=0,sticky="w")
    QuantityBox.grid(row=10, column=0,sticky="w")
    generateButton = Button(text="Generate Bill",width=20,border=10,font=("Arial",13,"bold"),command=lambda :generateBill())
    generateButton.grid(row=13,column=0,sticky="w",padx=680,ipady=4)
    checkButton = Button(text="Check",border=6,font=("Arial",10,"bold"),command=lambda :customers())
    checkButton.grid(row=6,column=0,sticky="w",padx=400)


    add1 = Button(text="Add", width=20, border=6,font=("Arial",10,"bold"))
    add1.grid(padx=90, pady=10, row=11, column=0, sticky="w")

    def updateDatabase(event):
        db = mysql.connector.connect(host="localhost", user="root", passwd="Kushal3008@", database="ShopLens")
        cursor = db.cursor()

        saleProduct = str(ProductBox.get().lower().strip())
        saleQuantity = int(QuantityBox.get())
        salesDate = date.today()
        cursor.execute(f"select Price from products where ProductName = '{saleProduct}';")
        result1 = cursor.fetchone()
        if result1:
            salesPrice = int(result1[0])
        else:
            salesPrice = 0

        salesAmount = saleQuantity * salesPrice
        cursor.execute(f"select Quantity from Products where ProductName = '{saleProduct}';")
        result2 = cursor.fetchone()
        if int(result2[0]) > 0:
            stockUpdate = int(result2[0]) - saleQuantity
            cursor.execute("select BillId from buys order by BillId desc limit 1;")
            result3 = cursor.fetchone()
            if result3:
                billID = int(result3[0]) + 1
            else:
                billID = 1000
            query2 = "insert into sales(BillId,Item,Quantity,PricePerUnit,Amount,Date) values (%s,%s,%s,%s,%s,%s)"
            values = [billID, saleProduct, saleQuantity, salesPrice, salesAmount, salesDate]
            cursor.execute(query2, values)
            cursor.execute(f"update Products set Quantity = {stockUpdate} where ProductName = '{saleProduct}';")
            db.commit()
            cursor.execute(f"select sum(Amount) from sales where BillId = {billID};")
            result = cursor.fetchone()
            if result[0] != None:
                billAmount = int(result[0])
            else:
                billAmount = 0



            # Displaying total amount of the purchase

            totalAmount.config(state="normal")
            totalAmount.delete(0, tk.END)  # Clear the entry before inserting new value
            totalAmount.insert(tk.END, f"Total Amount:\t{billAmount}")
            totalAmount.config(state="readonly")

            # Displaying items added in cart

            items = f"{saleProduct  }\t\t\t\t\t\t\t{saleQuantity}\t\t\t\t\t\t\t{salesPrice}\t\t\t\t\t\t\t{salesAmount}"
            billarea.config(state="normal")
            billarea.insert(tk.END, items + "\n")
            billarea.config(state="disabled")
            ProductBox.delete(0, tk.END)
            QuantityBox.delete(0, tk.END)
            cursor.close()
            db.close()
        elif int(result2[0]) == 0:
            messagebox.showinfo(message=f"!!{saleProduct.capitalize()} is out of stock!!")
            ProductBox.delete(0, tk.END)
            QuantityBox.delete(0, tk.END)
        else:
            ProductBox.delete(0, tk.END)
            QuantityBox.delete(0, tk.END)

    #Adding event to update database

    add1.bind("<Button-1>",updateDatabase)

    #Addinng Textarea where bill item will be displayed

    billarea = Text(height=20,width=186,background="light blue",font=('Arial',11,"bold"))
    billarea.config(state="normal")
    billarea.insert(tk.END, 297 * f"-" + "\n")
    billarea.insert(tk.END, f"Product Name\t\t\t\t\t\t\tQuantity\t\t\t\t\t\t\tPrice Per Quantity\t\t\t\t\t\t\tAmount\n")
    billarea.insert(tk.END, 297*f"-"+"\n")
    billarea.config(state="disabled")
    billarea.grid(padx=20,row=12,column=0,sticky="w")

    #Displaying Total Amount


    totalAmount = Entry(width=30, font=('Arial', 15, 'bold'),background="white")
    totalAmount.config(state="normal")
    totalAmount.insert(tk.END, f"Total Amount:\t0")
    totalAmount.config(state="readonly")
    totalAmount.grid(row=13, column=0, pady=20, padx=200, ipady=10, sticky="e")

    #Add customer detail to database

    def customers():
        db = mysql.connector.connect(host="localhost", user="root", passwd="Kushal3008@", database="ShopLens")
        cursor = db.cursor()
        query1 = "insert into Customers(Name,Email) values (%s,%s);"
        saleCustomer = customerName.get().lower()
        salesEmail = emailBox.get().lower()
        cursor.execute(f"select * from customers where Email = '{salesEmail}'")
        temp = cursor.fetchone()
        if temp:
            emailfound = Label(text="!!Email Found!!",font=("Arial",10,"bold"))
            emailfound.grid(row=6,column=0,padx=500,sticky="w")
        else:
            values1 = [saleCustomer, salesEmail]
            cursor.execute(query1, values1)
            emailadded = Label(text="!!New Customer Added!!", font=("Arial", 10, "bold"))
            emailadded.grid(row=6, column=0, padx=500, sticky="w")
            db.commit()


        cursor.close()
        db.close()


    # Generate Bill and send to email

    def generateBill():
        db = mysql.connector.connect(host="localhost", user="root", passwd="Kushal3008@", database="ShopLens")
        cursor = db.cursor()
        salesEmail = emailBox.get().lower()
        cursor.execute(f"select CustomerId from customers where Email = '{salesEmail}'")
        result = cursor.fetchone()
        if result:
            customerID = int(result[0])
        else:
            messagebox.showerror(title="Error",message="No Customer Found")
        cursor.execute(f"insert into buys(CustomerId) values ({customerID})")
        db.commit()
        ProductBox.delete(0, tk.END)
        QuantityBox.delete(0, tk.END)
        emailBox.delete(0,tk.END)
        customerName.delete(0,tk.END)
        cursor.execute("select BillId from buys order by BillId desc limit 1;")
        result3 = cursor.fetchone()
        if result3:
            billID = int(result3[0])
        else:
            billID = 1000
        path,email = generatePDF(billID)
        send_email_with_pdf(path,email)
        billAmount = 0
        totalAmount.config(state="normal")
        totalAmount.delete(0, tk.END)  # Clear the entry before inserting new value
        totalAmount.insert(tk.END, f"Total Amount:\t{billAmount}")
        totalAmount.config(state="readonly")
        billarea.config(state="normal")
        billarea.delete("1.0",tk.END)
        billarea.config(state="disabled")
        billarea.config(state="normal")
        billarea.insert(tk.END, 297 * f"-" + "\n")
        billarea.insert(tk.END,f"Product Name\t\t\t\t\t\t\tQuantity\t\t\t\t\t\t\tPrice Per Quantity\t\t\t\t\t\t\tAmount\n")
        billarea.insert(tk.END, 297 * f"-" + "\n")
        billarea.config(state="disabled")
        cursor.close()
        db.close()

    def generatePDF(BillId):
        db = mysql.connector.connect(host="localhost", user="root", passwd="Kushal3008@", database="ShopLens")
        cursor = db.cursor()
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()

        # Add Invoice Number
        pdf.set_font(family="Times", style="B", size=32)
        pdf.cell(w=185, h=16, txt="ShopLens", ln=1, align="C")

        # Add Invoice Number
        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=8, txt=f"BillID: BID{BillId}", ln=1)

        # Fetch and add Date
        query = f"SELECT Date FROM sales WHERE BillId={BillId} GROUP BY Date;"
        cursor.execute(query)
        date = cursor.fetchall()
        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=8, txt=f"Date : {date[0][0]}", ln=1)

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
        cursor.close()
        db.close()
        return (path,email)

    def send_email_with_pdf(pdf_path,receiver):
        subject = "Subject: Your Shopping Bill"
        body = "Thanks for purchase."
        host = "smtp.gmail.com"
        port = 465
        user_name = "kushal.om30@gmail.com"  # Email address
        password = "evju lcnd zmwl wdow"  # App password

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
    window.mainloop()



if __name__ == "__main__":
    mainMenu()
