import customtkinter as ctk
from Invoice import Invoice
import json, os                       
from AiUserandDatastorage import USER_DATA_DIR

class MainPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")
        ...
        # (keep UI as before)
        ...

    def getInvoiceData(self):
        username = self.controller.current_user.username
        user_file = os.path.join(USER_DATA_DIR, f"{username}.json")
        company_name = self.companyEntry.get()
        company_email = "unknown"

        if os.path.exists(user_file):
            with open(user_file, "r") as f:
                data = json.load(f)
            for c in data.get("companies", []):
                if c["name"] == company_name:
                    company_email = c["email"]

        invoice = Invoice(
            poNumber=self.poNumberEntry.get(),
            jobAddress=self.jobAddressEntry.get(),
            unitPrices=self.UnitPriceEntry.get(),
            supervisor=self.SupervisorEntry.get(),
            companyEmailAddress=company_email,
            Company=company_name
        )
        print(invoice.poNumber, invoice.jobAddress, invoice.unitPrices, invoice.supervisor, invoice.companyEmailAddress, invoice.Company)
        return invoice

    def load_companies(self):
        username = self.controller.current_user.username
        user_file = os.path.join(USER_DATA_DIR, f"{username}.json")
        ...
