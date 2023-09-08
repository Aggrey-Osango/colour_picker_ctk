import customtkinter as ctk
from tkinter import *

# app configuration
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

# vars
framex, framey = 590, 510
pad_x, pad_y, c_radius = 10, 10, 10
widthx, heighty = 170, 35
mid = 0.5

prompt = """
    Which Colour do you Like?
"""

# Root window
root = ctk.CTk ()
root.geometry ("600x520")
root.title ("Helium Notes")

# frame.
frame = ctk.CTkFrame(master = root, width = framex, height = framey, corner_radius = c_radius,)

# label
label = ctk.CTkLabel (master = frame, width = widthx, height = heighty,
                      corner_radius = c_radius, text = prompt, bg_color = "black", fg_color = "white")


option = StringVar (value = " ")
def toggle_red ():
    if radial_01.cget("state"):
        radial_02.deselect()
        radial_03.deselect()
        option.set("You Picked Red")
        radial_01.configure(fg_color = "red")

def toggle_green():
    if radial_02.cget("state"):
        radial_01.deselect()
        radial_03.deselect()
        option.set("You Picked Green")
        radial_02.configure(fg_color = "green")

def toggle_blue():
    if radial_03.cget("state"):
        radial_01.deselect()
        radial_02.deselect()
        option.set("You Picked Blue")
        radial_03.configure(fg_color = "blue")


# Radial Buttons
radial_01 = ctk.CTkRadioButton (master = frame, text = "Red", command = toggle_red)
radial_02 = ctk.CTkRadioButton (master = frame, text = "Green", command = toggle_green)
radial_03 = ctk.CTkRadioButton (master = frame, text = "Blue", command = toggle_blue)

# label
msg_box = ctk.CTkLabel(master = frame, width = widthx, height = heighty, corner_radius = c_radius, textvariable = option)


frame.pack(padx=pad_x, pady=pad_y)
label.place(relx = mid, rely = 0.4, anchor = CENTER)
radial_01.place(relx=mid, rely=0.5, anchor = CENTER)
radial_02.place(relx=mid, rely=0.6, anchor = CENTER)
radial_03.place(relx=mid, rely=0.7, anchor = CENTER)
msg_box.place (relx=mid, rely=0.8, anchor = CENTER)
if __name__ == '__main__':
    root.mainloop()

