import sys
import tkinter as tk
from tkinter import messagebox
import os




def getUserdetails():
    if len(sys.argv) < 7:  # Check if enough command-line arguments are provided
        print("Insufficient command-line arguments.")
        return None

    user_id = sys.argv[1]
    first_name = sys.argv[2]
    last_name = sys.argv[3]
    username = sys.argv[4]
    password = sys.argv[5]
    status = sys.argv[6]

    return {
        'user_id': user_id,
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
        'password': password,
        'status': status
    }



# Simulated user roles (you can replace this with actual user roles from your authentication system)
USER_ROLES = {
    '1': {  # Admin
        'passenger_management': True,
        'trip_management': True,
        'window1_access': True,
        'window2_access': True,
        'window3_access': True,
        'administrator_management': True
    },
    '2': {  # Trip Manager
        'passenger_management': True,
        'trip_management': True,
        'window1_access': True,
        'window2_access': True,
        'window3_access': False,
        'administrator_management': False

    },
    '3': {  # Trip Coordinator
        'passenger_management': True,
        'trip_management': True,
        'window1_access': True,
        'window2_access': True,
        'window3_access': False,
        'administrator_management': False

    },
    '4': {  # Passenger
        'passenger_management': True,
        'trip_management': True,
        'window1_access': True,
        'window2_access': True,
        'window3_access': False,
        'administrator_management': False

    }
}

def open_window1():
    if not hasattr(open_window1, "window"):
        open_window1.window = tk.Toplevel(root)
        open_window1.window.title("Window 1")
        open_window1.window.geometry("300x200")
        tk.Label(open_window1.window, text="This is Window 1").pack(padx=20, pady=50)
    else:
        open_window1.window.lift()

def open_window2():
    if not hasattr(open_window2, "window"):
        open_window2.window = tk.Toplevel(root)
        open_window2.window.title("Window 2")
        open_window2.window.geometry("300x200")
        tk.Label(open_window2.window, text="This is Window 2").pack(padx=20, pady=50)
    else:
        open_window2.window.lift()

def open_window3():
    if not hasattr(open_window3, "window"):
        open_window3.window = tk.Toplevel(root)
        open_window3.window.title("Window 3")
        open_window3.window.geometry("300x200")
        tk.Label(open_window3.window, text="This is Window 3").pack(padx=20, pady=50)
    else:
        open_window3.window.lift()

def open_add_passenger_window():
    if USER_ROLES[current_user]['passenger_management']:
        os.system("python3 addPassengers.py")
    else:
        messagebox.showwarning("Access Denied", "You do not have permission to manage passengers.")

def open_edit_passenger_window():
    if USER_ROLES[current_user]['passenger_management'] and current_user != '4':
        os.system("python3 editPassenger.py")
    else:
        messagebox.showwarning("Access Denied", "You do not have permission to manage passengers.")



def open_delete_passenger_window():
    if USER_ROLES[current_user]['passenger_management'] and current_user not in ['3', '4']:
        # Allow delete except for users '3' (Trip Coordinator) and '4' (Passenger)
        os.system("python3 deletePassenger.py")
    else:
        messagebox.showwarning("Access Denied", "You do not have permission to manage passengers.")

def open_available_trips_window():
    if USER_ROLES[current_user]['trip_management']:
        os.system("python3 availableTrips.py")
    else:
        messagebox.showwarning("Access Denied", "You do not have permission to manage trips.")


def open_add_trip_window():
    if USER_ROLES[current_user]['trip_management']and current_user != '4':
        os.system("python3 addTrip.py")
    else:
        messagebox.showwarning("Access Denied", "You do not have permission to manage trips.")

def open_edit_trip_window():
    if USER_ROLES[current_user]['trip_management'] and current_user != '4':
        os.system("python3 editTrip.py")
    else:
        messagebox.showwarning("Access Denied", "You do not have permission to manage trips.")

def open_delete_trip_window():
    if current_user in ['1', '2']:  # Allow delete for Admin (user '1') and Trip Manager (user '2')
        os.system("python3 deleteTrip.py")
    else:
        messagebox.showwarning("Access Denied", "You do not have permission to delete trips.")


def open_userdatasite_window():
    os.system("python3 userdatasite.py")

def open_admin_window():
    if USER_ROLES[current_user]['administrator_management'] and current_user not in ['3', '4']:
        # Allow delete except for users '3' (Trip Coordinator) and '4' (Passenger)
        os.system("python3 userdatasite.py")
    else:
        messagebox.showwarning("Access Denied", "You do not have permission to manage users.")




user_details = getUserdetails()
current_user = user_details['status']
# # Simulated current user (you can replace this with the actual logged-in user)
# current_user = status  # Change this to '3', '2', or '1' to simulate different user roles

# Create the main Tkinter window
root = tk.Tk()
root.title("Main Window")
root.geometry("600x400")


# Add a label to the main window for visible content
tk.Label(root, text="Welcome to the Main Window", font=("Helvetica", 16)).pack(pady=50)

# Add a label to display the welcome message
welcome_label = tk.Label(root, text="", font=("Helvetica", 16))
welcome_label.pack(pady=50)


# Update the welcome label text with user details
user_details = getUserdetails()
if user_details:
    first_name = user_details['first_name']
    last_name = user_details['last_name']
    status = user_details['status']

    # Map status codes to role descriptions
    if status == '1':
        role = "Administrator"
    elif status == '2':
        role = "Trip Manager"
    elif status == '3':
        role = "Trip Coordinator"
    else:
        role = "Visitor"

    welcome_message = (
        f"Welcome, {first_name} {last_name},\n"
        f"You can manage the system according to your authorization level.\n"
        f"You logged in as {role}!"
    )

    welcome_label.config(text=welcome_message)



# Create a menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create a "Windows" menu with options to open different windows
windows_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Windows", menu=windows_menu)
if USER_ROLES[current_user]['window1_access']:
    windows_menu.add_command(label="Window 1", command=open_available_trips_window)
windows_menu.add_separator()
if USER_ROLES[current_user]['window2_access']:
    windows_menu.add_command(label="Window 2", command=open_window2)
windows_menu.add_separator()
if USER_ROLES[current_user]['window3_access']:
    windows_menu.add_command(label="Create users", command=open_window3)

# Create a "Trip" menu with options for trip management
trip_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Trip", menu=trip_menu)
if USER_ROLES[current_user]['trip_management']:
    trip_menu.add_command(label="Add Trip", command=open_add_trip_window)
    trip_menu.add_separator()
    trip_menu.add_command(label="Edit Trip", command=open_edit_trip_window)
    if current_user != '4':  # Exclude 'Delete Trip' option for user '4' (Passenger)
        trip_menu.add_separator()
        trip_menu.add_command(label="Delete Trip", command=open_delete_trip_window)

# Create a "Passenger" menu with options for passenger management
passenger_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Passenger", menu=passenger_menu)
if USER_ROLES[current_user]['passenger_management']:
    passenger_menu.add_command(label="Add Passenger", command=open_add_passenger_window)
    passenger_menu.add_separator()
    passenger_menu.add_command(label="Edit Passenger", command=open_edit_passenger_window)
    if current_user != '3':  # Exclude 'Delete Passenger' option for user '3' (Trip Coordinator)
        passenger_menu.add_separator()
        passenger_menu.add_command(label="Delete Passenger", command=open_delete_passenger_window)

administrator_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Administrator", menu=administrator_menu)
if USER_ROLES[current_user]['administrator_management']:
    administrator_menu.add_command(label="Manage System Users", command=open_admin_window)
    administrator_menu.add_separator()

# Start the main event loop
root.mainloop()
