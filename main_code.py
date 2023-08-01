import tkinter as tk
import customtkinter as ctk
import time 

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()

app.after(0, lambda:app.state('zoomed'))
app.title("Tablica")

#ovdje sam kreirao tabView
tabView = ctk.CTkTabview(app)
tabView.pack(pady=10, padx=10, fill="both", expand=True)

#ovdje sam dodao dva taba
tabView.add("Tablica")
tabView.add("Glavni izbornik")


#ovdje sam stavio da tab glavni izbornik bude prvi otvoren kada se pokrene aplikacija
tabView.set("Tablica")


#funkcija koja se pokrene kada stisnem + gumb

i = 1



def add_row():
    
    global i
    
    checkbox = ctk.CTkCheckBox(tabView.tab("Tablica"),text=None)
    checkbox.grid(column=0,row=i+1,padx=0,sticky="w")
    
    
    
    
    entry_datum = ctk.CTkEntry(tabView.tab("Tablica"),width=100)
    entry_datum.grid(column=1,row=i+1,padx=0,pady=0,sticky="w")

    entry_otkup = ctk.CTkEntry(tabView.tab("Tablica"),width=340)
    entry_otkup.grid(column=2,row=i+1,padx=0,pady=0)

    entry_ustup = ctk.CTkEntry(tabView.tab("Tablica"),width=260)
    entry_ustup.grid(column=3,row=i+1,padx=0)

    entry_datumipotpis = ctk.CTkEntry(tabView.tab("Tablica"),width=310)
    entry_datumipotpis.grid(column=4,row=i+1,padx=0,pady=0)
    
    i += 1
    pass







#Labele
label_datum = ctk.CTkLabel(tabView.tab("Tablica"),
                           text="Datum",
                           font=("Arial",24))
label_datum.grid(column=1,row=0)

label_otkup = ctk.CTkLabel(tabView.tab("Tablica"),
                           text="Ugovor o otkupu",
                           font=("Arial",24))
label_otkup.grid(column=2,row=0,padx=70)

label_otkup = ctk.CTkLabel(tabView.tab("Tablica"),
                           text="Ugovor o ustupu",
                           font=("Arial",24))
label_otkup.grid(column=3,row=0)

label_otkup = ctk.CTkLabel(tabView.tab("Tablica"),
                           text="Potpis sa datumom",
                           font=("Arial",24))
label_otkup.grid(column=4,row=0,padx=50)


#entry

entry_datum = ctk.CTkEntry(tabView.tab("Tablica"),width=100)
entry_datum.grid(column=1,row=1,padx=0,pady=(5,0),sticky="w")

entry_otkup = ctk.CTkEntry(tabView.tab("Tablica"),width=340)
entry_otkup.grid(column=2,row=1,padx=0,pady=(5,0))

entry_ustup = ctk.CTkEntry(tabView.tab("Tablica"),width=260)
entry_ustup.grid(column=3,row=1,padx=0,pady=(5,0))

entry_datumipotpis = ctk.CTkEntry(tabView.tab("Tablica"),width=310)
entry_datumipotpis.grid(column=4,row=1,padx=0,pady=(5,0))


#gumb za dodavanje reda
button_add_row = ctk.CTkButton(tabView.tab("Tablica"),text="+",
                               width=30,
                               corner_radius=120,
                               anchor="w",
                               command=add_row)
button_add_row.grid(column=0,row=0,sticky="w")

checkbox = ctk.CTkCheckBox(tabView.tab("Tablica"),text=None)
checkbox.grid(column=0,row=1,padx=0,sticky="w")







#class Table():
    
    #def __init__(self,root):
    
    



app.mainloop()