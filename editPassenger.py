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
selected_passenger_id = None  # Track selected passenger ID

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

# Function to handle form submission and database update (for both add and edit operations)
def submit_details():
    global entry_first_name, entry_last_name, entry_dob, entry_gender, entry_email, entry_phone_number, entry_address, selected_passenger_id

    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    dob = entry_dob.get()
    gender = entry_gender.get()
    email = entry_email.get()
    phone_number = entry_phone_number.get()
    address = entry_address.get()

    # Validate input data
    if not first_name or not last_name or not dob or not gender or not email or not phone_number or not address:
        messagebox.showerror("Error", "Please fill out all fields.")
        return

    # Perform additional validation (e.g., check email format, phone number format, etc.)
    if not validate_email(email):
        messagebox.showerror("Error", "Please enter a valid email address.")
        return

    if not validate_phone_number(phone_number):
        messagebox.showerror("Error", "Please enter a valid phone number.")
        return

    if selected_passenger_id:
        # Update existing passenger details
        update_passenger_details(selected_passenger_id, first_name, last_name, dob, gender, email, phone_number, address)
    else:
        # Insert new passenger details
        insert_passenger_details(first_name, last_name, dob, gender, email, phone_number, address)

    # Clear entry fields after submission
    clear_entry_fields()

    # Refresh displayed passengers
    display_existing_passengers()

# Function to insert new passenger details into MySQL database
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

# Function to update existing passenger details in MySQL database
def update_passenger_details(passenger_id, first_name, last_name, dob, gender, email, phone_number, address):
    try:
        con = connect_to_database()
        if con:
            cur = con.cursor()
            query = "UPDATE passengers SET first_name=%s, last_name=%s, dob=%s, gender=%s, email=%s, phone_number=%s, address=%s WHERE id=%s"
            cur.execute(query, (first_name, last_name, dob, gender, email, phone_number, address, passenger_id))
            con.commit()
            messagebox.showinfo("Success", "Passenger details updated successfully!")
            con.close()
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error updating passenger details: {e}")

# Function to validate email format
def validate_email(email):
    import re
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email)

# Function to validate phone number format
def validate_phone_number(phone_number):
    import re
    # Define the regular expression pattern for UK phone numbers
    # This pattern covers common UK phone number formats and enforces a length restriction
    phone_pattern = r"^(?:(?:\+44\s?|0)(?:\d{3}\s?\d{3}\s?\d{4}|\d{2}\s?\d{4}\s?\d{4}|\d{4}\s?\d{4}|\d{5}\s?\d{3}\s?\d{3}|\d{4}\s?\d{2}\s?\d{3}))$"

    # Define the desired minimum and maximum lengths for the phone number (excluding spaces)
    min_length = 10  # Minimum length (excluding spaces)
    max_length = 15  # Maximum length (excluding spaces)

    # Remove spaces from the phone number string
    phone_number_no_spaces = phone_number.replace(" ", "")

    # Check if the phone number matches the pattern and falls within the length range
    if (re.match(phone_pattern, phone_number) and
            min_length <= len(phone_number_no_spaces) <= max_length):
        return True
    else:
        return False

# Function to clear entry fields
def clear_entry_fields():
    global entry_first_name, entry_last_name, entry_dob, entry_gender, entry_email, entry_phone_number, entry_address, selected_passenger_id
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_gender.set("Male")  # Reset gender selection
    entry_email.delete(0, tk.END)
    entry_phone_number.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    selected_passenger_id = None  # Reset selected passenger ID

# Function to handle edit button click (populate entry fields with selected passenger details)
def handle_edit_passenger():
    global entry_first_name, entry_last_name, entry_dob, entry_gender, entry_email, entry_phone_number, entry_address, selected_passenger_id

    # Get selected passenger details from Treeview
    selected_item = tree.focus()  # Get item ID of selected row
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a passenger to edit.")
        return

    passenger_details = tree.item(selected_item, "values")
    if not passenger_details:
        messagebox.showwarning("Warning", "Invalid selection. Please try again.")
        return

    # Extract passenger details
    passenger_id, first_name, last_name, dob, gender, email, phone_number, address = passenger_details

    # Populate entry fields with selected passenger details
    entry_first_name.delete(0, tk.END)
    entry_first_name.insert(0, first_name)
    entry_last_name.delete(0, tk.END)
    entry_last_name.insert(0, last_name)
    entry_dob.delete(0, tk.END)
    entry_dob.insert(0, dob)
    entry_gender.set(gender)
    entry_email.delete(0, tk.END)
    entry_email.insert(0, email)
    entry_phone_number.delete(0, tk.END)
    entry_phone_number.insert(0, phone_number)
    entry_address.delete(0, tk.END)
    entry_address.insert(0, address)

    # Set selected passenger ID for update operation
    selected_passenger_id = passenger_id

# Create main tkinter window
root = tk.Tk()
root.title("Passenger Details")

# Set window size and position
window_width = 1300  # Total window width
window_height = 500  # Window height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Text label above the data entry area
entry_label = tk.Label(root, text="Please fill out the passenger details:")
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
        # Create an OptionMenu widget for Gender selection
        options = ["Male", "Female", "Other"]
        entry_gender = tk.StringVar(root)
        entry_gender.set(options[0])  # Default selection
        gender_menu = tk.OptionMenu(entry_frame, entry_gender, *options)
        gender_menu.grid(row=i, column=1, padx=10, pady=5, sticky="w")
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

# Button to edit selected passenger
edit_button = tk.Button(root, text="Edit Selected Passenger", command=handle_edit_passenger)
edit_button.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

# Configure grid weights for responsive layout
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

# Start the main event loop
root.mainloop()
