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
topFrame = ctk.CTkFrame(app, border_width=4)
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew",padx=5,pady=5)
topFrame.grid_columnconfigure(0,weight=1)
topFrame.grid_columnconfigure(1,weight=0)
titleLabel = ctk.CTkLabel(topFrame, text="Innovate Invoice", font=("Aptos", 30))
titleLabel.grid(row=0, column=0, sticky="w", padx=1, pady=1)

#Bottom Frame
bottomFrame = ctk.CTkFrame(app, border_width=4)
bottomFrame.grid(row=2, column=0, columnspan=2, sticky="nsew",padx=5,pady=5)
bottomFrame.grid_columnconfigure(0,weight=1)
bottomFrame.grid_columnconfigure(1,weight=0)
submit_button = ctk.CTkButton(bottomFrame, text="Submit")
submit_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

#Entryfield Frame
entryFieldFrame = ctk.CTkFrame(app, border_width=4)
entryFieldFrame.grid(row=1, column=0, sticky="nsew",padx=5,pady=5)
entryFieldFrame.grid_columnconfigure(0,weight=1)
entryFieldFrame.grid_columnconfigure(1,weight=0)
nameEntry = ctk.CTkEntry(entryFieldFrame, width=200)
nameEntry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

#Preview Frame
previewFrame = ctk.CTkFrame(app, border_width=4)
previewFrame.grid(row=1, column=1, sticky="nsew",padx=5,pady=5)
previewFrame.grid_columnconfigure(0,weight=1)
previewFrame.grid_columnconfigure(1,weight=0)

app.mainloop()