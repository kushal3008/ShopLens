ShopLens
ShopLens is a Python-based shop management system designed to streamline sales, inventory, and customer management for retail environments. The application features modules for admin and cashier operations, sales tracking, stock management, and reporting.

Features
Admin and cashier login systems

Inventory and stock management

Sales tracking and reporting (including date range and most sold products)

Customer management

Email notifications (OTP, welcome emails, password reset)

PDF report generation

Requirements
Python 3.7 or higher

Required Python packages (see below)

Installation
Clone the repository:

bash
git clone https://github.com/kushal3008/ShopLens.git
cd ShopLens
Install dependencies:

If a requirements.txt is provided:

bash
pip install -r requirements.txt
Otherwise, ensure you have the following common packages (as inferred from typical shop management apps):

bash
pip install sqlite3 pillow fpdf
(Add any other packages as needed based on import errors.)

Usage
To start the application, run the core.py file:

bash
python core.py
This will launch the main menu and allow you to access all features of ShopLens.

File Structure
core.py - Main entry point for the application

adminMainMenu.py, adminPage.py - Admin functionality

cashierlogin.py - Cashier login system

main_menu.py - Main menu logic

ShopLens.db, Shopify.db - Database files

sendOtp.py, sendWelcomeEmail.py, resetPass.py - Email and authentication utilities

PDFs/ - Generated PDF reports

assets/ - Image files for the GUI
