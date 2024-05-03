import tkinter as tk
import addPassengersVertical5


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

def open_add_passenger():
    addPassengersVertical5.main()  # Call the main function from addPassengersVertical5 module

# Create the main Tkinter window
root = tk.Tk()
root.title("Main Window")

# Add a label to the main window for visible content
tk.Label(root, text="Welcome to the Main Window", font=("Helvetica", 16)).pack(pady=50)

# Create a menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create a "Windows" menu with options to open different windows
windows_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Windows", menu=windows_menu)
windows_menu.add_command(label="Window 1", command=open_window1)
windows_menu.add_command(label="Window 2", command=open_window2)
windows_menu.add_command(label="Window 3", command=open_window3)

# Create a "Trip" menu with options related to trip details
trip_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Trip", menu=trip_menu)
trip_menu.add_command(label="View Trip", command=open_window1)
trip_menu.add_command(label="Add Trip", command=open_window2)
trip_menu.add_command(label="Edit Trip", command=open_window3)

# Create a "Passenger" menu with options related to passengers
passenger_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Passenger", menu=passenger_menu)
passenger_menu.add_command(label="View/Add Passenger", command=open_add_passenger)
passenger_menu.add_command(label="Edit Passenger", command=open_window2)
passenger_menu.add_command(label="Delete Passenger", command=open_window3)

# Start the main event loop
root.mainloop()
