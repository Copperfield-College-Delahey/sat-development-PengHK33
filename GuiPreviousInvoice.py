#GuiPreviousInvoice.py:
import customtkinter as ctk

class PreviousInvoicesPage(ctk.CTkFrame):
    def __init__(self, master, controller=None):
        super().__init__(master)
        self.controller= controller


        # Configure window grid
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)


        # Title
        titleLabel = ctk.CTkLabel(self, text="Previous Invoices", font=("Aptos", 24, "bold"))
        titleLabel.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # Scrollable Frame for invoice list
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=700, height=350)
        self.scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.scroll_frame.grid_columnconfigure(0, weight=1)

        # Back button
        back_button = ctk.CTkButton(self, text="Back", command=self.controller.showMain)
        back_button.grid(row=2, column=0, padx=20, pady=15, sticky="w")
  
