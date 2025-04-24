import tkinter as tk

# Function to update the label with user input
def display_text():
    user_input = entry.get()
    output_label.config(text=f"You entered: {user_input}")

# Create the main window
root = tk.Tk()
root.title("Text Display GUI")
root.geometry("350x180")
root.configure(bg="#f0f8ff")  # Light blue background

# Create a text widget 
entry = tk.Entry(root, width=30, fg="#333", bg="#e6f2ff", relief="solid", borderwidth=1)
entry.pack(pady=10)

# Create a button
submit_button = tk.Button(
    root,
    text="Submit",
    command=display_text,
    fg="white",
    bg="#007acc",
    activebackground="#005f99",
    activeforeground="White",
    relief="raised",
    borderwidth=3
)
submit_button.pack(pady=5)

# Label to display 
output_label = tk.Label(root, text="", bg="#f0f8ff", fg="#004466", font=("Arial", 12))
output_label.pack(pady=10)

# Run main
root.mainloop()