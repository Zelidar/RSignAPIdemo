import tkinter as tk

# Global variables
user_entries = []
info_window = None
text_widget = None

def APIcallOk(name, email):
    global text_widget
    if text_widget:
        text_widget.config(state=tk.NORMAL)  # Enable editing

        # Insert and style the message
        callOKmessage = "The envelope was sent to " + name + ", using " + email + "\n"
        text_widget.insert(tk.END, callOKmessage, 'call_OK')
        text_widget.see(tk.END)

        text_widget.config(state=tk.DISABLED)  # Disable editing

def update_display():
    global text_widget
    if text_widget:
        text_widget.config(state=tk.NORMAL)  # Enable editing

        # text_widget.delete(1.0, tk.END)  # Clear current text
        # # Display the last 10 entries
        # for entry in user_entries[-10:]:
        #     text_widget.insert(tk.END, entry + "\n")

        # Display the last entry
        last_entry = user_entries[-1]
        text_widget.insert(tk.END, last_entry + "\n")
        text_widget.see(tk.END)

        # Insert and style the email sent message
        userName = user_entries[-1].split(', ')[0].split(': ')[1]
        userEmail = user_entries[-1].split(', ')[2].split(': ')[1]
        email_message = "... now sending an email to: {} for user: {}\n".format(userEmail, userName)
        text_widget.insert(tk.END, email_message, 'email_sent')
        text_widget.see(tk.END)

        text_widget.config(state=tk.DISABLED)  # Disable editing

def display_info(name, email, month):
    global user_entries, info_window, text_widget

    # Add new entry
    user_entries.append(f"Name: {name}, Month: {month}, Email: {email}")

    # Create the window if it does not exist
    if not info_window or not tk.Toplevel.winfo_exists(info_window):
        info_window = tk.Toplevel()
        info_window.title("Operation Log")
        info_window.geometry("500x200")  # Set initial size

        # Create a scrollbar
        scrollbar = tk.Scrollbar(info_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a text widget with the scrollbar
        text_widget = tk.Text(info_window, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        text_widget.pack(expand=True, fill=tk.BOTH)

        # Configure the scrollbar to scroll the text widget
        scrollbar.config(command=text_widget.yview)

        # Style for messages
        text_widget.tag_configure('email_sent', foreground='red', font=('Arial', 10, 'bold'))
        text_widget.tag_configure('call_OK', foreground='green', font=('Arial', 10, 'bold'))

        close_button = tk.Button(info_window, text="Close", command=info_window.destroy)
        close_button.pack()

    # Update the display with the new entry
    update_display()
