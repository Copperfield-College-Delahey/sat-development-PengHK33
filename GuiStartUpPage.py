import customtkinter as ctk
app = ctk.CTk()
app.title("My App")
app.geometry("1000x600")

#conigure app window grid
app.grid_columnconfigure(0, weight=1) # 
app.grid_columnconfigure(1, weight=6) # 
app.grid_columnconfigure(2, weight=1) # main piece
app.grid_rowconfigure(0, weight=1) # main piece
app.grid_rowconfigure(1, weight=6) # 
app.grid_rowconfigure(2, weight=1) # 

#Main Box
mainBox = ctk.CTkFrame(app, border_width=0)
mainBox.grid(row=2, column=0, columnspan=2, sticky="nsew",padx=5,pady=5)
mainBox.grid_rowconfigure(0,weight=1)
mainBox.grid_rowonfigure(1,weight=1)

#Label
LogInTitle = ctk.CTkLabel(mainBox, text="INNOVATE INVOICES", font=("Aptos", 30))
LogInTitle.grid(row=0, column=0, sticky="w", padx=1, pady=1)
logInLabel = ctk.CTkLabel(mainBox, text="Po Number:", font=("Aptos", 12))
logInLabel.grid(row=1, column=0, sticky="w", padx=1, pady=1)
PasswordLabel = ctk.CTkLabel(mainBox, text="Job Address:", font=("Aptos", 12))
PasswordLabel.grid(row=3, column=0, sticky="w", padx=1, pady=1)

#inputBox
logInEntry = ctk.CTkEntry(entryFieldFrame, width=200)
logInEntry.grid(row=2, column=0, padx=10, pady=10, sticky="w")
passwordEntry = ctk.CTkEntry(entryFieldFrame, width=200)
passwordEntry.grid(row=4, column=0, padx=10, pady=10, sticky="w")