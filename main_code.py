import tkinter as tk
import customtkinter as ctk
import time 
import tkinter.messagebox
import configparser

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



app = ctk.CTk()

app.after(0, lambda:app.state('zoomed'))
app.title("Office")
#ovdje sam kreirao tabView
tabView = ctk.CTkTabview(app)
tabView.pack(pady=0, padx=0, fill="both", expand=True)

#ovdje sam dodao tri taba
tabView.add("Main Office")
tabView.add("Middle Office")
tabView.add("Back Office")

#ovdje sam stavio da tab glavni izbornik bude prvi otvoren kada se pokrene aplikacija
tabView.set("Back Office")

#region Fiksni Frameovi
#Fiksni frame Main Office
fixed_frame_main_office = ctk.CTkFrame(tabView.tab("Main Office"),height=35)
fixed_frame_main_office.pack(pady=5,padx=5,fill="both")
#fiksni frame Middle Office
fixed_frame_middle_office = ctk.CTkFrame(tabView.tab("Middle Office"),height=35)
fixed_frame_middle_office.pack(pady=5,padx=5,fill="both")
#fiksni frame Back Office
fixed_frame_back_office = ctk.CTkFrame(tabView.tab("Back Office"),height=35)
fixed_frame_back_office.pack(pady=5,padx=5,fill="both")
#endregion

#region Scrollable Frameovi
#Main scrollable frame
scrollable_frame_Main = ctk.CTkScrollableFrame(tabView.tab("Main Office"))
scrollable_frame_Main.pack(pady=5, padx=5, fill="both", expand=True)
#Middle scrollable frame
scrollable_frame_Middle = ctk.CTkScrollableFrame(tabView.tab("Middle Office"))
scrollable_frame_Middle.pack(pady=5, padx=5, fill="both", expand=True)
#Back scrollable frame
scrollable_frame_Back = ctk.CTkScrollableFrame(tabView.tab("Back Office"))
scrollable_frame_Back.pack(pady=5, padx=5, fill="both", expand=True)
#endregion

#region Liste
main_add_all_list = []
middle_add_all_list = []
back_add_all_list = []
#endregion

#region Konstante
i = 1
j = 1
k = 1
#endregion

#region FUNKCIJE 
def main_add_row():
    global i
    main_checkbox = ctk.CTkCheckBox(scrollable_frame_Main,text=None)
    main_checkbox.grid(column=0,row=i+1,padx=0,sticky="w")
    
    main_entry_datum = ctk.CTkEntry(scrollable_frame_Main,width=100)
    main_entry_datum.grid(column=1,row=i+1,padx=0,pady=0,sticky="w")
    #add_all_list.append(entry_datum)

    main_entry_otkup = ctk.CTkEntry(scrollable_frame_Main,width=340)
    main_entry_otkup.grid(column=2,row=i+1,padx=0,pady=0)
    #add_all_list.append(entry_datum)

    main_entry_ustup = ctk.CTkEntry(scrollable_frame_Main,width=260)
    main_entry_ustup.grid(column=3,row=i+1,padx=0)
    #add_all_list.append(entry_ustup)

    main_entry_datumipotpis = ctk.CTkEntry(scrollable_frame_Main,width=310)
    main_entry_datumipotpis.grid(column=4,row=i+1,padx=0,pady=0)
    #add_all_list.append(entry_datumipotpis)
    
    # Store references to the widgets of the row in a list
    main_row_widgets = [main_checkbox, main_entry_datum, main_entry_otkup, main_entry_ustup, main_entry_datumipotpis]
    main_add_all_list.append(main_row_widgets)
    
    i += 1
    
def main_delete_row():
    global i
    if main_add_all_list:
        last_row_widgets = main_add_all_list.pop()  # Remove the last row's widgets from the list
        for widget in last_row_widgets:
            widget.destroy()  # Destroy each widget in the row
        i -= 1
    else:
        tkinter.messagebox.showinfo("Error","Nije moguce izbrisati pocetni red")

def middle_add_row():
    
    global j
    middle_checkbox = ctk.CTkCheckBox(scrollable_frame_Middle,text=None)
    middle_checkbox.grid(column=0,row=j+1,padx=0,sticky="w")
    
    middle_entry_datum = ctk.CTkEntry(scrollable_frame_Middle,width=300)
    middle_entry_datum.grid(column=1,row=j+1,padx=0,pady=0,sticky="w")

    middle_entry_br_ugovora = ctk.CTkEntry(scrollable_frame_Middle,width=170)
    middle_entry_br_ugovora.grid(column=2,row=j+1,padx=0,pady=0)

    middle_entry_br_fakture = ctk.CTkEntry(scrollable_frame_Middle,width=170)
    middle_entry_br_fakture.grid(column=3,row=j+1,padx=0)

    middle_entry_iznos = ctk.CTkEntry(scrollable_frame_Middle,width=150)
    middle_entry_iznos.grid(column=4,row=j+1,padx=0,pady=0)
    
    middle_entry_placeno_neplaceno = ctk.CTkEntry(scrollable_frame_Middle,width=310)
    middle_entry_placeno_neplaceno.grid(column=5,row=j+1,padx=0,pady=0)
    
    # Store references to the widgets of the row in a list
    middle_row_widgets = [middle_checkbox,middle_entry_datum,middle_entry_br_ugovora,
                   middle_entry_br_fakture,middle_entry_iznos,middle_entry_placeno_neplaceno]
    middle_add_all_list.append(middle_row_widgets)
    
    j += 1

def middle_delete_row():
    global j
    if middle_add_all_list:
        last_row_widgets = middle_add_all_list.pop()  # Remove the last row's widgets from the list
        for widget in last_row_widgets:
            widget.destroy()  # Destroy each widget in the row
        j -= 1
    else:
        tkinter.messagebox.showinfo("Error","Nije moguce izbrisati pocetni red")

def back_add_row():
    global k
    
    back_checkbox = ctk.CTkCheckBox(scrollable_frame_Back,text=None)
    back_checkbox.grid(column=0,row=k+1,ipadx=0,sticky="w")
    
    back_entry_primatelj = ctk.CTkEntry(scrollable_frame_Back,width=105)
    back_entry_primatelj.grid(column=1,row=k+1,ipadx=0,pady=(5,0),sticky="w")

    back_entry_posiljatelj = ctk.CTkEntry(scrollable_frame_Back,width=105)
    back_entry_posiljatelj.grid(column=2,row=k+1,ipadx=0,pady=(5,0))

    back_entry_broj_ugovora = ctk.CTkEntry(scrollable_frame_Back,width=145)
    back_entry_broj_ugovora.grid(column=3,row=k+1,ipadx=0,pady=(5,0))

    back_entry_iznos_potrazivanja = ctk.CTkEntry(scrollable_frame_Back,width=195)
    back_entry_iznos_potrazivanja.grid(column=4,row=k+1,ipadx=0,pady=(5,0))

    back_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_Back,width=140)
    back_entry_iznos_otkupa.grid(column=5,row=k+1,ipadx=0,pady=(5,0))

    back_entry_broj_fakture = ctk.CTkEntry(scrollable_frame_Back,width=130)
    back_entry_broj_fakture.grid(column=6,row=k+1,ipadx=0,pady=(5,0))

    back_entry_datum_stavljanja_na_placanje = ctk.CTkEntry(scrollable_frame_Back,width=300)
    back_entry_datum_stavljanja_na_placanje.grid(column=7,row=k+1,ipadx=0,pady=(5,0))

    back_row_widgets = [back_checkbox,back_entry_primatelj,back_entry_posiljatelj,
                        back_entry_broj_ugovora,back_entry_iznos_potrazivanja,
                        back_entry_iznos_otkupa,back_entry_broj_fakture,
                        back_entry_datum_stavljanja_na_placanje]
    back_add_all_list.append(back_row_widgets)
    
    k += 1

def back_delete_row():
    global k
    if back_add_all_list:
        last_row_widgets = back_add_all_list.pop()  # Remove the last row's widgets from the list
        for widget in last_row_widgets:
            widget.destroy()  # Destroy each widget in the row
        k -= 1
    else:
        tkinter.messagebox.showinfo("Error","Nije moguce izbrisati pocetni red")
    
#endregion




#region Labele Main Office
main_label_datum = ctk.CTkLabel(fixed_frame_main_office,
                           text="Datum",
                           font=("Arial",24))
main_label_datum.grid(column=1,row=0,ipadx=10)

main_label_otkup = ctk.CTkLabel(fixed_frame_main_office,
                           text="Ugovor o otkupu",
                           font=("Arial",24))
main_label_otkup.grid(column=2,row=0,ipadx=120)

main_label_otkup = ctk.CTkLabel(fixed_frame_main_office,
                           text="Ugovor o ustupu",
                           font=("Arial",24))
main_label_otkup.grid(column=3,row=0,ipadx=80)

main_label_otkup = ctk.CTkLabel(fixed_frame_main_office,
                           text="Potpis sa datumom",
                           font=("Arial",24))
main_label_otkup.grid(column=4,row=0,ipadx=60)
#endregion

#region Entry Main Office
main_entry_datum = ctk.CTkEntry(scrollable_frame_Main,width=100)
main_entry_datum.grid(column=1,row=1,padx=0,pady=(5,0),sticky="w")

main_entry_otkup = ctk.CTkEntry(scrollable_frame_Main,width=340)
main_entry_otkup.grid(column=2,row=1,padx=0,pady=(5,0))

main_entry_ustup = ctk.CTkEntry(scrollable_frame_Main,width=260)
main_entry_ustup.grid(column=3,row=1,padx=0,pady=(5,0))

main_entry_datumipotpis = ctk.CTkEntry(scrollable_frame_Main,width=310)
main_entry_datumipotpis.grid(column=4,row=1,padx=0,pady=(5,0))
#endregion

#region Checkbox Main Office
#checkbox Main Office
main_checkbox = ctk.CTkCheckBox(scrollable_frame_Main,text=None)
main_checkbox.grid(column=0,row=1,padx=0,sticky="w")
#endregion

#region gumb za dodavanje/oduzimanje reda Main Office
main_button_add_row = ctk.CTkButton(fixed_frame_main_office,text="+",
                               width=10,
                               corner_radius=120,
                               anchor="w",
                               command=main_add_row)
main_button_add_row.grid(column=0,row=0,sticky="w")

main_button_delete_row = ctk.CTkButton(fixed_frame_main_office,text="-",
                               width=30,
                               corner_radius=120,
                               command=main_delete_row)
main_button_delete_row.grid(column=0,row=0,padx=40)
#endregion



#region Label Middle office

middle_label_datum = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Datum dospijeca placanja",
                           font=("Arial",24))
middle_label_datum.grid(column=1,row=0,ipadx=10)

middle_label_br_ugovora = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Broj ugovora",
                           font=("Arial",24))
middle_label_br_ugovora.grid(column=2,row=0,ipadx=40)

middle_label_br_fakture = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Broj fakture",
                           font=("Arial",24))
middle_label_br_fakture.grid(column=3,row=0,ipadx=10)

middle_label_iznos = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Iznos",
                           font=("Arial",24))
middle_label_iznos.grid(column=4,row=0,ipadx=100)

middle_label_placeno_neplaceno = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Placeno/Neplaceno",
                           font=("Arial",24))
middle_label_placeno_neplaceno.grid(column=5,row=0,ipadx=30)

#endregion

#region Entry Middle Office
middle_entry_datum = ctk.CTkEntry(scrollable_frame_Middle,width=300)
middle_entry_datum.grid(column=1,row=1,padx=0,pady=(5,0),sticky="w")

middle_entry_br_ugovora = ctk.CTkEntry(scrollable_frame_Middle,width=170)
middle_entry_br_ugovora.grid(column=2,row=1,padx=0,pady=(5,0))

middle_entry_br_fakture = ctk.CTkEntry(scrollable_frame_Middle,width=170)
middle_entry_br_fakture.grid(column=3,row=1,padx=0,pady=(5,0))

middle_entry_iznos = ctk.CTkEntry(scrollable_frame_Middle,width=150)
middle_entry_iznos.grid(column=4,row=1,padx=0,pady=(5,0))

middle_entry_placeno_neplaceno = ctk.CTkEntry(scrollable_frame_Middle,width=310)
middle_entry_placeno_neplaceno.grid(column=5,row=1,padx=0,pady=(5,0))
#endregion

#region Checkbox Middle Office
checkbox = ctk.CTkCheckBox(scrollable_frame_Middle,text=None)
checkbox.grid(column=0,row=1,padx=0,sticky="w")
#endregion

#region gumb za dodavanje/oduzimanje reda Middle Office
middle_button_add_row = ctk.CTkButton(fixed_frame_middle_office,text="+",
                               width=10,
                               corner_radius=120,
                               anchor="w",
                               command=middle_add_row)
middle_button_add_row.grid(column=0,row=0,sticky="w")

middle_button_delete_row = ctk.CTkButton(fixed_frame_middle_office,text="-",
                               width=30,
                               corner_radius=120,
                               command=middle_delete_row)
middle_button_delete_row.grid(column=0,row=0,padx=40)
#endregion



#region Label Back Office
back_label_primatelj = ctk.CTkLabel(fixed_frame_back_office,
                           text="Primatelj",
                           font=("Arial",24))
back_label_primatelj.grid(column=1,row=0,padx=5)

back_label_posiljatelj = ctk.CTkLabel(fixed_frame_back_office,
                           text="Posiljatelj",
                           font=("Arial",24))
back_label_posiljatelj.grid(column=2,row=0,ipadx=5)

back_label_broj_ugovora = ctk.CTkLabel(fixed_frame_back_office,
                           text="Broj ugovora",
                           font=("Arial",24))
back_label_broj_ugovora.grid(column=3,row=0,ipadx=5)

back_label_iznos_potrazivanja = ctk.CTkLabel(fixed_frame_back_office,
                           text="Iznos potrazivanja",
                           font=("Arial",24))
back_label_iznos_potrazivanja.grid(column=4,row=0,ipadx=5)

back_label_iznos_otkupa = ctk.CTkLabel(fixed_frame_back_office,
                           text="Iznos otkupa",
                           font=("Arial",24))
back_label_iznos_otkupa.grid(column=5,row=0,ipadx=5)

back_label_broj_fakture = ctk.CTkLabel(fixed_frame_back_office,
                           text="Broj fakture",
                           font=("Arial",24))
back_label_broj_fakture.grid(column=6,row=0,ipadx=5)

back_label_datum_stavljanja_na_placanje = ctk.CTkLabel(fixed_frame_back_office,
                                            text="Datum stavljanja na placanje",
                                            font=("Arial",24))
back_label_datum_stavljanja_na_placanje.grid(column=7,row=0,ipadx=5)
#endregion

#region Entry Back Office

back_entry_primatelj = ctk.CTkEntry(scrollable_frame_Back,width=105)
back_entry_primatelj.grid(column=1,row=1,ipadx=0,pady=(5,0),sticky="w")

back_entry_posiljatelj = ctk.CTkEntry(scrollable_frame_Back,width=105)
back_entry_posiljatelj.grid(column=2,row=1,ipadx=0,pady=(5,0))

back_entry_broj_ugovora = ctk.CTkEntry(scrollable_frame_Back,width=145)
back_entry_broj_ugovora.grid(column=3,row=1,ipadx=0,pady=(5,0))

back_entry_iznos_potrazivanja = ctk.CTkEntry(scrollable_frame_Back,width=195)
back_entry_iznos_potrazivanja.grid(column=4,row=1,ipadx=0,pady=(5,0))

back_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_Back,width=140)
back_entry_iznos_otkupa.grid(column=5,row=1,ipadx=0,pady=(5,0))

back_entry_broj_fakture = ctk.CTkEntry(scrollable_frame_Back,width=130)
back_entry_broj_fakture.grid(column=6,row=1,ipadx=0,pady=(5,0))

back_entry_datum_stavljanja_na_placanje = ctk.CTkEntry(scrollable_frame_Back,width=300)
back_entry_datum_stavljanja_na_placanje.grid(column=7,row=1,ipadx=0,pady=(5,0))

#endregion

#region Checkbox Back Office

back_checkbox = ctk.CTkCheckBox(scrollable_frame_Back,text=None)
back_checkbox.grid(column=0,row=1,ipadx=0,sticky="w")
#endregion

#region gumb za dodavanje reda Back Office
button_add_row = ctk.CTkButton(fixed_frame_back_office,text="+",
                               width=10,
                               corner_radius=120,
                               anchor="w",
                               command=back_add_row)
button_add_row.grid(column=0,row=0,sticky="w",ipadx=0)

button_delete_row = ctk.CTkButton(fixed_frame_back_office,text="-",
                               width=10,
                               corner_radius=20,
                               command=back_delete_row)
button_delete_row.grid(column=0,row=0,padx=40,ipadx=0)
#endregion








app.mainloop()