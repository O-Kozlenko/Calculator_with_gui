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
    size = int(slider.get())
    text_area.configure(font=(choice,size))

def switch_event():
    current_mode = switch_var.get()
    ctk.set_appearance_mode(current_mode)
    switch.configure(text="Mode: "+current_mode)

def slider_event(value):
    current_font = option_menu.get()
    text_area.configure(font=(current_font, value))

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
switch.pack(anchor="nw", padx=2, pady=2)

# Header Label
slider_title = ctk.CTkLabel(root,
                            text="Text Size",
                            font=("Arial", 12, "bold"))
slider_title.pack(anchor="nw", padx=10, pady=(10, 0))

#Slider
slider = customtkinter.CTkSlider(root,
                                 from_=8, to=48,
                                 command=slider_event)
slider.set(14)
slider.pack(anchor="n", padx=2, pady=2)

#Text box
text_area = ctk.CTkTextbox(root, width=480, height=400, font=("Arial", 14))
text_area.pack(padx=5, pady=5)

root.mainloop()