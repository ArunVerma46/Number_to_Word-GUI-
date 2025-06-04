import tkinter as tk
from tkinter import messagebox
import inflect

# inflect engine create karo
p = inflect.engine()

# Convert karne ka function
def convert_number():
    num = entry.get()
    if num.isdigit():
        word = p.number_to_words(num)
        result_label.config(text="In words: " + word.capitalize())
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# Main Window
root = tk.Tk()
root.title("Number to Word Converter")
root.geometry("400x250")
root.config(bg="#f0f0f0")

# Title Label
title = tk.Label(root, text="Number to Word Converter", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
title.pack(pady=10)

# Entry field
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

# Convert button
convert_btn = tk.Button(root, text="Convert", font=("Arial", 12), command=convert_number, bg="#4CAF50", fg="white", padx=10, pady=5)
convert_btn.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0", fg="#222")
result_label.pack(pady=10)

# Run the window
root.mainloop()
