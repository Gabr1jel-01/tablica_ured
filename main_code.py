import tkinter as tk
from time import *
import customtkinter as ctk
import time 
import tkinter.messagebox
import configparser
from tkinter import filedialog


ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.after(0, lambda:app.state('zoomed'))
app.title("Office")

#region TabView
#ovdje sam kreirao tabView
tabView = ctk.CTkTabview(app)
tabView.pack(pady=0, padx=0, fill="both", expand=True)

#ovdje sam dodao tri taba
tabView.add("Main Office")
tabView.add("Middle Office")
tabView.add("Back Office")
tabView.add("Datoteka")

#ovdje sam stavio da tab glavni izbornik bude prvi otvoren kada se pokrene aplikacija
tabView.set("Main Office")
#endregion

#region Save i Save As buttons...
save_button = ctk.CTkButton(tabView.tab("Datoteka"), text="Spremi",command="")
save_button.pack(padx=450,pady=(190,5)) 

save_as_button = ctk.CTkButton(tabView.tab("Datoteka"), text="Spremi kao...",command="")
save_as_button.pack(padx=450,pady=(10,0))
#endregion

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
def add_row():
    global i
    global rows
    row = []

    cbox_var = tkinter.IntVar()
    kwargs = {}
    kwargs["checked"] = cbox_var
    kwargs["row"] = row
    checkbox = ctk.CTkCheckBox(scrollable_frame_Main,
                               onvalue=1,
                               variable=cbox_var,
                               offvalue=0,
                               text=None,
                               fg_color="#37CB56",
                               hover_color="#176828",
                               command=lambda kwargs=kwargs: checkbox_check(kwargs))
    checkbox.grid(column=0, row=i+1, padx=0, sticky="w")
    row.append(checkbox)

    entry_datum = ctk.CTkEntry(scrollable_frame_Main, width=100)
    entry_datum.grid(column=1, row=i+1, padx=0, pady=0, sticky="w")
    row.append(entry_datum)

    main_entry_otkup = ctk.CTkEntry(scrollable_frame_Main, width=340)
    main_entry_otkup.grid(column=2, row=i+1, padx=0, pady=0)
    row.append(main_entry_otkup)

    main_entry_ustup = ctk.CTkEntry(scrollable_frame_Main, width=260)
    main_entry_ustup.grid(column=3, row=i+1, padx=0)
    row.append(main_entry_ustup)

    main_entry_datumipotpis = ctk.CTkEntry(scrollable_frame_Main, width=310)
    main_entry_datumipotpis.grid(column=4, row=i+1, padx=0, pady=0)
    row.append(main_entry_datumipotpis)

    main_add_all_list.append(row)

    i += 1

    
def main_delete_row():
    global i
    if main_add_all_list:
        last_row_widgets = main_add_all_list.pop()  # Remove the last row's widgets from the list
        for widget in last_row_widgets.values():
            widget.destroy()  # Destroy each widget in the row
        i -= 1
    else:
        tkinter.messagebox.showinfo("Error","Nije moguce izbrisati pocetni red")

def back_add_row():
    
    global j
    back_checkbox = ctk.CTkCheckBox(scrollable_frame_Back,text=None,fg_color="#37CB56",hover_color="#176828")
    back_checkbox.grid(column=0,row=j+1,padx=0,sticky="w")
    
    back_entry_datum = ctk.CTkEntry(scrollable_frame_Back,width=300)
    back_entry_datum.grid(column=1,row=j+1,padx=0,pady=0,sticky="w")

    back_entry_br_ugovora = ctk.CTkEntry(scrollable_frame_Back,width=170)
    back_entry_br_ugovora.grid(column=2,row=j+1,padx=0,pady=0)

    back_entry_br_fakture = ctk.CTkEntry(scrollable_frame_Back,width=170)
    back_entry_br_fakture.grid(column=3,row=j+1,padx=0)

    back_entry_iznos = ctk.CTkEntry(scrollable_frame_Back,width=150)
    back_entry_iznos.grid(column=4,row=j+1,padx=0,pady=0)
    
    back_entry_placeno_neplaceno = ctk.CTkEntry(scrollable_frame_Back,width=310)
    back_entry_placeno_neplaceno.grid(column=5,row=j+1,padx=0,pady=0)
    
    # Store references to the widgets of the row in a list
    back_row_widgets = [back_checkbox,back_entry_datum,back_entry_br_ugovora,
                   back_entry_br_fakture,back_entry_iznos,back_entry_placeno_neplaceno]
    back_add_all_list.append(back_row_widgets)
    
    j += 1

def back_delete_row():
    global j
    if back_add_all_list:
        last_row_widgets = back_add_all_list.pop()  # Remove the last row's widgets from the list
        for widget in last_row_widgets:
            widget.destroy()  # Destroy each widget in the row
        j -= 1
    else:
        tkinter.messagebox.showinfo("Error","Nije moguce izbrisati pocetni red")

def middle_add_row():
    global k
    
    middle_checkbox = ctk.CTkCheckBox(scrollable_frame_Middle,text=None,fg_color="#37CB56",hover_color="#176828")
    middle_checkbox.grid(column=0,row=k+1,ipadx=0,sticky="w")
    
    middle_entry_primatelj = ctk.CTkEntry(scrollable_frame_Middle,width=105)
    middle_entry_primatelj.grid(column=1,row=k+1,ipadx=0,pady=0,sticky="w")

    middle_entry_posiljatelj = ctk.CTkEntry(scrollable_frame_Middle,width=105)
    middle_entry_posiljatelj.grid(column=2,row=k+1,ipadx=0,pady=0)

    middle_entry_broj_ugovora = ctk.CTkEntry(scrollable_frame_Middle,width=145)
    middle_entry_broj_ugovora.grid(column=3,row=k+1,ipadx=0,pady=0)

    middle_entry_iznos_potrazivanja = ctk.CTkEntry(scrollable_frame_Middle,width=195)
    middle_entry_iznos_potrazivanja.grid(column=4,row=k+1,ipadx=0,pady=0)

    middle_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_Middle,width=140)
    middle_entry_iznos_otkupa.grid(column=5,row=k+1,ipadx=0,pady=0)

    middle_entry_broj_fakture = ctk.CTkEntry(scrollable_frame_Middle,width=130)
    middle_entry_broj_fakture.grid(column=6,row=k+1,ipadx=0,pady=0)

    middle_entry_datum_stavljanja_na_placanje = ctk.CTkEntry(scrollable_frame_Middle,width=300)
    middle_entry_datum_stavljanja_na_placanje.grid(column=7,row=k+1,ipadx=0,pady=0)

    middle_row_widgets = [middle_checkbox,middle_entry_primatelj,middle_entry_posiljatelj,
                        middle_entry_broj_ugovora,middle_entry_iznos_potrazivanja,
                        middle_entry_iznos_otkupa,middle_entry_broj_fakture,
                        middle_entry_datum_stavljanja_na_placanje]
    middle_add_all_list.append(middle_row_widgets)
    
    k += 1

def middle_delete_row():
    global k
    if middle_add_all_list:
        last_row_widgets = middle_add_all_list.pop()  # Remove the last row's widgets from the list
        for widget in last_row_widgets:
            widget.destroy()  # Destroy each widget in the row
        k -= 1
    else:
        tkinter.messagebox.showinfo("Error","Nije moguce izbrisati pocetni red")

def save_as_file():
    
    pass    

def checkbox_check(kwargs):
    if kwargs["checked"].get():
        for item in kwargs["row"]:
            item.configure(fg_color="#37CB56")
    else:
        for item in kwargs["row"]:
            item.configure(fg_color="white")

def save_the_state():
    main_entry_datumipotpis_data =  main_entry_datumipotpis.get()
    main_entry_datum_data = main_entry_datum.get()
    main_entry_otkup_data = main_entry_otkup.get()
    main_entry_ustup_data = main_entry_ustup.get()
    
    
    
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

main_row = []

main_entry_datum = ctk.CTkEntry(scrollable_frame_Main,width=100)
main_entry_datum.grid(column=1,row=1,ipadx=0,pady=(5,0),sticky="w")
main_row.append(main_entry_datum)

main_entry_otkup = ctk.CTkEntry(scrollable_frame_Main,width=340)
main_entry_otkup.grid(column=2,row=1,ipadx=0,pady=(5,0))
main_row.append(main_entry_otkup)

main_entry_ustup = ctk.CTkEntry(scrollable_frame_Main,width=260)
main_entry_ustup.grid(column=3,row=1,ipadx=0,pady=(5,0))
main_row.append(main_entry_ustup)

main_entry_datumipotpis = ctk.CTkEntry(scrollable_frame_Main,width=310)
main_entry_datumipotpis.grid(column=4,row=1,ipadx=0,pady=(5,0))
main_row.append(main_entry_datumipotpis)

#endregion

#region Checkbox Main Office
cbox_var = tkinter.IntVar()
kwargs = {}
kwargs["checked"] = cbox_var
kwargs["row"] = main_row
main_checkbox = ctk.CTkCheckBox(master=scrollable_frame_Main,text=None,hover_color="#176828",fg_color="#37CB56",
                                onvalue=1, offvalue=0,
                                variable=cbox_var, command=lambda kwargs=kwargs: checkbox_check(kwargs))
main_checkbox.grid(column=0,row=1,padx=0,sticky="w")
main_row.append(main_checkbox)
#endregion

#region gumb za dodavanje/oduzimanje reda Main Officed
main_button_add_row = ctk.CTkButton(fixed_frame_main_office,text="+",
                               width=10,
                               corner_radius=120,
                               anchor="w",
                               command=add_row)
main_button_add_row.grid(column=0,row=0,sticky="w")

main_button_delete_row = ctk.CTkButton(fixed_frame_main_office,text="-",
                               width=30,
                               corner_radius=120,
                               command=main_delete_row)
main_button_delete_row.grid(column=0,row=0,padx=40)
#endregion





#region Label Back office

back_label_datum = ctk.CTkLabel(fixed_frame_back_office,
                           text="Datum dospijeca placanja",
                           font=("Arial",24))
back_label_datum.grid(column=1,row=0,ipadx=10)

back_label_br_ugovora = ctk.CTkLabel(fixed_frame_back_office,
                           text="Broj ugovora",
                           font=("Arial",24))
back_label_br_ugovora.grid(column=2,row=0,ipadx=40)

back_label_br_fakture = ctk.CTkLabel(fixed_frame_back_office,
                           text="Broj fakture",
                           font=("Arial",24))
back_label_br_fakture.grid(column=3,row=0,ipadx=10)

back_label_iznos = ctk.CTkLabel(fixed_frame_back_office,
                           text="Iznos",
                           font=("Arial",24))
back_label_iznos.grid(column=4,row=0,ipadx=100)

back_label_placeno_neplaceno = ctk.CTkLabel(fixed_frame_back_office,
                           text="Placeno/Neplaceno",
                           font=("Arial",24))
back_label_placeno_neplaceno.grid(column=5,row=0,ipadx=30)

#endregion

#region Entry Back Office
back_entry_datum = ctk.CTkEntry(scrollable_frame_Back,width=300)
back_entry_datum.grid(column=1,row=1,padx=0,pady=(5,0),sticky="w")

back_entry_br_ugovora = ctk.CTkEntry(scrollable_frame_Back,width=170)
back_entry_br_ugovora.grid(column=2,row=1,padx=0,pady=(5,0))

back_entry_br_fakture = ctk.CTkEntry(scrollable_frame_Back,width=170)
back_entry_br_fakture.grid(column=3,row=1,padx=0,pady=(5,0))

back_entry_iznos = ctk.CTkEntry(scrollable_frame_Back,width=150)
back_entry_iznos.grid(column=4,row=1,padx=0,pady=(5,0))

back_entry_placeno_neplaceno = ctk.CTkEntry(scrollable_frame_Back,width=310)
back_entry_placeno_neplaceno.grid(column=5,row=1,padx=0,pady=(5,0))
#endregion

#region Checkbox Back Office
back_checkbox = ctk.CTkCheckBox(scrollable_frame_Back,text=None,fg_color="#37CB56",hover_color="#176828")
back_checkbox.grid(column=0,row=1,padx=0,sticky="w")
#endregion

#region gumb za dodavanje/oduzimanje reda Back Office
back_button_add_row = ctk.CTkButton(fixed_frame_back_office,text="+",
                               width=10,
                               corner_radius=120,
                               anchor="w",
                               command=back_add_row)
back_button_add_row.grid(column=0,row=0,sticky="w")

back_button_delete_row = ctk.CTkButton(fixed_frame_back_office,text="-",
                               width=30,
                               corner_radius=120,
                               command=back_delete_row)
back_button_delete_row.grid(column=0,row=0,padx=40)
#endregion




#region Label Middle Office
middle_label_primatelj = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Primatelj",
                           font=("Arial",24))
middle_label_primatelj.grid(column=1,row=0,padx=(0,5))

middle_label_posiljatelj = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Posiljatelj",
                           font=("Arial",24))
middle_label_posiljatelj.grid(column=2,row=0,ipadx=5)

middle_label_broj_ugovora = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Broj ugovora",
                           font=("Arial",24))
middle_label_broj_ugovora.grid(column=3,row=0,ipadx=5)

middle_label_iznos_potrazivanja = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Iznos potrazivanja",
                           font=("Arial",24))
middle_label_iznos_potrazivanja.grid(column=4,row=0,ipadx=5)

middle_label_iznos_otkupa = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Iznos otkupa",
                           font=("Arial",24))
middle_label_iznos_otkupa.grid(column=5,row=0,ipadx=5)

middle_label_broj_fakture = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Broj fakture",
                           font=("Arial",24))
middle_label_broj_fakture.grid(column=6,row=0,ipadx=5)

middle_label_datum_stavljanja_na_placanje = ctk.CTkLabel(fixed_frame_middle_office,
                                            text="Datum stavljanja na placanje",
                                            font=("Arial",24))
middle_label_datum_stavljanja_na_placanje.grid(column=7,row=0,ipadx=5)
#endregion

#region Entry Middle Office

middle_entry_primatelj = ctk.CTkEntry(scrollable_frame_Middle,width=105)
middle_entry_primatelj.grid(column=1,row=1,sticky="w",ipady=0,padx=0,pady=0)

middle_entry_posiljatelj = ctk.CTkEntry(scrollable_frame_Middle,width=105)
middle_entry_posiljatelj.grid(column=2,row=1,ipadx=0,ipady=0,padx=0,pady=0)

middle_entry_broj_ugovora = ctk.CTkEntry(scrollable_frame_Middle,width=145)
middle_entry_broj_ugovora.grid(column=3,row=1,ipadx=0,ipady=0,padx=0,pady=0)

middle_entry_iznos_potrazivanja = ctk.CTkEntry(scrollable_frame_Middle,width=195)
middle_entry_iznos_potrazivanja.grid(column=4,row=1,ipadx=0,ipady=0,padx=0,pady=0)

middle_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_Middle,width=140)
middle_entry_iznos_otkupa.grid(column=5,row=1,ipadx=0,ipady=0,padx=0,pady=0)

middle_entry_broj_fakture = ctk.CTkEntry(scrollable_frame_Middle,width=130)
middle_entry_broj_fakture.grid(column=6,row=1,ipadx=0,ipady=0,padx=0,pady=0)

middle_entry_datum_stavljanja_na_placanje = ctk.CTkEntry(scrollable_frame_Middle,width=300)
middle_entry_datum_stavljanja_na_placanje.grid(column=7,row=1,ipadx=0,ipady=0,padx=0,pady=0)

#endregion

#region Checkbox Middle Office

middle_checkbox = ctk.CTkCheckBox(scrollable_frame_Middle,text=None,fg_color="#37CB56",hover_color="#176828")
middle_checkbox.grid(column=0,row=1,ipadx=0,ipady=0,sticky="w")
#endregion

#region gumb za dodavanje/oduzimanje Middle reda Back Office
middle_button_add_row = ctk.CTkButton(fixed_frame_middle_office,text="+",
                               width=10,
                               corner_radius=120,
                               anchor="w",
                               command=middle_add_row)
middle_button_add_row.grid(column=0,row=0,sticky="w",ipadx=0,ipady=0)

middle_button_delete_row = ctk.CTkButton(fixed_frame_middle_office,text="-",
                               width=10,
                               corner_radius=20,
                               command=middle_delete_row)
middle_button_delete_row.grid(column=0,row=0,padx=40,ipadx=0,ipady=0)
#endregion



app.mainloop()