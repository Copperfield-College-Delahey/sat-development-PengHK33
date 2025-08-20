import customtkinter as ctk
from tkinter import messagebox
import os
from AiUserandDatastorage import UserManager, USERS_FILE

class LoginPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.manager = UserManager()  
        print("DEBUG: Inside logIn, manager =", getattr(self, "manager", None))# 
        self.grid(row=0, column=0, sticky="nsew")

        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

        mainBox = ctk.CTkFrame(self, corner_radius=10, width=400, height=400)
        mainBox.grid(row=1, column=1)
        mainBox.grid_propagate(False)
        mainBox.grid_columnconfigure(0, weight=1)
        mainBox.grid_rowconfigure(tuple(range(8)), weight=1)

        logInTitle = ctk.CTkLabel(mainBox, text="Log in:", font=("Aptos", 24, "bold"), anchor="w")
        logInTitle.grid(row=0, column=0, padx=30, pady=(15, 5), sticky="w")

        LogInLabel = ctk.CTkLabel(mainBox, text="Email:", font=("Aptos", 13))
        LogInLabel.grid(row=1, column=0, sticky="w", padx=30)
        self.LogInEntry = ctk.CTkEntry(mainBox, width=290)
        self.LogInEntry.grid(row=2, column=0, padx=30, pady=(0, 10), sticky="w")

        passwordAddressLabel = ctk.CTkLabel(mainBox, text="Password:", font=("Aptos", 13))
        passwordAddressLabel.grid(row=3, column=0, sticky="w", padx=30)
        self.passwordEntry = ctk.CTkEntry(mainBox, width=290, show="*")  # ✅ Masked
        self.passwordEntry.grid(row=4, column=0, padx=30, pady=(0, 10), sticky="w")

        linkRow = ctk.CTkFrame(mainBox, fg_color="transparent")
        linkRow.grid(row=5, column=0, sticky="ew", padx=30)
        linkRow.grid_columnconfigure((0,1), weight=1)

        createAccountButton = ctk.CTkLabel(linkRow, text="Create Account", text_color="#1E90FF", cursor="hand2")
        createAccountButton.grid(row=0, column=0, sticky="w")
        createAccountButton.bind("<Button-1>", lambda e: self.controller.showCreateAccount())

        forgotPasswordButton = ctk.CTkLabel(linkRow, text="Forgot Password?", text_color="#1E90FF", cursor="hand2")
        forgotPasswordButton.grid(row=0, column=1, sticky="e")

        logInButton = ctk.CTkButton(mainBox, text="Log In", width=80, command=self.logIn)
        logInButton.grid(row=6, column=0, padx=30, pady=(15, 10), sticky="w")

    def logIn(self):
        print("DEBUG: Inside logIn, manager =", getattr(self, "manager", None))
        email = self.LogInEntry.get().strip()
        password = self.passwordEntry.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "Please enter both email and password.")
            return

        if not os.path.exists(USERS_FILE):
            messagebox.showerror("Error", "No accounts found. Please create an account first.")
            return

        user = self.manager.get_user(email)
        if not user:
            messagebox.showerror("Error", "Account does not exist.")
            return

        if not user.check_password(password):
            messagebox.showerror("Error", "Incorrect password.")
            return

        self.controller.current_user = user  # ✅ Always a User object
        messagebox.showinfo("Success", f"Logged in as {email}")
        self.controller.mainPage.load_companies()
        self.controller.showMain()
