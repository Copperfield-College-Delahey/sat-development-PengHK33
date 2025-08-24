# GuiAddCompany.py:
import customtkinter as ctk
from Invoice import Company
import json, os                       
from AiUserandDatastorage import USER_DATA_DIR
from tkinter import messagebox


class AddCompanyPage(ctk.CTkFrame):
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

        # Main frame box
        mainBox = ctk.CTkFrame(self, corner_radius=15, width=600, height=600)
        mainBox.grid(row=1, column=1)
        mainBox.grid_propagate(False)
        mainBox.grid_columnconfigure(0, weight=1)
        mainBox.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

        # Title (left-aligned)
        newCompanyTitle = ctk.CTkLabel(mainBox, text="Add New Company:", font=("Aptos", 24, "bold"), anchor="w", justify="left")
        newCompanyTitle.grid(row=0, column=0, padx=30, pady=(15, 5), sticky="w")

        # Company Name
        CompanNameLabel = ctk.CTkLabel(mainBox, text="Company Name:", font=("Aptos", 13))
        CompanNameLabel.grid(row=1, column=0, sticky="w", padx=30, pady=(5, 0))
        self.companyNameEntry = ctk.CTkEntry(mainBox, width=290)
        self.companyNameEntry.grid(row=2, column=0, padx=30, pady=(0, 10), sticky="w")

        # Company Email
        companyEmailLabel = ctk.CTkLabel(mainBox, text="Company Email address:", font=("Aptos", 13))
        companyEmailLabel.grid(row=3, column=0, sticky="w", padx=30, pady=(5, 0))
        self.companyEmailEntry = ctk.CTkEntry(mainBox, width=290)
        self.companyEmailEntry.grid(row=4, column=0, padx=30, pady=(0, 10), sticky="w")

        #  
        sheetIdLabel = ctk.CTkLabel(mainBox, text="Google Sheet ID:", font=("Aptos", 13))
        sheetIdLabel.grid(row=5, column=0, sticky="w", padx=30, pady=(5, 0))
        self.sheetIdEntry = ctk.CTkEntry(mainBox, width=290)
        self.sheetIdEntry.grid(row=6, column=0, padx=30, pady=(0, 10), sticky="w")

        # Back Button
        cancelButton = ctk.CTkButton(mainBox, text="Cancel", width=80, command=self.controller.showMain)
        cancelButton.grid(row=7, column=0, padx=30, pady=(15, 10), sticky="w")

        # Submit Button
        submitButton = ctk.CTkButton(mainBox, text="Submit", width=80, command=self.saveCompanyInfo)
        submitButton.grid(row=7, column=1, padx=30, pady=(15, 10), sticky="w")

    def saveCompanyInfo(self):
        name = self.companyNameEntry.get().strip()
        email = self.companyEmailEntry.get().strip()
        sheet_id = self.sheetIdEntry.get().strip()

        if not name or not email or not sheet_id:
            messagebox.showerror("Error", "All fields must be filled in.")
            return

        newCompany = Company(name, email, sheet_id)

        # --- Load users ---
        if os.path.exists("users.json"):
            with open("users.json", "r") as f:
                users = json.load(f)
        else:
            users = {}

        if self.controller.current_user:
            user_data = users.setdefault(self.controller.current_user, {
                "password": "",
                "invoices": [],
                "companies": []
            })
            user_data.setdefault("companies", [])
            user_data["companies"].append({
                "name": newCompany.name,
                "email": newCompany.email,
                "googleSheetId": newCompany.googleSheetId
            })

            # --- Save back ---
            with open("users.json", "w") as f:
                json.dump(users, f, indent=4)

        messagebox.showinfo("Success", f"Company {name} saved!")
        self.controller.mainPage.load_companies()
        self.controller.showMain()  # refresh dropdown