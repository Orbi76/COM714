import tkinter as tk
from tkinter import messagebox, ttk
import pymysql

def connect_to_database():
    # Specify the connection parameters
    host = 'localhost'
    user = 'root'
    password = 'root'
    database = 'com714'
    port = 8889

    # Establish a connection to the MySQL database
    try:
        con = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        print("Database connected successfully")
        return con
    except pymysql.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_users():
    # Connect to the database
    con = connect_to_database()
    if not con:
        messagebox.showerror("Error", "Failed to connect to database.")
        return None

    try:
        # Create cursor object
        cursor = con.cursor()

        # Execute SELECT query to retrieve user data
        cursor.execute("SELECT firstName, lastName, username, password, status FROM users")

        # Fetch all user records
        users = cursor.fetchall()

        cursor.close()
        con.close()

        return users
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Failed to fetch users from database: {e}")
        return None

def display_users():
    # Clear the existing treeview content
    for row in users_treeview.get_children():
        users_treeview.delete(row)

    # Fetch users from the database
    users = fetch_users()
    if users:
        for user in users:
            # Insert user data into the treeview
            users_treeview.insert("", "end", values=user)

def clear_entry_fields():
    # Clear entry fields
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    status_var.set('1')  # Reset status dropdown

def submit_data():
    # Retrieve data from entry widgets
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    status = status_var.get()  # Retrieve selected status from the dropdown

    # Validate input (ensure required fields are not empty)
    if not first_name or not last_name or not username or not password or not status:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Connect to the database
    con = connect_to_database()
    if not con:
        messagebox.showerror("Error", "Failed to connect to database.")
        return

    try:
        # Create cursor object
        cursor = con.cursor()

        # Insert user data into the database
        cursor.execute('''
            INSERT INTO users (firstName, lastName, username, password, status)
            VALUES (%s, %s, %s, %s, %s)
        ''', (first_name, last_name, username, password, status))

        con.commit()
        cursor.close()
        con.close()

        # Display confirmation message
        messagebox.showinfo("Success", "User added successfully!")

        # Refresh the list of users after submitting data
        display_users()

        # Clear entry fields
        clear_entry_fields()
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Failed to insert data into database: {e}")

def select_user():
    selected_item = users_treeview.focus()  # Get the currently selected item
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a user.")
        return

    # Retrieve user details from the selected item
    user_details = users_treeview.item(selected_item, 'values')
    if not user_details:
        messagebox.showwarning("Warning", "Invalid user selection.")
        return

    # Populate the entry fields with the selected user's details
    first_name_entry.delete(0, tk.END)
    first_name_entry.insert(0, user_details[0])

    last_name_entry.delete(0, tk.END)
    last_name_entry.insert(0, user_details[1])

    username_entry.delete(0, tk.END)
    username_entry.insert(0, user_details[2])

    password_entry.delete(0, tk.END)
    password_entry.insert(0, user_details[3])

    status_var.set(user_details[4])  # Set the status dropdown to the selected user's status

def update_details():
    # Retrieve updated details from entry widgets
    updated_first_name = first_name_entry.get()
    updated_last_name = last_name_entry.get()
    updated_username = username_entry.get()
    updated_password = password_entry.get()
    updated_status = status_var.get()

    # Retrieve original user details
    selected_item = users_treeview.focus()  # Get the currently selected item
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a user.")
        return

    user_details = users_treeview.item(selected_item, 'values')
    if not user_details:
        messagebox.showwarning("Warning", "Invalid user selection.")
        return

    original_username = user_details[2]

    # Connect to the database
    con = connect_to_database()
    if not con:
        messagebox.showerror("Error", "Failed to connect to database.")
        return

    try:
        # Create cursor object
        cursor = con.cursor()

        # Update user data in the database
        cursor.execute('''
            UPDATE users
            SET firstName = %s, lastName = %s, username = %s, password = %s, status = %s
            WHERE username = %s
        ''', (updated_first_name, updated_last_name, updated_username, updated_password, updated_status, original_username))

        con.commit()
        cursor.close()
        con.close()

        # Display updated user details
        messagebox.showinfo("Success", "User details updated successfully!")

        # Refresh the list of users after updating details
        display_users()

        # Clear entry fields
        clear_entry_fields()
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Failed to update user details: {e}")

def delete_user():
    selected_item = users_treeview.focus()  # Get the currently selected item
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a user.")
        return

    # Retrieve user details from the selected item
    user_details = users_treeview.item(selected_item, 'values')
    if not user_details:
        messagebox.showwarning("Warning", "Invalid user selection.")
        return

    # Confirm deletion with a dialog
    confirmation = messagebox.askyesno("Delete User",
                                       f"Are you sure you want to delete {user_details[0]} {user_details[1]}?")

    if confirmation:
        # Connect to the database
        con = connect_to_database()
        if not con:
            messagebox.showerror("Error", "Failed to connect to database.")
            return

        try:
            # Create cursor object
            cursor = con.cursor()

            # Delete user from the database
            cursor.execute('''
                DELETE FROM users
                WHERE firstName = %s AND lastName = %s
            ''', (user_details[0], user_details[1]))

            con.commit()
            cursor.close()
            con.close()

            # Display deletion confirmation
            messagebox.showinfo("Success", f"User {user_details[0]} {user_details[1]} deleted successfully!")

            # Refresh the list of users after deletion
            display_users()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Failed to delete user from database: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("User Management System")
root.geometry("1400x600")

# Add/manage user details section
tk.Label(root, text="Add/Manage User Details", font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

# Labels and entry widgets for first name, last name, username, password
tk.Label(root, text="First Name:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Last Name:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Username:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
username_entry = tk.Entry(root)
username_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=4, column=1, padx=10, pady=5)

# Label and dropdown menu for status
tk.Label(root, text="Status:").grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
status_var = tk.StringVar(root)
status_var.set('1')  # Set initial value for dropdown
status_choices = ['1', '2', '3', '4']
status_dropdown = tk.OptionMenu(root, status_var, *status_choices)
status_dropdown.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Select User button
select_button = tk.Button(root, text="Select User", command=select_user)
select_button.grid(row=7, column=0, padx=10, pady=10)

# Update Details button
update_button = tk.Button(root, text="Update Details", command=update_details)
update_button.grid(row=7, column=1, padx=10, pady=10)

# Delete User button
delete_button = tk.Button(root, text="Delete User", command=delete_user)
delete_button.grid(row=7, column=2, padx=10, pady=10)

# Existing users section
tk.Label(root, text="Existing Users in the Database", font=("Helvetica", 14, "bold")).grid(row=0, column=2, columnspan=2, pady=10)

# Treeview to display existing users
users_treeview = ttk.Treeview(root, columns=("First Name", "Last Name", "Username", "Password", "Status"), show="headings")
users_treeview.heading("First Name", text="First Name")
users_treeview.heading("Last Name", text="Last Name")
users_treeview.heading("Username", text="Username")
users_treeview.heading("Password", text="Password")
users_treeview.heading("Status", text="Status")
users_treeview.grid(row=1, column=2, rowspan=6, padx=10, pady=10)

# Start by displaying existing users
display_users()

# Start the main event loop
root.mainloop()
