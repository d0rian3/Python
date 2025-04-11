import customtkinter as ctk
import random
from tkinter import messagebox


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")


options = {
    'Камень': 1,
    'Ножницы': 2,
    'Бумага': 3
}


app = ctk.CTk()
app.title("Камень, Ножницы, Бумага")
app.geometry("400x400")
app.resizable(True, True)

title_label = ctk.CTkLabel(app, text="Камень ✊\nНожницы ✌\nБумага 🖐", font=ctk.CTkFont(size=20, weight="bold"))
title_label.pack(pady=20)

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

for option in options:
    btn = ctk.CTkButton(button_frame, text=option, width=120, height=40, font=ctk.CTkFont(size=16))
    btn.pack(pady=8)


result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=16), justify="center")
result_label.pack(pady=30)

# Запуск
app.mainloop()


