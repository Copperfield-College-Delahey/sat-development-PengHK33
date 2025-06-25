import customtkinter as ctk
from CTkTable import*
app = ctk.CTK()
app.title("My App")
app.geometry("1000x600")
#conigure app window grid
app.grid_collumnconfigure(0, weight=1) # left column
app.grid_collumnconfigure(0, weight=1) # right column
app.grid_rowconfigure(0, weight=1) # top bar
app.grid_rowconfigure(1, weight=6) # main content
app.grid_rowconfigure(2, weight=1) # footer
#Top Frame
topFrame = ctk.CTkFrame(app, border_width=4)
topFrame.grid(row=0, collumn=0, columnspan=2, sticky="nsew",padx=5,pady=5)
topFrame.grid_collumnconfigure(0,weight=1)
topFrame.grid_collumnconfigure(1,weight=0)
titleLabel = ctk.CTkLabel(topFrame, text ="Innovate Invoice",font=("Aptos",30))
