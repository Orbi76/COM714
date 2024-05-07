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


def display_existing_trips():
    for row in tree.get_children():
        tree.delete(row)

    trips = display_trips()

    for trip in trips:
        tree.insert("", "end", values=trip)

root = tk.Tk()
root.title("Available Trips")

window_width = 1300
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

fields = [
    "Country", "City", "Type of Travel", "Duration (days)",
    "Meal", "Type of Accommodation", "Optional Program",
    "Start Date", "End Date", "Participants"
]



result_label = tk.Label(root, text="Existing Trips in the Database:")
result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

result_frame = tk.Frame(root)
result_frame.grid(row=1, column=2, columnspan=4, padx=10, pady=10, sticky="nsew")

tree = ttk.Treeview(result_frame, columns=["ID"] + fields, show="headings")
tree.grid(row=0, column=0, sticky="nsew")

tree.column("ID", width=50, anchor=tk.CENTER)
field_width = (window_width * 2 // 3 - 50) // len(fields)
for field in ["ID"] + fields:
    tree.column(field, width=field_width, anchor=tk.CENTER)
    tree.heading(field, text=field)

display_existing_trips()


root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.mainloop()
