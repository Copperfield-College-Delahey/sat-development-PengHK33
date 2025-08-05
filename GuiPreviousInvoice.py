import customtkinter as ctk

# Setup
app = ctk.CTk()
app.title("Previous Invoices")
app.geometry("800x500")

# Configure window grid
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)

# Title
titleLabel = ctk.CTkLabel(app, text="Previous Invoices", font=("Aptos", 24, "bold"))
titleLabel.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

# Scrollable Frame for invoice list
scroll_frame = ctk.CTkScrollableFrame(app, width=700, height=350)
scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
scroll_frame.grid_columnconfigure(0, weight=1)

# Back button
back_button = ctk.CTkButton(app, text="Back")
back_button.grid(row=2, column=0, padx=20, pady=15, sticky="w")

# Run app
app.mainloop()
