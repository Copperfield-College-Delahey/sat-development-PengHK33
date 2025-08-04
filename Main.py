import customtkinter as ctk

from GuiStartUpPage import LoginPage
from GuiMainPage import MainPage
from GuiAddCompany import AddCompanyPage
from GuiCreateAccount import CreateAccountPage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("My App")
        self.geometry("1000x600")

        # Configure the layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frame container for all pages
        self.pageContainer = ctk.CTkFrame(self)
        self.pageContainer.grid(row=0, column=0, sticky="nsew")
        self.pageContainer.grid_rowconfigure(0, weight=1)
        self.pageContainer.grid_columnconfigure(0, weight=1)

        # Load all pages
        self.loginPage = LoginPage(self.pageContainer, self)
        self.loginPage.grid(row=0, column=0, sticky="nsew")

        self.mainPage = MainPage(self.pageContainer, self)
        self.mainPage.grid(row=0, column=0, sticky="nsew")

        self.addCompanyPage = AddCompanyPage(self.pageContainer, self)
        self.addCompanyPage.grid(row=0, column=0, sticky="nsew")

        self.createAccountPage = CreateAccountPage(self.pageContainer, self)
        self.createAccountPage.grid(row=0, column=0, sticky="nsew")

        # Show login page first
        self.loginPage.tkraise()

    # Optional helper methods
    def show_login(self): self.loginPage.tkraise()
    def show_main(self): self.mainPage.tkraise()
    def show_add_company(self): self.addCompanyPage.tkraise()
    def show_create_account(self): self.createAccountPage.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
