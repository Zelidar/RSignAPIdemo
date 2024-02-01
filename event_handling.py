import tkinter as tk
from tkinter import messagebox  # Import messagebox explicitly
from file_logging import log_user_info
from info_display import display_info
import re
from RSignOperations import SendEnvelope, GetTemplateInfo
import threading

def is_valid_email(email):
    # Simple regex for validating an Email
    pattern = r'^\w+[\._]?\w+@\w+\.\w+$'
    return re.match(pattern, email) is not None

def is_valid_name(name):
    # Check if the name is not empty and contains only letters and spaces
    return name.isalpha() or " " in name

def is_valid_month(month):
    # Check if the month is one of the valid options
    valid_months = ["January", "February", "March", "April", "May", "June", 
                    "July", "August", "September", "October", "November", "December"]
    return month in valid_months

def handle_submission(name, email, month):
    if is_valid_email(email) and is_valid_name(name) and is_valid_month(month):
        log_user_info(name, email, month)
        display_info(name, email, month)
        # Run the SendEnvelope in a separate thread to avoid GUI freeze
        threading.Thread(target=send_email, args=(email, name)).start()
    else:
        messagebox.showerror("Error", "Invalid submission details")

def send_email(email, name):
    try:
        # If you need a RoleID, uncomment the next call and set a breakpoint
        # roles_info = GetTemplateInfo(60592)
        
        # Call the SendEnvelope function with email and name
        result = SendEnvelope(email, name)
        print(result)
        # Handle the result (e.g., update GUI or log)
    except Exception as e:
        print("Error during email sending:", e)
        messagebox.showerror("Error", "API call failed")
