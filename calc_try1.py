import customtkinter as ctk

# --- Logic Functions ---
expression = ""


def on_click(char):
    global expression

    if char == "C":
        expression = ""
    elif char == "del":
        expression = expression[:-1]
    elif char == "=":
        try:
            # Calculate the result
            expression = str(eval(expression))
        except:
            expression = "Error"
    else:
        expression += str(char)

    # Update the entry widget
    entry.delete(0, "end")
    entry.insert(0, expression)


# --- UI Setup ---
root = ctk.CTk()
root.title("Modern Calc")
root.geometry("300x450")
root.resizable(False, False)

ctk.set_appearance_mode("dark")

# Display Screen
entry = ctk.CTkEntry(
    root,
    placeholder_text="0",
    justify="right",
    font=("Arial", 32),
    height=80,
    fg_color="transparent",
    border_width=0
)
entry.pack(fill="x", padx=10, pady=20)

# Buttons Frame
btn_frame = ctk.CTkFrame(root, fg_color="transparent")
btn_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Button Layout
buttons = [
    'C', '%', '/', 'del',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '.', '='
]

row, col = 0, 0

for button in buttons:
    # Logic to handle button colors
    is_num = button.isdigit() or button == "."
    color = "#3b3b3b" if is_num else "#2b2b2b"
    if button == "=": color = "#1f6aa5"

    # Create the button
    # We use a default argument (x=button) in the lambda to "capture" the current value
    btn = ctk.CTkButton(
        btn_frame,
        text=button,
        width=60,
        height=60,
        fg_color=color,
        font=("Arial", 18, "bold"),
        command=lambda x=button: on_click(x)
    )

    # Grid Logic
    if button == "0":
        btn.grid(row=row, column=col, columnspan=2, padx=5, pady=5, sticky="nsew")
        col += 1
    else:
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()