import tkinter as tk
from tkinter import messagebox
import hashlib
import base64
import os
import random
import string

# ----------------------- Hash Functions -----------------------

def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    digest = sha256.digest()
    return base64.b64encode(digest).decode('utf-8')

def verify_password(stored_hash, password):
    return stored_hash == hash_password(password)

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# ----------------------- Auth Logic -----------------------

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both username and password.")
        return

    if not os.path.exists('database.txt'):
        messagebox.showerror("Login Failed", "No registered users found. Please sign up first.")
        return

    with open('database.txt', 'r') as f:
        for line in f:
            stored_username, stored_hash = line.strip().split(',')
            if username == stored_username and verify_password(stored_hash, password):
                messagebox.showinfo("Login Success", f"Welcome back, {username}!")
                return

    messagebox.showerror("Login Failed", "Invalid username or password.")

def signup():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both username and password.")
        return

    hashed_password = hash_password(password)

    # Check if username already exists
    if os.path.exists('database.txt'):
        with open('database.txt', 'r') as f:
            for line in f:
                stored_username, _ = line.strip().split(',')
                if username == stored_username:
                    messagebox.showerror("Signup Failed", "Username already exists. Try a different one.")
                    return

    # Save new user
    with open('database.txt', 'a') as f:
        f.write(f"{username},{hashed_password}\n")

    messagebox.showinfo("Signup Success", "Account created successfully! You can now login.")

# ----------------------- GUI Setup -----------------------

mainwindow = tk.Tk()
mainwindow.title("Password Hasher App")
mainwindow.geometry("400x300")
mainwindow.config(bg="black")
mainwindow.resizable(True, False)

# Title
tk.Label(
    mainwindow,
    text="Login / Signup",
    font=("Arial", 18, "bold"),
    bg="black",
    fg="white"
).pack(pady=10)

# Username field
tk.Label(
    mainwindow,
    text="Username",
    font=("Arial", 12),
    bg="black",
    fg="white").pack(pady=(10, 0))
username_entry = tk.Entry(mainwindow, font=("Arial", 12))
username_entry.pack(pady=5)

# Password field
tk.Label(
    mainwindow,
    text="Password",
    font=("Arial", 12),
    bg="black",
    fg="white").pack(pady=(10, 0))
password_entry = tk.Entry(
    mainwindow,
    font=("Arial", 12),
    show="*")
password_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(
    mainwindow,
    bg="black")
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="Login",
    width=10,
    command=login,
    bg="#0bda51",
    fg="black").grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Signup",
    width=10,
    command=signup,
    bg="#1e90ff",
    fg="white").grid(row=0, column=1, padx=10)

mainwindow.mainloop()
