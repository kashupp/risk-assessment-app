import tkinter as tk
from tkinter import messagebox
from app import assess_risk


def calculate_risk():
    try:
        numbers = []

        # Read the five input values
        for entry in entries:
            value = float(entry.get())
            numbers.append(value)

        # Calculate total and risk
        total = sum(numbers)
        result = assess_risk(numbers)

        # Display total
        sum_label.config(text=f"Model value: {total:g}")

        # Display result
        if result == "RISK":
            result_label.config(
                text="Patient is classified as HIGH RISK",
                fg="red"
            )
        else:
            result_label.config(
                text="Patient is classified as LOW RISK",
                fg="green"
            )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter exactly 5 valid features."
        )


def clear_fields():
    for entry in entries:
        entry.delete(0, tk.END)

    sum_label.config(text="Total Sum: ")
    result_label.config(text="Result: ", fg="black")


# Create main window
root = tk.Tk()
root.title("An example Risk Assessment Application")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg="#eef2f7")

# Heading
title_label = tk.Label(
    root,
    text="RISK ASSESSMENT",
    font=("Arial", 22, "bold"),
    bg="#eef2f7",
    fg="#183153"
)
title_label.pack(pady=25)

# Instructions
instruction_label = tk.Label(
    root,
    text="Enter values of five features below",
    font=("Arial", 12),
    bg="#eef2f7"
)
instruction_label.pack(pady=5)

# Input frame
input_frame = tk.Frame(root, bg="#eef2f7")
input_frame.pack(pady=15)

entries = []

for i in range(5):
    label = tk.Label(
        input_frame,
        text=f"Feature {i + 1}:",
        font=("Arial", 12),
        bg="#eef2f7"
    )
    label.grid(row=i, column=0, padx=10, pady=8)

    entry = tk.Entry(
        input_frame,
        font=("Arial", 12),
        width=20,
        justify="center"
    )
    entry.grid(row=i, column=1, padx=10, pady=8)

    entries.append(entry)

# Calculate button
calculate_button = tk.Button(
    root,
    text="CALCULATE RISK",
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="black",
    width=20,
    command=calculate_risk
)
calculate_button.pack(pady=15)

# Clear button
clear_button = tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 11),
    width=15,
    command=clear_fields
)
clear_button.pack(pady=5)

# Sum display
sum_label = tk.Label(
    root,
    text="Model calculations: ",
    font=("Arial", 15, "bold"),
    bg="#eef2f7"
)
sum_label.pack(pady=15)

# Result display
result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 20, "bold"),
    bg="#eef2f7"
)
result_label.pack(pady=10)

# Start application
root.mainloop()