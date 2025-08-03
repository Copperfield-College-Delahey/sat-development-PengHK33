import customtkinter as ctk

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
        createAccountTitle = ctk.CTkLabel(mainBox, text="Create Acco", font=("Aptos", 24, "bold"), anchor="w", justify="left")
        createAccountTitle.grid(row=0, column=0, padx=30, pady=(15, 5), sticky="w")

        # Add email for account
        addNewEmailLabel = ctk.CTkLabel(mainBox, text="Email Address:", font=("Aptos", 13))
        addNewEmailLabel.grid(row=1, column=0, sticky="w", padx=30, pady=(5, 0))
        addNewEmailEntry = ctk.CTkEntry(mainBox, width=290)
        addNewEmailEntry.grid(row=2, column=0, padx=30, pady=(0, 10), sticky="w")

        # Create Password
        createPasswordLabel = ctk.CTkLabel(mainBox, text="Password:", font=("Aptos", 13))
        createPasswordLabel.grid(row=3, column=0, sticky="w", padx=30, pady=(5, 0))
        createPasswordEntry = ctk.CTkEntry(mainBox, width=290)
        createPasswordEntry.grid(row=4, column=0, padx=30, pady=(0, 10), sticky="w")

        # Back Button (go back to Login page)
        backButton = ctk.CTkButton(mainBox, text="Back", width=80, command=self.controller.show_login)
        backButton.grid(row=7, column=0, padx=30, pady=(15, 10), sticky="w")

        # Submit Button (after creating account go to Main page)
        submitButton = ctk.CTkButton(mainBox, text="Submit", width=80, command=self.controller.show_main)
        submitButton.grid(row=7, column=1, padx=30, pady=(15, 10), sticky="w")
