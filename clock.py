from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    # Get the current time in the specified format
    string = strftime("%H:%M:%S %p")

    # Update the label text
    label.config(text=string)

    # Call the time function again after 1000 milliseconds (1 second)
    label.after(1000, time)

# Create a label widget for displaying the time
label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')

# Initial call to the time function to start the clock
time()

# Start the Tkinter event loop
mainloop()
