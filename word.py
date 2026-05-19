import customtkinter as ctk

# --- Appearance & Window Setup ---
root = ctk.CTk()
root.title("Word 2.0")
root.geometry("500x600")  # Adjusted height slightly to prevent UI overlap
root.resizable(width=False, height=False)
ctk.set_appearance_mode("light")


# --- Logic ---

def update_font(*args):
    """Handles all font and label text updates synchronously."""
    family = option_menu.get()
    size = int(slider.get())

    # Update the dynamic slider title label text
    slider_title.configure(text=f"Text Size: {size}")

    # Collect selected styles into a list
    styles = []
    if check_var_bold.get() == "bold":
        styles.append("bold")
    if check_var_italic.get() == "italic":
        styles.append("italic")
    if check_var_underline.get() == "underline":
        styles.append("underline")
    if check_var_overstrike.get() == "overstrike":
        styles.append("overstrike")

    # Default to "normal" if no checkboxes are selected
    if not styles:
        styles.append("normal")

    text_area.configure(font=(family, size, *styles))


def switch_event():
    current_mode = switch_var.get()
    ctk.set_appearance_mode(current_mode)
    switch.configure(text="Mode: " + current_mode)


# --- UI Elements ---

# Font Selection Menu
option_menu = ctk.CTkOptionMenu(
    root,
    values=["Arial", "Courier", "Times New Roman"],
    command=update_font
)
option_menu.place(x=5, y=5)

# Light/Dark Mode Switch
switch_var = ctk.StringVar(value="light")
switch = ctk.CTkSwitch(root,
                       text="Mode: light",
                       command=switch_event,
                       variable=switch_var,
                       onvalue="dark", offvalue="light")
switch.place(x=150, y=7)

# Dynamic Header Label (Fixed string concatenation error)
slider_title = ctk.CTkLabel(root,
                            text="Text Size: 14",
                            font=("Arial", 12, "bold"))
slider_title.place(x=8, y=35)

# Size Slider
slider = ctk.CTkSlider(root,
                       from_=8, to=48,
                       command=update_font)
slider.set(14)
slider.place(x=5, y=55)

# Check box (Bold)
check_var_bold = ctk.StringVar(value="normal")
checkbox_bold = ctk.CTkCheckBox(root,
                                text="Bold",
                                command=update_font,
                                variable=check_var_bold,
                                onvalue="bold", offvalue="normal")
checkbox_bold.place(x=10, y=85)

# Check box (Italic)
check_var_italic = ctk.StringVar(value="normal")
checkbox_italic = ctk.CTkCheckBox(root,
                                  text="Italic",
                                  command=update_font,
                                  variable=check_var_italic,
                                  onvalue="italic", offvalue="normal")
checkbox_italic.place(x=90, y=85)

check_var_underline = ctk.StringVar(value="normal")
checkbox_underline = ctk.CTkCheckBox(root,
                                  text="Underline",
                                  command=update_font,
                                  variable=check_var_underline,
                                  onvalue="underline", offvalue="normal")
checkbox_underline.place(x=160, y=85)

check_var_overstrike = ctk.StringVar(value="normal")
checkbox_overstrike = ctk.CTkCheckBox(root,
                                  text="Overstrike",
                                  command=update_font,
                                  variable=check_var_overstrike,
                                  onvalue="overstrike", offvalue="normal")
checkbox_overstrike.place(x=250, y=85)

# Text Editing Box
text_area = ctk.CTkTextbox(root, width=480, height=450, font=("Arial", 14))
text_area.place(x=10, y=125)

root.mainloop()