from tkinter import Label, Tk
import time

# Configure the main window
root = Tk()
root.title("Digital Clock")
root.geometry("500x300")  # Adjusted window size
root.resizable(False, False)
root.configure(bg="black")

# Create labels for displaying time and date
time_label = Label(root, text="", font=("Arial", 40, "bold"), bg="black", fg="white")
time_label.pack(anchor="center", pady=20)

date_label = Label(root, text="", font=("Arial", 20, "bold"), bg="black", fg="white")
date_label.pack(anchor="center", pady=10)

# Function to update time
def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)  # Updates every 1 second

# Function to update date
def update_date():
    current_date = time.strftime("%A, %d %B %Y")
    date_label.config(text=current_date)
    date_label.after(60000, update_date)  # Updates every 1 minute

# Initialize time and date updates
update_time()
update_date()

# Run the application
root.mainloop()
