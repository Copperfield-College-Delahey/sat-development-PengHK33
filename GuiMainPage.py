import customtkinter as ctk
from Invoice import Invoice
import json, os                       
from AiUserandDatastorage import USER_DATA_DIR

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

        submitButton = ctk.CTkButton(bottomFrame, text="Submit",command=self.getInvoiceData) 
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

        # Entryframe Entryfields
        self.poNumberEntry = ctk.CTkEntry(entryFieldFrame, width=200)
        self.poNumberEntry.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.jobAddressEntry = ctk.CTkEntry(entryFieldFrame, width=200)
        self.jobAddressEntry.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.UnitPriceEntry = ctk.CTkEntry(entryFieldFrame, width=200)
        self.UnitPriceEntry.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.SupervisorEntry = ctk.CTkEntry(entryFieldFrame, width=200)
        self.SupervisorEntry.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.companyEntry = ctk.CTkComboBox(entryFieldFrame, values=[], width=200)
        self.companyEntry.grid(row=9, column=0, padx=10, pady=10, sticky="w")

        self.load_companies()

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
    
    def getInvoiceData(self):
        invoice = Invoice(
            poNumber = self.poNumberEntry.get(),
            jobAddress = self.jobAddressEntry.get(),
            unitPrices = self.UnitPriceEntry.get(),
            supervisor = self.SupervisorEntry.get(),
            companyEmailAddress="placeholder@gmail.com",  # Placeholder for email address
            Company = self.companyEntry.get()
        )
        
        print(invoice.poNumber, invoice.jobAddress, invoice.unitPrices, invoice.supervisor, invoice.companyEmailAddress, invoice.Company)
        
        return invoice

    def load_companies(self):          
        """Load companies for the logged-in user and update dropdown."""
        username = self.controller.current_user.username
        user_file = os.path.join(USER_DATA_DIR, f"{username}.json")

        if os.path.exists(user_file):
            with open(user_file, "r") as f:
                data = json.load(f)
            companies = [c["name"] for c in data.get("companies", [])]
        else:
            companies = []

        self.companyEntry.configure(values=companies)

        if companies:
            self.companyEntry.set(companies[0])  # select first by default
        else:
            self.companyEntry.set("")            # leave empty if no companies