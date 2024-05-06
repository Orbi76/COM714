import tkinter as tk
from tkinter import ttk, messagebox
import pymysql


def connect_to_database():
    try:
        con = pymysql.connect(host='localhost', port=8889, user='root', password='root', database='com714')
        messagebox.showinfo("Success", "Connected to MySQL database!")
        return con
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error connecting to MySQL database: {e}")
        return None


def insert_trip_details(trip_details):
    try:
        con = connect_to_database()
        if con:
            cur = con.cursor()
            query = """
                INSERT INTO trips 
                (country, city, type_of_travel, duration_of_trip, meals, type_of_accommodation, optional_program, start_date, end_date, participants) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, trip_details)
            con.commit()
            messagebox.showinfo("Success", "Trip details added successfully!")
            con.close()
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error adding trip details: {e}")


def display_trips():
    try:
        con = connect_to_database()
        if con:
            cur = con.cursor()
            cur.execute("SELECT * FROM trips")
            trips = cur.fetchall()
            con.close()
            return trips
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error fetching trip details: {e}")
        return []


def submit_trip_details():
    country = entries["Country"].get()
    city = entries["City"].get()
    travel_type = entries["Type of Travel"].get()
    duration_days = entries["Duration (days)"].get()
    meal = entries["Meal"].get()
    accommodation_type = entries["Accommodation Type"].get()
    optional_program = entries["Optional Program"].get()
    start_date = entries["Start Date"].get()
    end_date = entries["End Date"].get()
    participants = entries["Participants"].get()

    trip_details = (
        country, city, travel_type, duration_days, meal, accommodation_type, optional_program, start_date, end_date,
        participants
    )

    insert_trip_details(trip_details)
    display_existing_trips()


def display_existing_trips():
    for row in tree.get_children():
        tree.delete(row)

    trips = display_trips()

    for trip in trips:
        tree.insert("", "end", values=trip)


root = tk.Tk()
root.title("Add Trip")

# Left Frame (Entry Fields)
left_frame = tk.Frame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Text label prompting the user to fill in trip details
prompt_label = tk.Label(left_frame, text="Please fill in the details of the trip!")
prompt_label.grid(row=0, column=0, columnspan=4, pady=5, sticky="we")

fields = [
    "Country", "City", "Type of Travel", "Duration (days)",
    "Meal", "Accommodation Type", "Optional Program",
    "Start Date", "End Date", "Participants"
]

# Dictionary to hold entry widgets
entries = {}

# Calculate number of rows needed based on half the length of fields list
num_rows = len(fields) // 2 + len(fields) % 2

for i, field in enumerate(fields):
    row = i % num_rows + 1
    column = (i // num_rows) * 2

    tk.Label(left_frame, text=field + ":").grid(row=row, column=column, padx=10, pady=5, sticky="e")

    if field == "Type of Travel":
        travel_type_options = ["Flight", "Cruise Ship", "Coach", "Train"]
        entry_travel_type = tk.StringVar(left_frame)
        entry_travel_type.set(travel_type_options[0])
        travel_type_menu = tk.OptionMenu(left_frame, entry_travel_type, *travel_type_options)
        travel_type_menu.grid(row=row, column=column + 1, padx=10, pady=5, sticky="ew")
        entries[field] = entry_travel_type

    elif field == "Meal":
        meal_options = ["Breakfast", "Half pension", "All inclusive", "None"]
        entry_meal = tk.StringVar(left_frame)
        entry_meal.set(meal_options[0])
        meal_menu = tk.OptionMenu(left_frame, entry_meal, *meal_options)
        meal_menu.grid(row=row, column=column + 1, padx=10, pady=5, sticky="ew")
        entries[field] = entry_meal

    elif field == "Accommodation Type":
        accommodation_options = ["Hotel", "Camping", "Guest House"]
        entry_accommodation_type = tk.StringVar(left_frame)
        entry_accommodation_type.set(accommodation_options[0])
        accommodation_menu = tk.OptionMenu(left_frame, entry_accommodation_type, *accommodation_options)
        accommodation_menu.grid(row=row, column=column + 1, padx=10, pady=5, sticky="ew")
        entries[field] = entry_accommodation_type

    else:
        entry = tk.Entry(left_frame)
        entry.grid(row=row, column=column + 1, padx=10, pady=5, sticky="ew")
        entries[field] = entry

# Submit Button
submit_button = tk.Button(left_frame, text="Create Trip", command=submit_trip_details)
submit_button.grid(row=num_rows + 1, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Right Frame (Display Area)
right_frame = tk.Frame(root)
right_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Text label above the result area
result_label = tk.Label(right_frame, text="Existing Trips in the Database:")
result_label.pack(pady=5)

# Treeview to display existing trips
tree = ttk.Treeview(right_frame, columns=["ID"] + fields, show="headings")
tree.pack(padx=10, pady=10, fill="both", expand=True)

# Define column widths and headings for the Treeview
tree.column("ID", width=50, anchor=tk.CENTER)
for field in ["ID"] + fields:
    tree.column(field, width=120, anchor=tk.CENTER)
    tree.heading(field, text=field)

# Display existing trips initially
display_existing_trips()

# Start the main event loop
root.mainloop()
