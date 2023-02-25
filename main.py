#imports
import customtkinter as ctk

#Functions
def login():
  print("Test")

#user interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x350")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

LoginLBL = ctk.CTkLabel(master=frame, text="Login System")
LoginLBL.pack(pady=12, padx=10)

UsrnENT = ctk.CTkEntry(master=frame, placeholder_text="Username")
UsrnENT.pack(pady=12, padx= 10)
PswrdENT = ctk.CTkEntry(master=frame, placeholder_text="Password", show="O")
PswrdENT.pack(pady=12, padx= 10)

LoginBTN = ctk.CTkButton(master=frame, text="Login", command=login)
LoginBTN.pack(pady=12, padx=10)

RmbrCHK = ctk.CTkCheckBox(master=frame, text="Remember Me")
RmbrCHK.pack(pady=12, padx=10)
root.mainloop()