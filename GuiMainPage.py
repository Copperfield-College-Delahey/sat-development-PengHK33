# GuiMainPage.py
import customtkinter as ctk
from Invoice import Invoice, Company
import json, os                       
from AiUserandDatastorage import USER_DATA_DIR
from tkinter import messagebox

# --- Google Sheets setup ---
import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)


class MainPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        # configure app window grid
        self.grid_columnconfigure(0, weight=1)  # left column
        self.grid_columnconfigure(1, weight=1)  # right column
        self.grid_rowconfigure(0, weight=1)  # top bar
        self.grid_rowconfigure(1, weight=6)  # main content
        self.grid_rowconfigure(2, weight=1)  # footer

        # Top Frame
        topFrame = ctk.CTkFrame(self, border_width=0)
        topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        topFrame.grid_columnconfigure(0, weight=1)
        topFrame.grid_columnconfigure(1, weight=0)
        titleLabel = ctk.CTkLabel(topFrame, text="Innovate Invoice", font=("Aptos", 30))
        titleLabel.grid(row=0, column=0, sticky="w", padx=1, pady=1)

        previousButton = ctk.CTkButton(topFrame, text="Previous Invoices", command=self.controller.showPreviousInvoices)
        previousButton.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        # Bottom Frame
        bottomFrame = ctk.CTkFrame(self, border_width=0)
        bottomFrame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        bottomFrame.grid_columnconfigure(0, weight=1)
        bottomFrame.grid_columnconfigure(1, weight=1)

        submitButton = ctk.CTkButton(bottomFrame, text="Submit", command=self.getInvoiceData) 
        submitButton.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        backButton = ctk.CTkButton(bottomFrame, text="Back", command=self.controller.showLogin)
        backButton.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Entryfield Frame
        entryFieldFrame = ctk.CTkFrame(self, border_width=0)
        entryFieldFrame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        entryFieldFrame.grid_rowconfigure(0, weight=1)
        entryFieldFrame.grid_rowconfigure(1, weight=1)
        entryFieldFrame.grid_rowconfigure(2, weight=1)
        entryFieldFrame.grid_rowconfigure(3, weight=1)
        entryFieldFrame.grid_rowconfigure(4, weight=1)
        entryFieldFrame.grid_rowconfigure(5, weight=1)
        entryFieldFrame.grid_rowconfigure(6, weight=1)
        entryFieldFrame.grid_rowconfigure(7, weight=1)
        entryFieldFrame.grid_rowconfigure(8, weight=1)
        entryFieldFrame.grid_rowconfigure(9, weight=1)

        self.companyDropdown = ctk.CTkComboBox(entryFieldFrame, values=["No companies"])
        self.companyDropdown.grid(row=9, column=0, padx=10, pady=10, sticky="w")

        # Entryframe Entryfields
        self.poNumberEntry = ctk.CTkEntry(entryFieldFrame, width=200)
        self.poNumberEntry.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.jobAddressEntry = ctk.CTkEntry(entryFieldFrame, width=200)
        self.jobAddressEntry.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.UnitPriceEntry = ctk.CTkEntry(entryFieldFrame, width=200)
        self.UnitPriceEntry.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.SupervisorEntry = ctk.CTkEntry(entryFieldFrame, width=200)
        self.SupervisorEntry.grid(row=7, column=0, padx=10, pady=10, sticky="w")

        # Entryframe labels
        poNumberLabel = ctk.CTkLabel(entryFieldFrame, text="Po Number:", font=("Aptos", 12))
        poNumberLabel.grid(row=0, column=0, sticky="w", padx=1, pady=1)
        jobAddressLabel = ctk.CTkLabel(entryFieldFrame, text="Job Address:", font=("Aptos", 12))
        jobAddressLabel.grid(row=2, column=0, sticky="w", padx=1, pady=1)
        UnitPriceLabel = ctk.CTkLabel(entryFieldFrame, text="Unit Price:", font=("Aptos", 12))
        UnitPriceLabel.grid(row=4, column=0, sticky="w", padx=1, pady=1)
        SupervisorLabel = ctk.CTkLabel(entryFieldFrame, text="Supervisor:", font=("Aptos", 12))
        SupervisorLabel.grid(row=6, column=0, sticky="w", padx=1, pady=1)
        companyLabel = ctk.CTkLabel(entryFieldFrame, text="Company:", font=("Aptos", 12))
        companyLabel.grid(row=8, column=0, sticky="w", padx=1, pady=1)

        # Add company button
        linkFrame = ctk.CTkFrame(entryFieldFrame, fg_color="transparent")
        linkFrame.grid(row=10, column=0, sticky="w", padx=10, pady=(0, 10))

        addCompanyLink = ctk.CTkLabel(linkFrame, text="Add Company", text_color="#1E90FF", cursor="hand2", font=("Aptos", 12, "underline"))
        addCompanyLink.grid(row=0, column=0, sticky="w")
        addCompanyLink.bind("<Button-1>", lambda e: self.controller.showAddCompany())

        # Preview Frame
        previewFrame = ctk.CTkFrame(self, border_width=0)
        previewFrame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        previewFrame.grid_columnconfigure(0, weight=1)
        previewFrame.grid_columnconfigure(1, weight=0)
    
        
    def getInvoiceData(company, poNumber, jobAddress, unitPrice, supervisor):
        try:
            if not company or not getattr(company, "googleSheetId", None):
                messagebox.showwarning("Warning", "This company does not have a linked Google Sheet ID.")
                return

            # --- Open Google Sheet ---
            sheet = client.open_by_key(company.googleSheetId).sheet1

            # --- Update normal values ---
            sheet.update("G7", [[poNumber]])      # PO Number
            sheet.update("B19", [[jobAddress]])   # Job Address
            sheet.update("F19", [[unitPrice]])    # Unit Price
            sheet.update("B15", [[supervisor]])   # Supervisor

            # --- Increment invoice number (G6) ---
            current_invoice = sheet.acell("G6").value
            current_invoice = int(current_invoice) if str(current_invoice).isdigit() else 0
            sheet.update("G6", [[current_invoice + 1]])

            # --- Auto formulas ---
            sheet.update("G19", [["=F19*0.1"]])      # 10% of unit price
            sheet.update("G21", [["=G19+F19"]])      # total

            # --- Apply formatting ---
            from gspread_formatting import (
                CellFormat, TextFormat, format_cell_range,
                Color, NumberFormat
            )

            # Text style (bold, size 12, black)
            bold_black = CellFormat(
                textFormat=TextFormat(bold=True, fontSize=12, foregroundColor=Color(0, 0, 0))
            )

            # Money style
            money_format = CellFormat(
                numberFormat=NumberFormat(type="NUMBER", pattern="£#,##0.00")
            )

            # Apply text formatting
            format_cell_range(sheet, "G7", bold_black)
            format_cell_range(sheet, "B19", bold_black)
            format_cell_range(sheet, "F19", bold_black)
            format_cell_range(sheet, "B15", bold_black)
            format_cell_range(sheet, "G6", bold_black)

            # Apply money formatting
            format_cell_range(sheet, "F19", money_format)
            format_cell_range(sheet, "G19", money_format)
            format_cell_range(sheet, "G21", money_format)

            messagebox.showinfo("Success", f"Invoice saved and updated in {company.name}'s Google Sheet.")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to update Google Sheet: {e}")


    def load_companies(self):
        """Reload companies from JSON for the current user"""
        import json, os
        USERS_FILE = "users.json"

        self.controller.companyList = []  # clear previous list

        if self.controller.current_user and os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r") as f:
                users = json.load(f)
            companies_data = users[self.controller.current_user].get("companies", [])
            self.controller.companyList = [
                Company(c["name"], c["email"], c["googleSheetId"]) for c in companies_data
            ]

        # Update dropdown
        if self.controller.companyList:
            names = [c.name for c in self.controller.companyList]
            self.companyDropdown.configure(values=names)
            self.companyDropdown.set(names[0])
        else:
            self.companyDropdown.configure(values=["No companies"])
            self.companyDropdown.set("No companies")