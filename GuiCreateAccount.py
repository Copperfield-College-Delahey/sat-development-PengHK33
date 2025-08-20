import customtkinter as ctk
import json
import os
from tkinter import messagebox
from AiUserandDatastorage import UserManager

USERS_FILE = "users.json"

class CreateAccountPage(ctk.CTkFrame):
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
        createAccountTitle = ctk.CTkLabel(mainBox, text="Create Account:", font=("Aptos", 24, "bold"), anchor="w", justify="left")
        createAccountTitle.grid(row=0, column=0, padx=30, pady=(15, 5), sticky="w")

        # Add email for account
        addNewEmailLabel = ctk.CTkLabel(mainBox, text="Email Address:", font=("Aptos", 13))
        addNewEmailLabel.grid(row=1, column=0, sticky="w", padx=30, pady=(5, 0))
        self.addNewEmailEntry = ctk.CTkEntry(mainBox, width=290)
        self.addNewEmailEntry.grid(row=2, column=0, padx=30, pady=(0, 10), sticky="w")

        # Create Password
        createPasswordLabel = ctk.CTkLabel(mainBox, text="Password:", font=("Aptos", 13))
        createPasswordLabel.grid(row=3, column=0, sticky="w", padx=30, pady=(5, 0))
        self.createPasswordEntry = ctk.CTkEntry(mainBox, width=290)
        self.createPasswordEntry.grid(row=4, column=0, padx=30, pady=(0, 10), sticky="w")

        # Back Button (go back to Login page)
        backButton = ctk.CTkButton(mainBox, text="Back", width=80, command=self.controller.showLogin)
        backButton.grid(row=7, column=0, padx=30, pady=(15, 10), sticky="w")

        # Submit Button (after creating account go to Main page)
        submitButton = ctk.CTkButton(mainBox, text="Submit", width=80, command=self.saveAccount)
        submitButton.grid(row=7, column=1, padx=30, pady=(15, 10), sticky="w")

    def saveAccount(self):
        email = self.addNewEmailEntry.get().strip()
        password = self.createPasswordEntry.get().strip()

        # --- Validation checks ---
        if not email or not password:
            messagebox.showerror("Error", "Please enter both email and password.")
            return

        # Email format check
        if "@" not in email:
            messagebox.showerror("Error", "Please enter a valid email address.")
            return

        # Password strength check
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long.")
            return
        if not any(char.isdigit() for char in password):
            messagebox.showerror("Error", "Password must contain at least one number.")
            return
        if not any(char.isupper() for char in password):
            messagebox.showerror("Error", "Password must contain at least one uppercase letter.")
            return
        
        #Use UserManager instead of writing JSON directly
        success = self.manager.add_user(email, password)
        if not success:
            messagebox.showerror("Error", "Account already exists!")
            return
        
        messagebox.showinfo("Success", f"Account created for {email}")
        self.controller.showLogin()