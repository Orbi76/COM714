import tkinter as tk
from tkinter import ttk, messagebox
import pymysql

# Global variables for entry widgets
entry_first_name = None
entry_last_name = None
entry_dob = None
entry_gender = None
entry_email = None
entry_phone_number = None
entry_address = None

# Function to establish connection to MySQL database
def connect_to_database():
    try:
        con = pymysql.connect(host='localhost', port=8889, user='root', password='root', database='com714')
        messagebox.showinfo("Success", "Connected to MySQL database!")
        return con
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error connecting to MySQL database: {e}")
        return None

# Function to retrieve existing passenger details from MySQL database
def display_passengers():
    try:
        con = connect_to_database()
        if con:
            cur = con.cursor()
            cur.execute("SELECT id, first_name, last_name, dob, gender, email, phone_number, address FROM passengers")
            passengers = cur.fetchall()
            con.close()
            return passengers
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error fetching passenger details: {e}")
        return []

# Function to handle form submission and database update
def submit_details():
    global entry_first_name, entry_last_name, entry_dob, entry_gender, entry_email, entry_phone_number, entry_address

    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    dob = entry_dob.get()
    gender = entry_gender.get()
    email = entry_email.get()
    phone_number = entry_phone_number.get()
    address = entry_address.get()

    insert_passenger_details(first_name, last_name, dob, gender, email, phone_number, address)
    display_existing_passengers()

# Function to insert passenger details into MySQL database
def insert_passenger_details(first_name, last_name, dob, gender, email, phone_number, address):
    try:
        con = connect_to_database()
        if con:
            cur = con.cursor()
            query = "INSERT INTO passengers (first_name, last_name, dob, gender, email, phone_number, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cur.execute(query, (first_name, last_name, dob, gender, email, phone_number, address))
            con.commit()
            messagebox.showinfo("Success", "Passenger details added successfully!")
            con.close()
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error adding passenger details: {e}")

# Create main tkinter window
root = tk.Tk()
root.title("Passenger Details")

# Set window size and position
window_width = 1500  # Total window width
window_height = 500  # Window height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Text label above the data entry area
entry_label = tk.Label(root, text="Please fill out the new passenger details:")
entry_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Frame for data entry area
entry_frame = tk.Frame(root)
entry_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Create and place labels and entry widgets for passenger details
fields = ["First Name", "Last Name", "Date of Birth (YYYY-MM-DD)", "Gender", "Email", "Phone Number", "Address"]
entries = []

for i, field in enumerate(fields):
    tk.Label(entry_frame, text=field + ":").grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(entry_frame)
    entry.grid(row=i, column=1, padx=10, pady=5)

    # Assign entry widgets to global variables
    if field == "First Name":
        entry_first_name = entry
    elif field == "Last Name":
        entry_last_name = entry
    elif field == "Date of Birth (YYYY-MM-DD)":
        entry_dob = entry
    elif field == "Gender":
        entry_gender = entry
    elif field == "Email":
        entry_email = entry
    elif field == "Phone Number":
        entry_phone_number = entry
    elif field == "Address":
        entry_address = entry

# Create and place the submit button within the entry frame
submit_button = tk.Button(entry_frame, text="Submit", command=submit_details)
submit_button.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

# Text label above the result area
result_label = tk.Label(root, text="These are the existing passengers in the database:")
result_label.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="nsew")

# Frame for result area
result_frame = tk.Frame(root)
result_frame.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky="nsew")

# Create Treeview widget to display passenger details
tree = ttk.Treeview(result_frame, columns=["ID"] + fields, show="headings")
tree.grid(row=0, column=0, sticky="nsew")

# Define column widths for the Treeview
tree.column("ID", width=50, anchor=tk.CENTER)  # ID column width
field_width = (window_width * 2 // 3 - 50) // len(fields)  # Width for other columns
for field in fields:
    tree.column(field, width=field_width, anchor=tk.CENTER)

# Define column headings for the Treeview
tree.heading("ID", text="ID")
for field in fields:
    tree.heading(field, text=field)

# Function to display existing passenger details in the Treeview widget
def display_existing_passengers():
    # Clear existing data in the Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Retrieve existing passenger details from database
    passengers = display_passengers()

    # Insert retrieved data into the Treeview
    for passenger in passengers:
        tree.insert("", "end", values=passenger)

# Display existing passenger details initially
display_existing_passengers()

# Configure grid weights for responsive layout
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

# Start the main event loop
root.mainloop()
