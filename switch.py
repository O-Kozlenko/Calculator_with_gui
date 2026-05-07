import customtkinter

app = customtkinter.CTk()
app.geometry("400x150")
customtkinter.set_appearance_mode("light")

def switch_event():
    current_mode = switch_var.get()
    customtkinter.set_appearance_mode(current_mode)
    switch.configure(text=f"Mode: {current_mode}")

switch_var = customtkinter.StringVar(value="light")
switch = customtkinter.CTkSwitch(app, text="Mode: light", command=switch_event,
                                 variable=switch_var, onvalue="dark", offvalue="light")
switch.pack(side="top", anchor="nw", padx=2, pady=2)


def option_menu_callback(choice):
    if choice == "None":
        app.configure(fg_color=customtkinter.ThemeManager.theme["CTk"]["fg_color"])
    else:
        app.configure(fg_color=choice)

option_menu = customtkinter.CTkOptionMenu(app, values=["None","red", "orange","yellow","green","blue","purple"],
                                         command=option_menu_callback)
option_menu.set("Background color")
option_menu.pack(side="top", anchor="nw", padx=2, pady=2)

app.mainloop()