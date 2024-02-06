import tkinter as tk
from tkinter import ttk
from event_handling import handle_submission

class UserInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Membership Application")

        # Load and display logo
        self.logo = tk.PhotoImage(file="CompaniesLogo.png")
        tk.Label(self.root, image=self.logo).pack()

        # Name Entry
        tk.Label(self.root, text="Enter your name:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        # Email Entry
        tk.Label(self.root, text="Enter your email:").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        # CRM Customer Number Entry
        tk.Label(self.root, text="CRM Customer Number:").pack()
        self.CrmCustNbr_entry = tk.Entry(self.root)
        self.CrmCustNbr_entry.pack()

        # CRM Contract Number Entry
        tk.Label(self.root, text="CRM Contract Number:").pack()
        self.CrmContractNbr_entry = tk.Entry(self.root)
        self.CrmContractNbr_entry.pack()

        # CRM Customer String Entry
        tk.Label(self.root, text="CRM Customer String:").pack()
        self.CrmCustString_entry = tk.Entry(self.root)
        self.CrmCustString_entry.pack()

        # Month Dropdown
        tk.Label(self.root, text="Month to begin:").pack()
        self.month_var = tk.StringVar()
        self.month_combo = ttk.Combobox(self.root, textvariable=self.month_var, 
                                        values=["January", "February", "March", 
                                                "April", "May", "June", "July", 
                                                "August", "September", "October", 
                                                "November", "December"])
        self.month_combo.pack()

        # Submission Text
        submission_text = "Once you press the submit button, a membership application will be sent to the email you have entered. Please sign it."
        tk.Label(self.root, text=submission_text, wraplength=300).pack()

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Send me the contract...", command=self.submit)
        self.submit_button.pack()

        # Bind Enter key to the submit function
        self.root.bind("<Return>", self.submit)

    def submit(self, event=None):
        handle_submission(self.name_entry.get(), 
                          self.email_entry.get(), 
                          self.CrmCustNbr_entry.get(), 
                          self.CrmContractNbr_entry.get(), 
                          self.CrmCustString_entry.get(), 
                          self.month_var.get())
        self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.CrmCustNbr_entry.delete(0, tk.END)
        self.CrmContractNbr_entry.delete(0, tk.END)
        self.CrmCustString_entry.delete(0, tk.END)
        self.month_combo.set('')
