import tkinter as tk

# Global variables
user_entries = []
info_window = None
text_widget = None

def update_display():
    global text_widget
    if text_widget:
        text_widget.config(state=tk.NORMAL)  # Enable editing
        text_widget.delete(1.0, tk.END)  # Clear current text

        # Display the last 10 entries and the email sent message
        for entry in user_entries[-10:]:
            text_widget.insert(tk.END, entry + "\n")

        # Insert and style the email sent message
        email_message = "An email was sent to: {}\n".format(user_entries[-1].split(', ')[2].split(': ')[1])
        text_widget.insert(tk.END, email_message, 'email_sent')

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

        text_widget = tk.Text(info_window, wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH)

        # Style for email sent message
        text_widget.tag_configure('email_sent', foreground='red', font=('Arial', 12, 'bold'))

        close_button = tk.Button(info_window, text="Close", command=info_window.destroy)
        close_button.pack()

    # Update the display with the new entry
    update_display()
