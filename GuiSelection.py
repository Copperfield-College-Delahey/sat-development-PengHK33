import customtkinter as ctk

class AddCompanyPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")

        # Center the login box
        app.grid_columnconfigure(0, weight=1)
        app.grid_columnconfigure(1, weight=1)
        app.grid_columnconfigure(2, weight=1)
        app.grid_rowconfigure(0, weight=1)
        app.grid_rowconfigure(1, weight=1)
        app.grid_rowconfigure(2, weight=1)

        # Login frame
        mainBox = ctk.CTkFrame(app, corner_radius=10, width=400, height=400)
        mainBox.grid(row=1, column=1)
        mainBox.grid_propagate(False)
        mainBox.grid_columnconfigure(0, weight=1)
        mainBox.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7,8,9), weight=1)

        # Title (left-aligned)
        newCompanyTitle = ctk.CTkLabel(mainBox, text="Add New Company:", font=("Aptos", 24, "bold"), anchor="w", justify="left")
        newCompanyTitle.grid(row=0, column=0, padx=30, pady=(15, 5), sticky="w")

        # New Company Name
        CompanNameLabel = ctk.CTkLabel(mainBox, text="Company Name:", font=("Aptos", 13))
        CompanNameLabel.grid(row=1, column=0, sticky="w", padx=30, pady=(5, 0))
        CompanNameEntry = ctk.CTkEntry(mainBox, width=290)
        CompanNameEntry.grid(row=2, column=0, padx=30, pady=(0, 10), sticky="w")

        # Company Email
        companyEmailLabel = ctk.CTkLabel(mainBox, text="Company Email address", font=("Aptos", 13))
        companyEmailLabel.grid(row=3, column=0, sticky="w", padx=30, pady=(5, 0))
        companyEmailEntry = ctk.CTkEntry(mainBox, width=290)
        companyEmailEntry.grid(row=4, column=0, padx=30, pady=(0, 10), sticky="w")

        # Google Form layout Link
        invoiceLayoutLinkLabel = ctk.CTkLabel(mainBox, text="Company Email address", font=("Aptos", 13))
        invoiceLayoutLinkLabel.grid(row=5, column=0, sticky="w", padx=30, pady=(5, 0))
        invoiceLayoutLinkEntry = ctk.CTkEntry(mainBox, width=290)
        invoiceLayoutLinkEntry.grid(row=6, column=0, padx=30, pady=(0, 10), sticky="w")

        # Back Button (small, bottom left)
        backButton = ctk.CTkButton(mainBox, text="Back", width=80)
        backButton.grid(row=7, column=0, padx=30, pady=(15, 10), sticky="w")

        # Submit Button (small, bottom left)
        submitButton = ctk.CTkButton(mainBox, text="Submit", width=80)
        submitButton.grid(row=7, column=1, padx=30, pady=(15, 10), sticky="w")



