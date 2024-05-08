import tkinter as tk
from tkinter import messagebox
import pymysql
import subprocess

# Function to connect to the database
def connect_to_database():
    host = 'localhost'
    user = 'root'
    password = 'root'
    database = 'com714'
    port = 8889

    try:
        con = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        print("Database connected successfully")
        return con
    except pymysql.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Function to handle login
def login():
    root = tk.Tk()
    root.title("Login Page")
    root.geometry("800x500")

    tk.Label(root, text="Username:").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password:").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    def on_login():
        username = username_entry.get()
        password = password_entry.get()
        con = connect_to_database()

        if con:
            try:
                with con.cursor() as cur:
                    cur.execute('SELECT * FROM users WHERE username = %s', (username,))
                    user = cur.fetchone()

                    if user:
                        if user[4] == password:
                            messagebox.showinfo("Login Successful", f"Welcome, {username}")
                            root.destroy()  # Close the login window
                            open_userdatasite(user)
                        else:
                            messagebox.showinfo("Wrong Password", "Password is incorrect")
                    else:
                        messagebox.showerror("Login Failed", "Invalid username or password")

            except pymysql.Error as e:
                print(f"Error executing SQL query: {e}")
            finally:
                con.close()
        else:
            messagebox.showerror("Database Error", "Failed to connect to the database")

    tk.Button(root, text="Login", command=on_login).pack(pady=10)

    root.mainloop()

# Function to open the user data site
def open_userdatasite(user):
    # Convert all user information to strings
    user_id = str(user[0])
    first_name = user[1]
    last_name = user[2]
    username = user[3]
    password = user[4]
    status = user[5]

    # Create command and arguments for subprocess.Popen
    homepage_args = ["python3", "homepage.py", user_id, first_name, last_name, username, password, status]
    homepage_args = [str(arg) for arg in homepage_args]  # Convert all elements to strings

    # Create a new Toplevel window for user data display
    homepage_window = tk.Tk()
    homepage_window.title("User Data Site")
    homepage_window.geometry("600x400")
    # Calculate the center position of the screen
    window_width = 600
    window_height = 400
    screen_width = homepage_window.winfo_screenwidth()
    screen_height = homepage_window.winfo_screenheight()
    x_coordinate = int((screen_width - window_width) / 2)
    y_coordinate = int((screen_height - window_height) / 2)
    homepage_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")



    tk.Label(homepage_window, text=f"User ID: {user_id}").pack(pady=5)
    tk.Label(homepage_window, text=f"First Name: {first_name}").pack(pady=5)
    tk.Label(homepage_window, text=f"Last Name: {last_name}").pack(pady=5)
    tk.Label(homepage_window, text=f"Username: {username}").pack(pady=5)
    tk.Label(homepage_window, text=f"Password: {password}").pack(pady=5)
    tk.Label(homepage_window, text=f"Status: {status}").pack(pady=5)

    # Close the user data site window after 3 seconds
    homepage_window.after(3000, homepage_window.destroy)

    # Execute homepage3.py after homepage_window is closed
    subprocess.Popen(homepage_args)
# Main entry point
if __name__ == '__main__':
    login()
