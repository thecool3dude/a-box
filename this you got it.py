import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("do you?")

# Create a label to display the text
label = tk.Label(window, text="do you want to run\nYes or No?")
label.pack(pady=10)

# Create buttons for "Yes" and "No"
yes_button = tk.Button(window, text="Yes", command=lambda: print("lets gooooooooooooooo "))
yes_button.pack(side=tk.LEFT, padx=20)

no_button = tk.Button(window, text="No", command=lambda: print("why not :( )"))
no_button.pack(side=tk.RIGHT, padx=20)

# Start the application
window.mainloop()