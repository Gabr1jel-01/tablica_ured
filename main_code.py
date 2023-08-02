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
tabView.pack(pady=0, padx=0, fill="both", expand=True)

#ovdje sam dodao dva taba
tabView.add("Tablica")
tabView.add("Tablica 2")


#ovdje sam stavio da tab glavni izbornik bude prvi otvoren kada se pokrene aplikacija
tabView.set("Tablica")


#Fiksni frame
fixed_frame = ctk.CTkFrame(tabView.tab("Tablica"),height=35)
fixed_frame.pack(pady=5,padx=5,fill="both")

#Frame koji ima scroll
scrollable_frame = ctk.CTkScrollableFrame(tabView.tab("Tablica"))
scrollable_frame.pack(pady=5, padx=5, fill="both", expand=True)


#funkcija koja se pokrene kada stisnem + gumb

i = 1
def add_row():
    global i
    checkbox = ctk.CTkCheckBox(scrollable_frame,text=None)
    checkbox.grid(column=0,row=i+1,padx=0,sticky="w")
    
    entry_datum = ctk.CTkEntry(scrollable_frame,width=100)
    entry_datum.grid(column=1,row=i+1,padx=0,pady=0,sticky="w")

    entry_otkup = ctk.CTkEntry(scrollable_frame,width=340)
    entry_otkup.grid(column=2,row=i+1,padx=0,pady=0)

    entry_ustup = ctk.CTkEntry(scrollable_frame,width=260)
    entry_ustup.grid(column=3,row=i+1,padx=0)

    entry_datumipotpis = ctk.CTkEntry(scrollable_frame,width=310)
    entry_datumipotpis.grid(column=4,row=i+1,padx=0,pady=0)
    
    i += 1
    pass

#Labele Tablica
label_datum = ctk.CTkLabel(fixed_frame,
                           text="Datum",
                           font=("Arial",24))
label_datum.grid(column=1,row=0,ipadx=175)

label_otkup = ctk.CTkLabel(fixed_frame,
                           text="Ugovor o otkupu",
                           font=("Arial",24))
label_otkup.grid(column=2,row=0,ipadx=0)

label_otkup = ctk.CTkLabel(fixed_frame,
                           text="Ugovor o ustupu",
                           font=("Arial",24))
label_otkup.grid(column=3,row=0,ipadx=170)

label_otkup = ctk.CTkLabel(fixed_frame,
                           text="Potpis sa datumom",
                           font=("Arial",24))
label_otkup.grid(column=4,row=0)



#entry

entry_datum = ctk.CTkEntry(scrollable_frame,width=100)
entry_datum.grid(column=1,row=1,padx=0,pady=(5,0),sticky="w")

entry_otkup = ctk.CTkEntry(scrollable_frame,width=340)
entry_otkup.grid(column=2,row=1,padx=0,pady=(5,0))

entry_ustup = ctk.CTkEntry(scrollable_frame,width=260)
entry_ustup.grid(column=3,row=1,padx=0,pady=(5,0))

entry_datumipotpis = ctk.CTkEntry(scrollable_frame,width=310)
entry_datumipotpis.grid(column=4,row=1,padx=0,pady=(5,0))


#gumb za dodavanje reda
button_add_row = ctk.CTkButton(scrollable_frame,text="+",
                               width=30,
                               corner_radius=120,
                               anchor="w",
                               command=add_row)
button_add_row.grid(column=0,row=0,sticky="w")

checkbox = ctk.CTkCheckBox(scrollable_frame,text=None)
checkbox.grid(column=0,row=1,padx=0,sticky="w")




text_1 = ctk.CTkTextbox(tabView.tab("Tablica 2"), width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "CTkTextbox\n\n\n\n")


#class Table():
    
    #def __init__(self,root):
    
    



app.mainloop()