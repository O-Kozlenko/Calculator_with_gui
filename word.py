import customtkinter
import customtkinter as ctk

#Appearance
root = ctk.CTk()
root.title("Word 2.0")
root.geometry("500x500")
root.resizable(width=False, height=False)
ctk.set_appearance_mode("light")

#Commands
def option_menu_event(choice):
    text_area.configure(font=choice)

def switch_event():
    current_mode = switch_var.get()
    ctk.set_appearance_mode(current_mode)
    switch.configure(text="Mode: "+current_mode)

def slider_event(value):
    text_area.configure(font=value)

# UI Elements

#Option menu
option_menu = ctk.CTkOptionMenu(
    root,
    values=["Arial", "Courier","Times New Roman"],
    command=option_menu_event
)
option_menu.pack(side="top", anchor="nw", padx=10, pady=10)

#Switch
switch_var = ctk.StringVar(value="light")
switch = ctk.CTkSwitch(root,
                       text="Mode: light",
                       command=switch_event,
                       variable=switch_var,
                       onvalue="dark", offvalue="light")
switch.pack(side="top", anchor="nw", padx=2, pady=2)

#Text box
text_area = ctk.CTkTextbox(root, width=480, height=400, font=("Arial", 14))
text_area.pack(padx=5, pady=5)

#Slider


root.mainloop()