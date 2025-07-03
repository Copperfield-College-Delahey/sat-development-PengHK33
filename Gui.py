import customtkinter as ctk
app = ctk.CTk()
app.title("My App")
app.geometry("1000x600")

#conigure app window grid
app.grid_columnconfigure(0, weight=1) # left column
app.grid_columnconfigure(1, weight=1) # right column
app.grid_rowconfigure(0, weight=1) # top bar
app.grid_rowconfigure(1, weight=6) # main content
app.grid_rowconfigure(2, weight=1) # footer

#Top Frame
topFrame = ctk.CTkFrame(app, border_width=0)
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew",padx=5,pady=5)
topFrame.grid_columnconfigure(0,weight=1)
topFrame.grid_columnconfigure(1,weight=0)
titleLabel = ctk.CTkLabel(topFrame, text="Innovate Invoice", font=("Aptos", 30))
titleLabel.grid(row=0, column=0, sticky="w", padx=1, pady=1)

#Bottom Frame
bottomFrame = ctk.CTkFrame(app, border_width=0)
bottomFrame.grid(row=2, column=0, columnspan=2, sticky="nsew",padx=5,pady=5)
bottomFrame.grid_columnconfigure(0,weight=1)
bottomFrame.grid_columnconfigure(1,weight=1)
submitButton = ctk.CTkButton(bottomFrame, text="Submit")
submitButton.grid(row=0, column=1, padx=10, pady=10, sticky="e")
previousButton = ctk.CTkButton(bottomFrame, text="Previous Invoices")
previousButton.grid(row=0, column=0, padx=10, pady=10, sticky="e")

#Entryfield Frame
entryFieldFrame = ctk.CTkFrame(app, border_width=0)
entryFieldFrame.grid(row=1, column=0, sticky="nsew",padx=5,pady=5)
entryFieldFrame.grid_rowconfigure(0,weight=1)
entryFieldFrame.grid_rowconfigure(1,weight=1)
entryFieldFrame.grid_rowconfigure(2,weight=1)
entryFieldFrame.grid_rowconfigure(3,weight=1)
entryFieldFrame.grid_rowconfigure(4,weight=1)
entryFieldFrame.grid_rowconfigure(5,weight=1)
entryFieldFrame.grid_rowconfigure(6,weight=1)
entryFieldFrame.grid_rowconfigure(7,weight=1)
entryFieldFrame.grid_rowconfigure(8,weight=1)
entryFieldFrame.grid_rowconfigure(9,weight=1)

#Entryframe Entryfields
poNumberEntry = ctk.CTkEntry(entryFieldFrame, width=200)
poNumberEntry.grid(row=1, column=0, padx=10, pady=10, sticky="w")
jobAddressEntry = ctk.CTkEntry(entryFieldFrame, width=200)
jobAddressEntry.grid(row=3, column=0, padx=10, pady=10, sticky="w")
UnitPriceEntry = ctk.CTkEntry(entryFieldFrame, width=200)
UnitPriceEntry.grid(row=5, column=0, padx=10, pady=10, sticky="w")
SupervisorEntry = ctk.CTkEntry(entryFieldFrame, width=200)
SupervisorEntry.grid(row=7, column=0, padx=10, pady=10, sticky="w")
companyEntry = ctk.CTkEntry(entryFieldFrame, width=200)
companyEntry.grid(row=9, column=0, padx=10, pady=10, sticky="w")

#Entryframe labels
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

#Preview Frame
previewFrame = ctk.CTkFrame(app, border_width=0)
previewFrame.grid(row=1, column=1, sticky="nsew",padx=5,pady=5)
previewFrame.grid_columnconfigure(0,weight=1)
previewFrame.grid_columnconfigure(1,weight=0)

app.mainloop()