import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    age = age_entry.get().strip()
    gender = gender_var.get()

    if not name or not email or not age or gender == "Select":
        messagebox.showerror("Input Error", "Please fill out all fields correctly.")
        return
    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Age Error", "Please enter a valid age.")
        return

    messagebox.showinfo("Registration Successful", f"Welcome, {name}!\nEmail: {email}\nAge: {age}\nGender: {gender}")
    clear_fields()

def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("Select")


root = tk.Tk()
root.title("Registration Form")
root.geometry("380x280")
root.resizable(False, False)
root.configure(bg="#f0f8ff")

label_font = ("Segoe UI", 10)
entry_font = ("Segoe UI", 10)


tk.Label(root, text="Name:", font=label_font, bg="#f0f8ff").place(x=30, y=30)
name_entry = tk.Entry(root, width=30, font=entry_font)
name_entry.place(x=120, y=30)

tk.Label(root, text="Email:", font=label_font, bg="#f0f8ff").place(x=30, y=70)
email_entry = tk.Entry(root, width=30, font=entry_font)
email_entry.place(x=120, y=70)

tk.Label(root, text="Age:", font=label_font, bg="#f0f8ff").place(x=30, y=110)
age_entry = tk.Entry(root, width=30, font=entry_font)
age_entry.place(x=120, y=110)

tk.Label(root, text="Gender:", font=label_font, bg="#f0f8ff").place(x=30, y=150)
gender_var = tk.StringVar(value="Select")
gender_options = ["Select", "Male", "Female", "Other"]
gender_menu = tk.OptionMenu(root, gender_var, *gender_options)
gender_menu.config(width=26, font=entry_font)
gender_menu.place(x=120, y=145)


submit_btn = tk.Button(root, text="Submit", command=submit_form, bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), width=20)
submit_btn.place(x=100, y=210)

root.mainloop()
