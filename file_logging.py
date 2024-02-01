def log_user_info(name, email, month):
    with open("user_data.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}, Month: {month}\n")
