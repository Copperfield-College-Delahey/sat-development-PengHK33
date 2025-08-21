#GuiStartUpPage.py:
import customtkinter as ctk
import json
import os
from tkinter import messagebox
from Invoice import Company

USERS_FILE = "users.json"

class LoginPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        # Center the login box
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Login frame
        mainBox = ctk.CTkFrame(self, corner_radius=10, width=400, height=400)
        mainBox.grid(row=1, column=1)
        mainBox.grid_propagate(False)
        mainBox.grid_columnconfigure(0, weight=1)
        mainBox.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        # Title (left-aligned)
        logInTitle = ctk.CTkLabel(mainBox, text="Log in:", font=("Aptos", 24, "bold"), anchor="w", justify="left")
        logInTitle.grid(row=0, column=0, padx=30, pady=(15, 5), sticky="w")

        # Email
        LogInLabel = ctk.CTkLabel(mainBox, text="Email:", font=("Aptos", 13))
        LogInLabel.grid(row=1, column=0, sticky="w", padx=30, pady=(5, 0))
        self.LogInEntry = ctk.CTkEntry(mainBox, width=290)
        self.LogInEntry.grid(row=2, column=0, padx=30, pady=(0, 10), sticky="w")

        # Password
        passwordAddressLabel = ctk.CTkLabel(mainBox, text="Password:", font=("Aptos", 13))
        passwordAddressLabel.grid(row=3, column=0, sticky="w", padx=30, pady=(5, 0))
        self.passwordEntry = ctk.CTkEntry(mainBox, width=290)
        self.passwordEntry.grid(row=4, column=0, padx=30, pady=(0, 10), sticky="w")

        # Create Account and Forgot Password Text Buttons
        linkRow = ctk.CTkFrame(mainBox, fg_color="transparent")
        linkRow.grid(row=5, column=0, sticky="ew", padx=30)
        linkRow.grid_columnconfigure((0, 1), weight=1)

        createAccountButton = ctk.CTkLabel(linkRow, text="Create Account", text_color="#1E90FF", cursor="hand2")
        createAccountButton.grid(row=0, column=0, sticky="w")
        createAccountButton.bind("<Button-1>", lambda e: self.controller.showCreateAccount())

        forgotPasswordButton = ctk.CTkLabel(linkRow, text="Forgot Password?", text_color="#1E90FF", cursor="hand2")
        forgotPasswordButton.grid(row=0, column=1, sticky="e")

        # Submit Button (small, bottom left)
        logInButton = ctk.CTkButton(mainBox, text="Log In", width=80, command=self.logIn)
        logInButton.grid(row=6, column=0, padx=30, pady=(15, 10), sticky="w")
    
    import json

    def logIn(self):
        email = self.LogInEntry.get().strip()
        password = self.passwordEntry.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "Please enter both email and password.")
            return

        if not os.path.exists(USERS_FILE):
            messagebox.showerror("Error", "No accounts found. Please create an account first.")
            return

        with open(USERS_FILE, "r") as f:
            users = json.load(f)

        if email not in users:
            messagebox.showerror("Error", "Account does not exist.")
            return

        if users[email]["password"] != password:
            messagebox.showerror("Error", "Incorrect password.")
            return

        #  Load companies into memory
        companies_data = users[email].get("companies", [])
        self.controller.companyList = [
            Company(c["name"], c["email"], c["layout"]) for c in companies_data
        ]

        self.controller.current_user = email

        messagebox.showinfo("Success", f"Welcome back, {email}!")
        self.controller.showMain()