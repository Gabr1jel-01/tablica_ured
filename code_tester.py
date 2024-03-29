import tkinter as tk
from time import *
import customtkinter as ctk
import tkinter.messagebox
from tkinter import END
from tkcalendar import *
import os, json




ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.after(0, lambda:app.state('zoomed'))
#app.resizable(height=False,width=False)
app.title("Office")
#app.geometry("1280x800+400+50")


#region TabView
#ovdje sam kreirao tabView
tabView = ctk.CTkTabview(app)
tabView.pack(pady=0, padx=0, fill="both", expand=True)

#ovdje sam dodao cetiri taba
tabView.add("Main Office")
tabView.add("Middle Office")
tabView.add("Back Office")
tabView.add("Racunovodstvo1")
tabView.add("Racunovodstvo2")
tabView.add("Racunovodstvo3")
tabView.add("Datoteka")

#ovdje sam stavio da tab glavni izbornik bude prvi otvoren kada se pokrene aplikacija
tabView.set("Main Office")
#endregion



#region Fiksni Frameovi
#Fiksni frame Main Office
fixed_frame_main_office = ctk.CTkFrame(tabView.tab("Main Office"),height=35)
fixed_frame_main_office.pack(pady=5,padx=5,fill="both",anchor="center")
fixed_frame_main_office.grid_rowconfigure(0,weight=1)
#fiksni frame Middle Office
fixed_frame_middle_office = ctk.CTkFrame(tabView.tab("Middle Office"),height=35)
fixed_frame_middle_office.pack(pady=5,padx=5,fill="both")
#fiksni frame Back Office
fixed_frame_back_office = ctk.CTkFrame(tabView.tab("Back Office"),height=35)
fixed_frame_back_office.pack(pady=5,padx=5,fill="both")
#Fiksni frame Racunovodstvo1
fixed_frame_racunovodstvo1 = ctk.CTkFrame(tabView.tab("Racunovodstvo1"),height=35)
fixed_frame_racunovodstvo1.pack(pady=5,padx=5,fill="both")
#Fiksni frame Racunovodstvo2
fixed_frame_racunovodstvo2 = ctk.CTkFrame(tabView.tab("Racunovodstvo2"),height=35)
fixed_frame_racunovodstvo2.pack(pady=5,padx=5,fill="both")
#Fiskni frame Racunovodstvo3
fixed_frame_racunovodstvo3 = ctk.CTkFrame(tabView.tab("Racunovodstvo3"),height=35)
fixed_frame_racunovodstvo3.pack(pady=5,padx=5,fill="both")
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
#Scrollable frame Racunovodstvo1
scrollable_frame_racunovodstvo1 = ctk.CTkScrollableFrame(tabView.tab("Racunovodstvo1"))
scrollable_frame_racunovodstvo1.pack(pady=5, padx=5, fill="both", expand=True)
#Scrollable frame Racunovodstvo2
scrollable_frame_racunovodstvo2 = ctk.CTkScrollableFrame(tabView.tab("Racunovodstvo2"))
scrollable_frame_racunovodstvo2.pack(pady=5, padx=5, fill="both", expand=True)
#Scrollable frame Racunovodstvo3
scrollable_frame_racunovodstvo3 = ctk.CTkScrollableFrame(tabView.tab("Racunovodstvo3"))
scrollable_frame_racunovodstvo3.pack(pady=5, padx=5, fill="both", expand=True)
#endregion

#region Liste
main_add_all_list = [[]]
middle_add_all_list = [[]]
back_add_all_list = [[]]
racunovodstvo1_add_all_list = [[]]
racunovodstvo2_add_all_list = [[]]
racunovodstvo3_add_all_list = [[]]

main_all_entries_list = []
middle_all_entries_list = []
back_all_entries_list = []
racunovodstvo1_all_entries_list = []
racunovodstvo2_all_entries_list = []
racunovodstvo3_all_entries_list = []



#endregion

#region Konstante
i = 1
j = 1
k = 1
o = 1
m = 1
n = 1
#endregion


#region FUNKCIJE 
"""
def pick_date(event):
    
    global cal, date_window
    
    date_window = ctk.CTkToplevel()
    date_window.grab_set()
    date_window.title("Izaberi datum")
    date_window.geometry("300x230+300+300")
    cal = Calendar(date_window, selectmode="day", date_pattern = "mm/dd/yy", font=("Arial",8))
    cal.place(x=0,y=0)
    
    submit_button = ctk.CTkButton(date_window,text="Submit",
                                  height=20,
                                  width=60)
    submit_button.place(x=150,y=200)
    for i in range(6):
        cal._week_nbs[i].destroy()

def grab_date():
    main_entry_datum.delete(0, END)
    main_entry_datum.insert(0, cal.get_date())
    date_window.destroy()
    
    
    pass
"""

def main_add_row():
    global i
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
                               command=lambda kwargs=kwargs: checkbox_check(kwargs),border_color="black")
    checkbox.grid(column=0, row=i+1, sticky="w")
    row.append(checkbox)
    
    

    entry_datum = ctk.CTkEntry(scrollable_frame_Main, width=150,border_color="black")
    entry_datum.grid(column=1, row=i+1, padx=0, pady=0, sticky="w")
    row.append(entry_datum)
    main_all_entries_list.append(entry_datum)

    main_entry_otkup = ctk.CTkEntry(scrollable_frame_Main, width=560,border_color="black")
    main_entry_otkup.grid(column=2, row=i+1, padx=0, pady=0)
    row.append(main_entry_otkup)
    main_all_entries_list.append(main_entry_otkup)

    main_entry_ustup = ctk.CTkEntry(scrollable_frame_Main, width=500,border_color="black")
    main_entry_ustup.grid(column=3, row=i+1, padx=0)
    row.append(main_entry_ustup)
    main_all_entries_list.append(main_entry_ustup)

    main_entry_datumipotpis = ctk.CTkEntry(scrollable_frame_Main, width=500,border_color="black")
    main_entry_datumipotpis.grid(column=4, row=i+1, padx=0, pady=0)
    row.append(main_entry_datumipotpis)
    main_all_entries_list.append(main_entry_datumipotpis)

    main_add_all_list.append(row)
    i += 1

def main_delete_row():
    global i
    if main_add_all_list:
        last_row_widgets = main_add_all_list.pop()  # Remove the last row's widgets from the list
        for widget in last_row_widgets:
            widget.destroy()  # Destroy each widget in the row
        i -= 1
    else:
        tkinter.messagebox.showinfo("Error","Nije moguće izbrisati početni red")
    
    for _ in range(4):
        main_all_entries_list.pop()

def back_add_row():
    
    global j
    row = []
    cbox_var = tkinter.IntVar()
    kwargs = {}
    kwargs["checked"] = cbox_var
    kwargs["row"] = row
    
    
    
    back_checkbox = ctk.CTkCheckBox(scrollable_frame_Back,text=None,fg_color="#37CB56",hover_color="#176828", 
                                    onvalue=1,
                                    variable=cbox_var,
                                    offvalue=0,
                                    command=lambda kwargs=kwargs: checkbox_check(kwargs),border_color="black")
    back_checkbox.grid(column=0,row=j+1,padx=0,sticky="w")
    row.append(back_checkbox)
    
    
    back_entry_datum = ctk.CTkEntry(scrollable_frame_Back,width=350,border_color="black")
    back_entry_datum.grid(column=1,row=j+1,padx=0,pady=0,sticky="w")
    row.append(back_entry_datum)
    back_all_entries_list.append(back_entry_datum)
    
    back_entry_br_ugovora = ctk.CTkEntry(scrollable_frame_Back,width=300,border_color="black")
    back_entry_br_ugovora.grid(column=2,row=j+1,padx=0,pady=0)
    row.append(back_entry_br_ugovora)
    back_all_entries_list.append(back_entry_br_ugovora)

    back_entry_br_fakture = ctk.CTkEntry(scrollable_frame_Back,width=300,border_color="black")
    back_entry_br_fakture.grid(column=3,row=j+1,padx=0)
    row.append(back_entry_br_fakture)
    back_all_entries_list.append(back_entry_br_fakture)
    
    back_entry_iznos = ctk.CTkEntry(scrollable_frame_Back,width=350,border_color="black")
    back_entry_iznos.grid(column=4,row=j+1,padx=0,pady=0)
    row.append(back_entry_iznos)
    back_all_entries_list.append(back_entry_iznos)
    
    back_entry_placeno_neplaceno = ctk.CTkEntry(scrollable_frame_Back,width=410,border_color="black")
    back_entry_placeno_neplaceno.grid(column=5,row=j+1,padx=0,pady=0)
    row.append(back_entry_placeno_neplaceno)
    back_all_entries_list.append(back_entry_placeno_neplaceno)
    
    # Store references to the widgets of the row in a list
    back_add_all_list.append(row)
    
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
    for _ in range(5):
        back_all_entries_list.pop()
    
def middle_add_row():
    global k
    
    row = []
    cbox_var = tkinter.IntVar()
    kwargs = {}
    kwargs["checked"] = cbox_var
    kwargs["row"] = row
    
    middle_checkbox = ctk.CTkCheckBox(scrollable_frame_Middle,text=None,fg_color="#37CB56",hover_color="#176828",
                                      onvalue=1,
                                    variable=cbox_var,
                                    offvalue=0,
                                    command=lambda kwargs=kwargs: checkbox_check(kwargs),border_color="black")
    middle_checkbox.grid(column=0,row=k+1,ipadx=0,sticky="w")
    row.append(middle_checkbox)
    
    
    middle_entry_primatelj = ctk.CTkEntry(scrollable_frame_Middle,width=140,border_color="black")
    middle_entry_primatelj.grid(column=1,row=k+1,ipadx=0,pady=0,sticky="w")
    row.append(middle_entry_primatelj)
    middle_all_entries_list.append(middle_entry_primatelj)

    middle_entry_posiljatelj = ctk.CTkEntry(scrollable_frame_Middle,width=210,border_color="black")
    middle_entry_posiljatelj.grid(column=2,row=k+1,ipadx=0,pady=0)
    row.append(middle_entry_posiljatelj)
    middle_all_entries_list.append(middle_entry_posiljatelj)

    middle_entry_broj_ugovora = ctk.CTkEntry(scrollable_frame_Middle,width=220,border_color="black")
    middle_entry_broj_ugovora.grid(column=3,row=k+1,ipadx=0,pady=0)
    row.append(middle_entry_broj_ugovora)
    middle_all_entries_list.append(middle_entry_broj_ugovora)

    middle_entry_iznos_potrazivanja = ctk.CTkEntry(scrollable_frame_Middle,width=300,border_color="black")
    middle_entry_iznos_potrazivanja.grid(column=4,row=k+1,ipadx=0,pady=0)
    row.append(middle_entry_iznos_potrazivanja)
    middle_all_entries_list.append(middle_entry_iznos_potrazivanja)

    middle_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_Middle,width=270,border_color="black")
    middle_entry_iznos_otkupa.grid(column=5,row=k+1,ipadx=0,pady=0)
    row.append(middle_entry_iznos_otkupa)
    middle_all_entries_list.append(middle_entry_iznos_otkupa)

    middle_entry_broj_fakture = ctk.CTkEntry(scrollable_frame_Middle,width=200,border_color="black")
    middle_entry_broj_fakture.grid(column=6,row=k+1,ipadx=0,pady=0)
    row.append(middle_entry_broj_fakture)
    middle_all_entries_list.append(middle_entry_broj_fakture)

    middle_entry_datum_stavljanja_na_placanje = ctk.CTkEntry(scrollable_frame_Middle,width=400,border_color="black")
    middle_entry_datum_stavljanja_na_placanje.grid(column=7,row=k+1,ipadx=0,pady=0)
    row.append(middle_entry_datum_stavljanja_na_placanje)
    middle_all_entries_list.append(middle_entry_datum_stavljanja_na_placanje)

    middle_add_all_list.append(row)
    
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
    for _ in range(7):
        middle_all_entries_list.pop()   

def checkbox_check(kwargs):
    if kwargs["checked"].get():
        for item in kwargs["row"]:
            item.configure(fg_color="#37CB56")
    else:
        for item in kwargs["row"]:
            item.configure(fg_color="white")

def racunovodstvo1_add_row():
    
    global o
    row = []

    cbox_var = tkinter.IntVar()
    kwargs = {}
    kwargs["checked"] = cbox_var
    kwargs["row"] = row
    checkbox = ctk.CTkCheckBox(scrollable_frame_racunovodstvo1,
                               onvalue=1,
                               variable=cbox_var,
                               offvalue=0,
                               text=None,
                               fg_color="#37CB56",
                               hover_color="#176828",
                               command=lambda kwargs=kwargs: checkbox_check(kwargs),border_color="black")
    checkbox.grid(column=0, row=o+1, padx=0, sticky="w")
    row.append(checkbox)
    
    racunovodstvo_entry_naziv_prim_plat = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=370,border_color="black")
    racunovodstvo_entry_naziv_prim_plat.grid(column=1,row=o+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_naziv_prim_plat)

    racunovodstvo_entry_naz_izda_rac = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=300,border_color="black")
    racunovodstvo_entry_naz_izda_rac.grid(column=2,row=o+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_naz_izda_rac)

    racunovodstvo_entry_uvjeti_stand_pos = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=260,border_color="black")
    racunovodstvo_entry_uvjeti_stand_pos.grid(column=3,row=o+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_uvjeti_stand_pos)

    racunovodstvo_entry_datum_otkupa = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=190,border_color="black")
    racunovodstvo_entry_datum_otkupa.grid(column=4,row=o+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_datum_otkupa)

    racunovodstvo_entry_datum_dospijeca = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=220,border_color="black")
    racunovodstvo_entry_datum_dospijeca.grid(column=5,row=o+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_datum_dospijeca)

    racunovodstvo_entry_iznos_racuna = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=180,border_color="black")
    racunovodstvo_entry_iznos_racuna.grid(column=6,row=o+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_iznos_racuna)

    racunovodstvo_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=180,border_color="black")
    racunovodstvo_entry_iznos_otkupa.grid(column=7,row=o+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_iznos_otkupa)
    
    
    racunovodstvo1_add_all_list.append(row)
    o += 1
    
def racunovodstvo1_delete_row():
    
    global o
    
    if racunovodstvo1_add_all_list:
        last_row_widgets = racunovodstvo1_add_all_list.pop()  # Remove the last row's widgets from the list
        for widget in last_row_widgets:
            widget.destroy()  # Destroy each widget in the row
        o -= 1
    else:
        tkinter.messagebox.showinfo("Error","Nije moguće izbrisati početni red")
    
    for _ in range(7):
        racunovodstvo1_all_entries_list.pop()
    
def racunovodstvo2_add_row():
    
    global m
    row = []

    cbox_var = tkinter.IntVar()
    kwargs = {}
    kwargs["checked"] = cbox_var
    kwargs["row"] = row
    checkbox = ctk.CTkCheckBox(scrollable_frame_racunovodstvo2,
                               onvalue=1,
                               variable=cbox_var,
                               offvalue=0,
                               text=None,
                               fg_color="#37CB56",
                               hover_color="#176828",
                               command=lambda kwargs=kwargs: checkbox_check(kwargs),border_color="black")
    checkbox.grid(column=0, row=m+1, padx=0, sticky="w")
    row.append(checkbox)
    
    racunovodstvo_entry_diskont_bruto = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=190,border_color="black")
    racunovodstvo_entry_diskont_bruto.grid(column=1,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_diskont_bruto)
    racunovodstvo2_all_entries_list.append(racunovodstvo_entry_diskont_bruto)

    racunovodstvo_entry_diskont_netto = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=200,border_color="black")
    racunovodstvo_entry_diskont_netto.grid(column=2,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_diskont_netto)
    racunovodstvo2_all_entries_list.append(racunovodstvo_entry_diskont_netto)

    racunovodstvo_entry_diskont_godisnji_trosak = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=200,border_color="black")
    racunovodstvo_entry_diskont_godisnji_trosak.grid(column=3,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_diskont_godisnji_trosak)
    racunovodstvo2_all_entries_list.append(racunovodstvo_entry_diskont_godisnji_trosak)

    racunovodstvo_entry_ex_ante = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=430,border_color="black")
    racunovodstvo_entry_ex_ante.grid(column=4,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_ex_ante)
    racunovodstvo2_all_entries_list.append(racunovodstvo_entry_ex_ante)

    racunovodstvo_entry_razlika = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=120,border_color="black")
    racunovodstvo_entry_razlika.grid(column=5,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_razlika)
    racunovodstvo2_all_entries_list.append(racunovodstvo_entry_razlika)

    racunovodstvo_entry_prihod = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=120,border_color="black")
    racunovodstvo_entry_prihod.grid(column=6,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_prihod)
    racunovodstvo2_all_entries_list.append(racunovodstvo_entry_prihod)

    racunovodstvo_entry_pdv = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=100,border_color="black")
    racunovodstvo_entry_pdv.grid(column=7,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_pdv)
    racunovodstvo2_all_entries_list.append(racunovodstvo_entry_pdv)

    racunovodstvo_entry_cisti_prihod = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=400,border_color="black")
    racunovodstvo_entry_cisti_prihod.grid(column=8,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_cisti_prihod)
    racunovodstvo2_all_entries_list.append(racunovodstvo_entry_cisti_prihod)
    
    racunovodstvo2_add_all_list.append(row)
    
    m += 1

def racunovodstvo2_delete_row():
    global m
    
    if racunovodstvo2_add_all_list:
        last_row_widgets = racunovodstvo2_add_all_list.pop()  # Remove the last row's widgets from the list
        for widget in last_row_widgets:
            widget.destroy()  # Destroy each widget in the row
        m -= 1
    else:
        tkinter.messagebox.showinfo("Error","Nije moguće izbrisati početni red")
    
    for _ in range(8):
        racunovodstvo2_all_entries_list.pop()

def racunovodstvo3_add_row():
    global n
    row = []

    cbox_var = tkinter.IntVar()
    kwargs = {}
    kwargs["checked"] = cbox_var
    kwargs["row"] = row
    checkbox = ctk.CTkCheckBox(scrollable_frame_racunovodstvo3,
                               onvalue=1,
                               variable=cbox_var,
                               offvalue=0,
                               text=None,
                               fg_color="#37CB56",
                               hover_color="#176828",
                               command=lambda kwargs=kwargs: checkbox_check(kwargs),border_color="black")
    checkbox.grid(column=0, row=n+1, padx=0, sticky="w")
    row.append(checkbox)
    
    racunovodstvo_entry_ex_post = ctk.CTkEntry(scrollable_frame_racunovodstvo3,width=430,border_color="black")
    racunovodstvo_entry_ex_post.grid(column=1,row=n+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_ex_post)
    racunovodstvo3_all_entries_list.append(racunovodstvo_entry_ex_post)

    racunovodstvo_entry_kasni_iza_valute = ctk.CTkEntry(scrollable_frame_racunovodstvo3,width=250,border_color="black")
    racunovodstvo_entry_kasni_iza_valute.grid(column=2,row=n+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_kasni_iza_valute)
    racunovodstvo3_all_entries_list.append(racunovodstvo_entry_kasni_iza_valute)

    racunovodstvo_entry_godisnji_ako_plati_valuti = ctk.CTkEntry(scrollable_frame_racunovodstvo3,width=550,border_color="black")
    racunovodstvo_entry_godisnji_ako_plati_valuti.grid(column=3,row=n+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_godisnji_ako_plati_valuti)
    racunovodstvo3_all_entries_list.append(racunovodstvo_entry_godisnji_ako_plati_valuti)

    racunovodstvo_entry_stvarni_godisnji_trosak = ctk.CTkEntry(scrollable_frame_racunovodstvo3,width=460,border_color="black")
    racunovodstvo_entry_stvarni_godisnji_trosak.grid(column=4,row=n+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_stvarni_godisnji_trosak)
    racunovodstvo3_all_entries_list.append(racunovodstvo_entry_stvarni_godisnji_trosak)
    
    racunovodstvo3_add_all_list.append(row)
    
    n += 1
    
    
    pass

def racunovodstvo3_delete_row():
    global n
    
    if racunovodstvo3_add_all_list:
        last_row_widgets = racunovodstvo3_add_all_list.pop()  # Remove the last row's widgets from the list
        for widget in last_row_widgets:
            widget.destroy()  # Destroy each widget in the row
        n -= 1
    else:
        tkinter.messagebox.showinfo("Error","Nije moguće izbrisati početni red")
    
    for _ in range(4):
        racunovodstvo3_all_entries_list.pop()    

def save_func():
    with open("widgetsDB/main_widgets_database", "w") as file:
            main_number = len(main_add_all_list)
            json.dump(main_number, file)
            
    loop_data_list = []
    main_entry_counter = 1
    for entry in main_all_entries_list:
        data1 = {
            f"entry{main_entry_counter}": entry.get()
            }
        loop_data_list.append(data1)
        main_entry_counter += 1
        
    with open("user_input_in_widgetsDB/user_entry_data.json", "w") as file:
            json.dump(loop_data_list, file)
          
            
#########################################################################################################
        
    with open("widgetsDB/middle_widgets_database", "w") as file:
            middle_number = len(middle_add_all_list)
            json.dump(middle_number, file)
            
    loop_data_list_middle = []
    middle_entry_counter = 1
    for entry in middle_all_entries_list:
        data2 = {
            f"entry{middle_entry_counter}": entry.get()
            }
        loop_data_list_middle.append(data2)
        middle_entry_counter += 1
        
    with open("user_input_in_widgetsDB/middle_user_entry_data.json", "w") as file:
            json.dump(loop_data_list_middle, file)        
            
#########################################################################################################          
    with open("widgetsDB/back_widgets_database", "w") as file:
            back_number = len(back_add_all_list)
            json.dump(back_number, file)
    
    loop_data_list_back = []
    back_entry_counter = 1
    for entry in back_all_entries_list:
        data3 = {
            f"entry{back_entry_counter}": entry.get()
            }
        loop_data_list_back.append(data3)
        back_entry_counter += 1
        
    with open("user_input_in_widgetsDB/back_user_entry_data.json", "w") as file:
            json.dump(loop_data_list_back, file)
#########################################################################################################
    with open("widgetsDB/racunovodstvo1_widgets_database", "w") as file:
            racunovodstvo1_number = len(racunovodstvo1_add_all_list)
            json.dump(racunovodstvo1_number, file)
    
    loop_data_list_racunovodstvo1 = []
    racunovodstvo1_entry_counter = 1
    for entry in racunovodstvo1_all_entries_list:
        data4 = {
            f"entry{racunovodstvo1_entry_counter}": entry.get()
            }
        loop_data_list_racunovodstvo1.append(data4)
        racunovodstvo1_entry_counter += 1
        
    with open("user_input_in_widgetsDB/racunovodstvo1_user_entry_data.json", "w") as file:
            json.dump(loop_data_list_racunovodstvo1, file)          

#########################################################################################################        
    with open("widgetsDB/racunovodstvo2_widgets_database", "w") as file:
            racunovodstvo2_number = len(racunovodstvo2_add_all_list)
            json.dump(racunovodstvo2_number, file)
            
    loop_data_list_racunovodstvo2 = []
    racunovodstvo2_entry_counter = 1
    for entry in racunovodstvo2_all_entries_list:
        data5 = {
            f"entry{racunovodstvo2_entry_counter}": entry.get()
            }
        loop_data_list_racunovodstvo2.append(data5)
        racunovodstvo2_entry_counter += 1
        
    with open("user_input_in_widgetsDB/racunovodstvo2_user_entry_data.json", "w") as file:
            json.dump(loop_data_list_racunovodstvo2, file)

#########################################################################################################
        
    with open("widgetsDB/racunovodstvo3_widgets_database", "w") as file:
            number = len(racunovodstvo3_add_all_list)
            json.dump(number, file)
            
    loop_data_list_racunovodstvo3 = []
    racunovodstvo3_entry_counter = 1
    for entry in racunovodstvo3_all_entries_list:
        data6 = {
            f"entry{racunovodstvo3_entry_counter}": entry.get()
            }
        loop_data_list_racunovodstvo3.append(data6)
        racunovodstvo3_entry_counter += 1
        
    with open("user_input_in_widgetsDB/racunovodstvo3_user_entry_data.json", "w") as file:
            json.dump(loop_data_list_racunovodstvo3, file)

#########################################################################################################
   
def load_func():
    
    try:
        with open("widgetsDB/main_widgets_database", "r") as file:
            loaded_data_main = json.load(file) - 1
            
            for y in range(loaded_data_main):
                global i
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
                                        command=lambda kwargs=kwargs: checkbox_check(kwargs),border_color="black")
                checkbox.grid(column=0, row=i+1, sticky="w")
                row.append(checkbox)
                
                entry_datum = ctk.CTkEntry(scrollable_frame_Main, width=150,border_color="black")
                entry_datum.grid(column=1, row=i+1, padx=0, pady=0, sticky="w")
                row.append(entry_datum)
                main_all_entries_list.append(entry_datum)
                
                main_entry_otkup = ctk.CTkEntry(scrollable_frame_Main, width=560,border_color="black")
                main_entry_otkup.grid(column=2, row=i+1, padx=0, pady=0)
                row.append(main_entry_otkup)
                main_all_entries_list.append(main_entry_otkup)

                main_entry_ustup = ctk.CTkEntry(scrollable_frame_Main, width=500,border_color="black")
                main_entry_ustup.grid(column=3, row=i+1, padx=0)
                row.append(main_entry_ustup)
                main_all_entries_list.append(main_entry_ustup)
                
                main_entry_datumipotpis = ctk.CTkEntry(scrollable_frame_Main, width=500,border_color="black")
                main_entry_datumipotpis.grid(column=4, row=i+1, padx=0, pady=0)
                row.append(main_entry_datumipotpis)
                main_all_entries_list.append(main_entry_datumipotpis)
            
                
                main_add_all_list.append(row)
                i += 1            
        if not os.path.exists("user_input_in_widgetsDB/user_entry_data.json"):
            return  # Return if the file doesn't exist

        with open("user_input_in_widgetsDB/user_entry_data.json", "r") as file:
            entry_data_list = json.load(file)

        main_entry_counter = 1
        for entry_data in entry_data_list:
            entry_key = f"entry{main_entry_counter}"
            if entry_key in entry_data:
                main_all_entries_list[main_entry_counter - 1].insert(0, entry_data[entry_key])
            main_entry_counter += 1
        
#########################################################################################################
        
        with open("widgetsDB/middle_widgets_database", "r") as file:
            loaded_data_middle = json.load(file) - 1
            
            for y in range(loaded_data_middle):
                global k
    
                row = []
                cbox_var = tkinter.IntVar()
                kwargs = {}
                kwargs["checked"] = cbox_var
                kwargs["row"] = row
                
                middle_checkbox = ctk.CTkCheckBox(scrollable_frame_Middle,text=None,fg_color="#37CB56",hover_color="#176828",
                                                onvalue=1,
                                                variable=cbox_var,
                                                offvalue=0,
                                                command=lambda kwargs=kwargs: checkbox_check(kwargs),border_color="black")
                middle_checkbox.grid(column=0,row=k+1,ipadx=0,sticky="w")
                row.append(middle_checkbox)
                
                
                middle_entry_primatelj = ctk.CTkEntry(scrollable_frame_Middle,width=140,border_color="black")
                middle_entry_primatelj.grid(column=1,row=k+1,ipadx=0,pady=0,sticky="w")
                row.append(middle_entry_primatelj)
                middle_all_entries_list.append(middle_entry_primatelj)

                middle_entry_posiljatelj = ctk.CTkEntry(scrollable_frame_Middle,width=210,border_color="black")
                middle_entry_posiljatelj.grid(column=2,row=k+1,ipadx=0,pady=0)
                row.append(middle_entry_posiljatelj)
                middle_all_entries_list.append(middle_entry_posiljatelj)

                middle_entry_broj_ugovora = ctk.CTkEntry(scrollable_frame_Middle,width=220,border_color="black")
                middle_entry_broj_ugovora.grid(column=3,row=k+1,ipadx=0,pady=0)
                row.append(middle_entry_broj_ugovora)
                middle_all_entries_list.append(middle_entry_broj_ugovora)

                middle_entry_iznos_potrazivanja = ctk.CTkEntry(scrollable_frame_Middle,width=300,border_color="black")
                middle_entry_iznos_potrazivanja.grid(column=4,row=k+1,ipadx=0,pady=0)
                row.append(middle_entry_iznos_potrazivanja)
                middle_all_entries_list.append(middle_entry_iznos_potrazivanja)

                middle_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_Middle,width=270,border_color="black")
                middle_entry_iznos_otkupa.grid(column=5,row=k+1,ipadx=0,pady=0)
                row.append(middle_entry_iznos_otkupa)
                middle_all_entries_list.append(middle_entry_iznos_otkupa)

                middle_entry_broj_fakture = ctk.CTkEntry(scrollable_frame_Middle,width=200,border_color="black")
                middle_entry_broj_fakture.grid(column=6,row=k+1,ipadx=0,pady=0)
                row.append(middle_entry_broj_fakture)
                middle_all_entries_list.append(middle_entry_broj_fakture)

                middle_entry_datum_stavljanja_na_placanje = ctk.CTkEntry(scrollable_frame_Middle,width=400,border_color="black")
                middle_entry_datum_stavljanja_na_placanje.grid(column=7,row=k+1,ipadx=0,pady=0)
                row.append(middle_entry_datum_stavljanja_na_placanje)
                middle_all_entries_list.append(middle_entry_datum_stavljanja_na_placanje)

        
                middle_add_all_list.append(row)
                
                k += 1
        if not os.path.exists("user_input_in_widgetsDB/middle_user_entry_data.json"):
            return  # Return if the file doesn't exist

        with open("user_input_in_widgetsDB/middle_user_entry_data.json", "r") as file:
            entry_data_list = json.load(file)

        middle_entry_counter = 1
        for entry_data in entry_data_list:
            entry_key = f"entry{middle_entry_counter}"
            if entry_key in entry_data:
                middle_all_entries_list[middle_entry_counter - 1].insert(0, entry_data[entry_key])
            middle_entry_counter += 1
            
            
            
#########################################################################################################
              
        with open("widgetsDB/back_widgets_database", "r") as file:
            loaded_data_back = json.load(file) - 1
            
            for y in range(loaded_data_back):
                global j
                row = []
                cbox_var = tkinter.IntVar()
                kwargs = {}
                kwargs["checked"] = cbox_var
                kwargs["row"] = row
                
                
                
                back_checkbox = ctk.CTkCheckBox(scrollable_frame_Back,text=None,fg_color="#37CB56",hover_color="#176828", 
                                                onvalue=1,
                                                variable=cbox_var,
                                                offvalue=0,
                                                command=lambda kwargs=kwargs: checkbox_check(kwargs),border_color="black")
                back_checkbox.grid(column=0,row=j+1,padx=0,sticky="w")
                row.append(back_checkbox)
                
                
                back_entry_datum = ctk.CTkEntry(scrollable_frame_Back,width=350,border_color="black")
                back_entry_datum.grid(column=1,row=j+1,padx=0,pady=0,sticky="w")
                row.append(back_entry_datum)
                back_all_entries_list.append(back_entry_datum)
                
                back_entry_br_ugovora = ctk.CTkEntry(scrollable_frame_Back,width=300,border_color="black")
                back_entry_br_ugovora.grid(column=2,row=j+1,padx=0,pady=0)
                row.append(back_entry_br_ugovora)
                back_all_entries_list.append(back_entry_br_ugovora)

                back_entry_br_fakture = ctk.CTkEntry(scrollable_frame_Back,width=300,border_color="black")
                back_entry_br_fakture.grid(column=3,row=j+1,padx=0)
                row.append(back_entry_br_fakture)
                back_all_entries_list.append(back_entry_br_fakture)
                
                back_entry_iznos = ctk.CTkEntry(scrollable_frame_Back,width=350,border_color="black")
                back_entry_iznos.grid(column=4,row=j+1,padx=0,pady=0)
                row.append(back_entry_iznos)
                back_all_entries_list.append(back_entry_iznos)
                
                back_entry_placeno_neplaceno = ctk.CTkEntry(scrollable_frame_Back,width=410,border_color="black")
                back_entry_placeno_neplaceno.grid(column=5,row=j+1,padx=0,pady=0)
                row.append(back_entry_placeno_neplaceno)
                back_all_entries_list.append(back_entry_placeno_neplaceno)
                
                # Store references to the widgets of the row in a list
                
                back_add_all_list.append(row)
                
                j += 1
        
        if not os.path.exists("user_input_in_widgetsDB/back_user_entry_data.json"):
            return  # Return if the file doesn't exist

        with open("user_input_in_widgetsDB/back_user_entry_data.json", "r") as file:
            entry_data_list = json.load(file)

        back_entry_counter = 1
        for entry_data in entry_data_list:
            entry_key = f"entry{back_entry_counter}"
            if entry_key in entry_data:
                back_all_entries_list[back_entry_counter - 1].insert(0, entry_data[entry_key])
            back_entry_counter += 1
            
            
#########################################################################################################    
        
        with open("widgetsDB/racunovodstvo1_widgets_database", "r") as file:
            loaded_data = json.load(file) - 1
            
            for _ in range(loaded_data):
                global o
                row = []

                cbox_var = tkinter.IntVar()
                kwargs = {}
                kwargs["checked"] = cbox_var
                kwargs["row"] = row
                checkbox = ctk.CTkCheckBox(scrollable_frame_racunovodstvo1,
                                        onvalue=1,
                                        variable=cbox_var,
                                        offvalue=0,
                                        text=None,
                                        fg_color="#37CB56",
                                        hover_color="#176828",
                                        command=lambda kwargs=kwargs: checkbox_check(kwargs),border_color="black")
                checkbox.grid(column=0, row=o+1, padx=0, sticky="w")
                row.append(checkbox)
                
                racunovodstvo_entry_naziv_prim_plat = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=370,border_color="black")
                racunovodstvo_entry_naziv_prim_plat.grid(column=1,row=o+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_naziv_prim_plat)
                racunovodstvo1_all_entries_list.append(racunovodstvo_entry_naziv_prim_plat)

                racunovodstvo_entry_naz_izda_rac = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=300,border_color="black")
                racunovodstvo_entry_naz_izda_rac.grid(column=2,row=o+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_naz_izda_rac)
                racunovodstvo1_all_entries_list.append(racunovodstvo_entry_naz_izda_rac)

                racunovodstvo_entry_uvjeti_stand_pos = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=260,border_color="black")
                racunovodstvo_entry_uvjeti_stand_pos.grid(column=3,row=o+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_uvjeti_stand_pos)
                racunovodstvo1_all_entries_list.append(racunovodstvo_entry_uvjeti_stand_pos)

                racunovodstvo_entry_datum_otkupa = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=190,border_color="black")
                racunovodstvo_entry_datum_otkupa.grid(column=4,row=o+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_datum_otkupa)
                racunovodstvo1_all_entries_list.append(racunovodstvo_entry_datum_otkupa)

                racunovodstvo_entry_datum_dospijeca = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=220,border_color="black")
                racunovodstvo_entry_datum_dospijeca.grid(column=5,row=o+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_datum_dospijeca)
                racunovodstvo1_all_entries_list.append(racunovodstvo_entry_datum_dospijeca)

                racunovodstvo_entry_iznos_racuna = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=180,border_color="black")
                racunovodstvo_entry_iznos_racuna.grid(column=6,row=o+1 ,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_iznos_racuna)
                racunovodstvo1_all_entries_list.append(racunovodstvo_entry_iznos_racuna)

                racunovodstvo_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=180,border_color="black")
                racunovodstvo_entry_iznos_otkupa.grid(column=7,row=o+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_iznos_otkupa)
                racunovodstvo1_all_entries_list.append(racunovodstvo_entry_iznos_otkupa)
                
                
                racunovodstvo1_add_all_list.append(row)
                o += 1        
        if not os.path.exists("user_input_in_widgetsDB/racunovodstvo1_user_entry_data.json"):
            return  # Return if the file doesn't exist

        with open("user_input_in_widgetsDB/racunovodstvo1_user_entry_data.json", "r") as file:
            entry_data_list = json.load(file)

        racunovodstvo1_entry_counter = 1
        for entry_data in entry_data_list:
            entry_key = f"entry{racunovodstvo1_entry_counter}"
            if entry_key in entry_data:
                racunovodstvo1_all_entries_list[racunovodstvo1_entry_counter - 1].insert(0, entry_data[entry_key])
            racunovodstvo1_entry_counter += 1
  
#########################################################################################################
        
        with open("widgetsDB/racunovodstvo2_widgets_database", "r") as file:
            loaded_data = json.load(file) - 1
            
            for y in range(loaded_data):
                global m
                row = []

                cbox_var = tkinter.IntVar()
                kwargs = {}
                kwargs["checked"] = cbox_var
                kwargs["row"] = row
                checkbox = ctk.CTkCheckBox(scrollable_frame_racunovodstvo2,
                                        onvalue=1,
                                        variable=cbox_var,
                                        offvalue=0,
                                        text=None,
                                        fg_color="#37CB56",
                                        hover_color="#176828",
                                        command=lambda kwargs=kwargs: checkbox_check(kwargs),border_color="black")
                checkbox.grid(column=0, row=m+1, padx=0, sticky="w")
                row.append(checkbox)
                
                racunovodstvo_entry_diskont_bruto = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=190,border_color="black")
                racunovodstvo_entry_diskont_bruto.grid(column=1,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_diskont_bruto)
                racunovodstvo2_all_entries_list.append(racunovodstvo_entry_diskont_bruto)

                racunovodstvo_entry_diskont_netto = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=200,border_color="black")
                racunovodstvo_entry_diskont_netto.grid(column=2,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_diskont_netto)
                racunovodstvo2_all_entries_list.append(racunovodstvo_entry_diskont_netto)

                racunovodstvo_entry_diskont_godisnji_trosak = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=200,border_color="black")
                racunovodstvo_entry_diskont_godisnji_trosak.grid(column=3,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_diskont_godisnji_trosak)
                racunovodstvo2_all_entries_list.append(racunovodstvo_entry_diskont_godisnji_trosak)

                racunovodstvo_entry_ex_ante = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=430,border_color="black")
                racunovodstvo_entry_ex_ante.grid(column=4,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_ex_ante)
                racunovodstvo2_all_entries_list.append(racunovodstvo_entry_ex_ante)

                racunovodstvo_entry_razlika = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=120,border_color="black")
                racunovodstvo_entry_razlika.grid(column=5,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_razlika)
                racunovodstvo2_all_entries_list.append(racunovodstvo_entry_razlika)

                racunovodstvo_entry_prihod = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=120,border_color="black")
                racunovodstvo_entry_prihod.grid(column=6,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_prihod)
                racunovodstvo2_all_entries_list.append(racunovodstvo_entry_prihod)

                racunovodstvo_entry_pdv = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=100,border_color="black")
                racunovodstvo_entry_pdv.grid(column=7,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_pdv)
                racunovodstvo2_all_entries_list.append(racunovodstvo_entry_pdv)

                racunovodstvo_entry_cisti_prihod = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=400,border_color="black")
                racunovodstvo_entry_cisti_prihod.grid(column=8,row=m+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_cisti_prihod)
                racunovodstvo2_all_entries_list.append(racunovodstvo_entry_cisti_prihod)
                
                racunovodstvo2_add_all_list.append(row)
                
                m += 1
        
        
        if not os.path.exists("user_input_in_widgetsDB/racunovodstvo2_user_entry_data.json"):
            return  # Return if the file doesn't exist

        with open("user_input_in_widgetsDB/racunovodstvo2_user_entry_data.json", "r") as file:
            entry_data_list = json.load(file)

        racunovodstvo2_entry_counter = 1
        for entry_data in entry_data_list:
            entry_key = f"entry{racunovodstvo2_entry_counter}"
            if entry_key in entry_data:
                racunovodstvo2_all_entries_list[racunovodstvo2_entry_counter - 1].insert(0, entry_data[entry_key])
            racunovodstvo2_entry_counter += 1
        
#########################################################################################################        
           
        with open("widgetsDB/racunovodstvo3_widgets_database", "r") as file:
            loaded_data = json.load(file) - 1
            
            for y in range(loaded_data):
                global n
                row = []

                cbox_var = tkinter.IntVar()
                kwargs = {}
                kwargs["checked"] = cbox_var
                kwargs["row"] = row
                checkbox = ctk.CTkCheckBox(scrollable_frame_racunovodstvo3,
                                        onvalue=1,
                                        variable=cbox_var,
                                        offvalue=0,
                                        text=None,
                                        fg_color="#37CB56",
                                        hover_color="#176828",
                                        command=lambda kwargs=kwargs: checkbox_check(kwargs),border_color="black")
                checkbox.grid(column=0, row=n+1, padx=0, sticky="w")
                row.append(checkbox)
                
                racunovodstvo_entry_ex_post = ctk.CTkEntry(scrollable_frame_racunovodstvo3,width=430,border_color="black")
                racunovodstvo_entry_ex_post.grid(column=1,row=n+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_ex_post)
                racunovodstvo3_all_entries_list.append(racunovodstvo_entry_ex_post)

                racunovodstvo_entry_kasni_iza_valute = ctk.CTkEntry(scrollable_frame_racunovodstvo3,width=250,border_color="black")
                racunovodstvo_entry_kasni_iza_valute.grid(column=2,row=n+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_kasni_iza_valute)
                racunovodstvo3_all_entries_list.append(racunovodstvo_entry_kasni_iza_valute)

                racunovodstvo_entry_godisnji_ako_plati_valuti = ctk.CTkEntry(scrollable_frame_racunovodstvo3,width=550,border_color="black")
                racunovodstvo_entry_godisnji_ako_plati_valuti.grid(column=3,row=n+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_godisnji_ako_plati_valuti)
                racunovodstvo3_all_entries_list.append(racunovodstvo_entry_godisnji_ako_plati_valuti)

                racunovodstvo_entry_stvarni_godisnji_trosak = ctk.CTkEntry(scrollable_frame_racunovodstvo3,width=460,border_color="black")
                racunovodstvo_entry_stvarni_godisnji_trosak.grid(column=4,row=n+1,sticky="w",ipady=0,padx=0,pady=0)
                row.append(racunovodstvo_entry_stvarni_godisnji_trosak)
                racunovodstvo3_all_entries_list.append(racunovodstvo_entry_stvarni_godisnji_trosak)
                
                racunovodstvo3_add_all_list.append(row)
                
                n += 1
                
                
        if not os.path.exists("user_input_in_widgetsDB/racunovodstvo3_user_entry_data.json"):
            return  # Return if the file doesn't exist

        with open("user_input_in_widgetsDB/racunovodstvo3_user_entry_data.json", "r") as file:
            entry_data_list = json.load(file)

        racunovodstvo3_entry_counter = 1
        for entry_data in entry_data_list:
            entry_key = f"entry{racunovodstvo3_entry_counter}"
            if entry_key in entry_data:
                racunovodstvo3_all_entries_list[racunovodstvo3_entry_counter - 1].insert(0, entry_data[entry_key])
            racunovodstvo3_entry_counter += 1
    
    
    except FileNotFoundError:
        pass

#endregion



#region Save button...
save_button = ctk.CTkButton(tabView.tab("Datoteka"), text="Spremi",command=save_func)
save_button.pack(padx=100,pady=20) 
#endregion




#region Labele Main Office

main_label_datum = ctk.CTkLabel(fixed_frame_main_office,
                           text="Datum",
                           font=("Arial",24))
main_label_datum.grid(column=1,row=0,ipadx=30)

main_label_otkup = ctk.CTkLabel(fixed_frame_main_office,
                           text="Ugovor o otkupu",
                           font=("Arial",24))
main_label_otkup.grid(column=2,row=0,ipadx=220)

main_label_ustup = ctk.CTkLabel(fixed_frame_main_office,
                           text="Ugovor o ustupu",
                           font=("Arial",24))
main_label_ustup.grid(column=3,row=0,ipadx=140)

main_label_datumipotpis = ctk.CTkLabel(fixed_frame_main_office,
                           text="Potpis sa datumom",
                           font=("Arial",24))
main_label_datumipotpis.grid(column=4,row=0,ipadx=140)
#endregion

#region Entry Main Office

main_row = []

main_entry_datum = ctk.CTkEntry(scrollable_frame_Main,width=150,border_color="black")
main_entry_datum.grid(column=1,row=1,ipadx=0,pady=(5,0),sticky="w")
main_row.append(main_entry_datum)
main_all_entries_list.append(main_entry_datum)


main_entry_otkup = ctk.CTkEntry(scrollable_frame_Main,width=560,border_color="black")
main_entry_otkup.grid(column=2,row=1,ipadx=0,pady=(5,0))
main_row.append(main_entry_otkup)
main_all_entries_list.append(main_entry_otkup)


main_entry_ustup = ctk.CTkEntry(scrollable_frame_Main,width=500,border_color="black")
main_entry_ustup.grid(column=3,row=1,ipadx=0,pady=(5,0))
main_row.append(main_entry_ustup)
main_all_entries_list.append(main_entry_ustup)


main_entry_datumipotpis = ctk.CTkEntry(scrollable_frame_Main,width=500,border_color="black")
main_entry_datumipotpis.grid(column=4,row=1,ipadx=0,pady=(5,0))
main_row.append(main_entry_datumipotpis)
main_all_entries_list.append(main_entry_datumipotpis)

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
                               command=main_add_row)
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
back_label_datum.grid(column=1,row=0,ipadx=30)

back_label_br_ugovora = ctk.CTkLabel(fixed_frame_back_office,
                           text="Broj ugovora",
                           font=("Arial",24))
back_label_br_ugovora.grid(column=2,row=0,ipadx=90)

back_label_br_fakture = ctk.CTkLabel(fixed_frame_back_office,
                           text="Broj fakture",
                           font=("Arial",24))
back_label_br_fakture.grid(column=3,row=0,ipadx=90)

back_label_iznos = ctk.CTkLabel(fixed_frame_back_office,
                           text="Iznos",
                           font=("Arial",24))
back_label_iznos.grid(column=4,row=0,ipadx=130)

back_label_placeno_neplaceno = ctk.CTkLabel(fixed_frame_back_office,
                           text="Placeno/Neplaceno",
                           font=("Arial",24))
back_label_placeno_neplaceno.grid(column=5,row=0,ipadx=90)

#endregion

#region Entry Back Office
back_row = []

back_entry_datum = ctk.CTkEntry(scrollable_frame_Back,width=350,border_color="black")
back_entry_datum.grid(column=1,row=1,padx=0,pady=(5,0),sticky="w")
back_row.append(back_entry_datum)
back_all_entries_list.append(back_entry_datum)

back_entry_br_ugovora = ctk.CTkEntry(scrollable_frame_Back,width=300,border_color="black")
back_entry_br_ugovora.grid(column=2,row=1,padx=0,pady=(5,0))
back_row.append(back_entry_br_ugovora)
back_all_entries_list.append(back_entry_br_ugovora)

back_entry_br_fakture = ctk.CTkEntry(scrollable_frame_Back,width=300,border_color="black")
back_entry_br_fakture.grid(column=3,row=1,padx=0,pady=(5,0))
back_row.append(back_entry_br_fakture)
back_all_entries_list.append(back_entry_br_fakture)

back_entry_iznos = ctk.CTkEntry(scrollable_frame_Back,width=350,border_color="black")
back_entry_iznos.grid(column=4,row=1,padx=0,pady=(5,0))
back_row.append(back_entry_iznos)
back_all_entries_list.append(back_entry_iznos)

back_entry_placeno_neplaceno = ctk.CTkEntry(scrollable_frame_Back,width=410,border_color="black")
back_entry_placeno_neplaceno.grid(column=5,row=1,padx=0,pady=(5,0))
back_row.append(back_entry_placeno_neplaceno)
back_all_entries_list.append(back_entry_placeno_neplaceno)


#endregion

#region Checkbox Back Office
cbox_var = tkinter.IntVar()
kwargs = {}
kwargs["checked"] = cbox_var
kwargs["row"] = back_row
back_checkbox = ctk.CTkCheckBox(master=scrollable_frame_Back,text=None,hover_color="#176828",fg_color="#37CB56",
                                onvalue=1, offvalue=0,
                                variable=cbox_var, command=lambda kwargs=kwargs: checkbox_check(kwargs))
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
middle_label_primatelj.grid(column=1,row=0,padx=(20,30))

middle_label_posiljatelj = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Posiljatelj",
                           font=("Arial",24))
middle_label_posiljatelj.grid(column=2,row=0,ipadx=50)

middle_label_broj_ugovora = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Broj ugovora",
                           font=("Arial",24))
middle_label_broj_ugovora.grid(column=3,row=0,ipadx=50)

middle_label_iznos_potrazivanja = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Iznos potrazivanja",
                           font=("Arial",24))
middle_label_iznos_potrazivanja.grid(column=4,row=0,ipadx=50)

middle_label_iznos_otkupa = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Iznos otkupa",
                           font=("Arial",24))
middle_label_iznos_otkupa.grid(column=5,row=0,ipadx=50)

middle_label_broj_fakture = ctk.CTkLabel(fixed_frame_middle_office,
                           text="Broj fakture",
                           font=("Arial",24))
middle_label_broj_fakture.grid(column=6,row=0,ipadx=50)

middle_label_datum_stavljanja_na_placanje = ctk.CTkLabel(fixed_frame_middle_office,
                                            text="Datum stavljanja na placanje",
                                            font=("Arial",24))
middle_label_datum_stavljanja_na_placanje.grid(column=7,row=0,ipadx=50)
#endregion

#region Entry Middle Office

middle_row = []

middle_entry_primatelj = ctk.CTkEntry(scrollable_frame_Middle,width=140,border_color="black")
middle_entry_primatelj.grid(column=1,row=1,sticky="w",ipady=0,padx=0,pady=0)
middle_row.append(middle_entry_primatelj)
middle_all_entries_list.append(middle_entry_primatelj)

middle_entry_posiljatelj = ctk.CTkEntry(scrollable_frame_Middle,width=210,border_color="black")
middle_entry_posiljatelj.grid(column=2,row=1,ipadx=0,ipady=0,padx=0,pady=0)
middle_row.append(middle_entry_posiljatelj)
middle_all_entries_list.append(middle_entry_posiljatelj)

middle_entry_broj_ugovora = ctk.CTkEntry(scrollable_frame_Middle,width=220,border_color="black")
middle_entry_broj_ugovora.grid(column=3,row=1,ipadx=0,ipady=0,padx=0,pady=0)
middle_row.append(middle_entry_broj_ugovora)
middle_all_entries_list.append(middle_entry_broj_ugovora)

middle_entry_iznos_potrazivanja = ctk.CTkEntry(scrollable_frame_Middle,width=300,border_color="black")
middle_entry_iznos_potrazivanja.grid(column=4,row=1,ipadx=0,ipady=0,padx=0,pady=0)
middle_row.append(middle_entry_iznos_potrazivanja)
middle_all_entries_list.append(middle_entry_iznos_potrazivanja)

middle_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_Middle,width=270,border_color="black")
middle_entry_iznos_otkupa.grid(column=5,row=1,ipadx=0,ipady=0,padx=0,pady=0)
middle_row.append(middle_entry_iznos_otkupa)
middle_all_entries_list.append(middle_entry_iznos_otkupa)

middle_entry_broj_fakture = ctk.CTkEntry(scrollable_frame_Middle,width=200,border_color="black")
middle_entry_broj_fakture.grid(column=6,row=1,ipadx=0,ipady=0,padx=0,pady=0)
middle_row.append(middle_entry_broj_fakture)
middle_all_entries_list.append(middle_entry_broj_fakture)

middle_entry_datum_stavljanja_na_placanje = ctk.CTkEntry(scrollable_frame_Middle,width=400,border_color="black")
middle_entry_datum_stavljanja_na_placanje.grid(column=7,row=1,ipadx=0,ipady=0,padx=0,pady=0)
middle_row.append(middle_entry_datum_stavljanja_na_placanje)
middle_all_entries_list.append(middle_entry_datum_stavljanja_na_placanje)


#endregion

#region Checkbox Middle Office
cbox_var = tkinter.IntVar()
kwargs = {}
kwargs["checked"] = cbox_var
kwargs["row"] = middle_row

middle_checkbox = ctk.CTkCheckBox(scrollable_frame_Middle,text=None,fg_color="#37CB56",hover_color="#176828",
                                onvalue=1, offvalue=0,
                                variable=cbox_var, command=lambda kwargs=kwargs: checkbox_check(kwargs))
middle_checkbox.grid(column=0,row=1,ipadx=0,ipady=0,sticky="w")
#endregion

#region gumb za dodavanje/oduzimanje reda Middle Office
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



#region Label Racunovodstvo1

rac_label_naziv_prim_plat = ctk.CTkLabel(fixed_frame_racunovodstvo1,
                                         text="Naziv primatelja/platitelja racuna",
                                        font=("Arial",24))
rac_label_naziv_prim_plat.grid(column=1,row=0,padx=(0,40))

rac_label_naz_izda_rac = ctk.CTkLabel(fixed_frame_racunovodstvo1,
                                         text="Naziv izdavatelja racuna",
                                        font=("Arial",24))
rac_label_naz_izda_rac.grid(column=2,row=0,padx=(0,40))

rac_label_uvjeti_stand_pos = ctk.CTkLabel(fixed_frame_racunovodstvo1,
                                         text="Uvjeti S-stand/P-pos",
                                        font=("Arial",24))
rac_label_uvjeti_stand_pos.grid(column=3,row=0,padx=(0,40))

rac_label_datum_otkupa = ctk.CTkLabel(fixed_frame_racunovodstvo1,
                                         text="Datum otkupa",
                                        font=("Arial",24))
rac_label_datum_otkupa.grid(column=4,row=0,padx=(0,40))


rac_label_datum_dospijeca = ctk.CTkLabel(fixed_frame_racunovodstvo1,
                                         text="Datum dospijeca",
                                        font=("Arial",24))
rac_label_datum_dospijeca.grid(column=5,row=0,padx=(0,40))


rac_label_iznos_racuna = ctk.CTkLabel(fixed_frame_racunovodstvo1,
                                         text="Iznos racuna",
                                        font=("Arial",24))
rac_label_iznos_racuna.grid(column=6,row=0,padx=(0,40))

rac_label_iznos_otkupa = ctk.CTkLabel(fixed_frame_racunovodstvo1,
                                         text="Iznos otkupa",
                                        font=("Arial",24))
rac_label_iznos_otkupa.grid(column=7,row=0,padx=(0,40))

#endregion

#region Entry Racunovodstvo1
racunovodstvo_row = []

racunovodstvo_entry_naziv_prim_plat = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=370,border_color="black")
racunovodstvo_entry_naziv_prim_plat.grid(column=1,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo_row.append(racunovodstvo_entry_naziv_prim_plat)
racunovodstvo1_all_entries_list.append(racunovodstvo_entry_naziv_prim_plat)

racunovodstvo_entry_naz_izda_rac = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=300,border_color="black")
racunovodstvo_entry_naz_izda_rac.grid(column=2,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo_row.append(racunovodstvo_entry_naz_izda_rac)
racunovodstvo1_all_entries_list.append(racunovodstvo_entry_naz_izda_rac)

racunovodstvo_entry_uvjeti_stand_pos = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=260,border_color="black")
racunovodstvo_entry_uvjeti_stand_pos.grid(column=3,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo_row.append(racunovodstvo_entry_uvjeti_stand_pos)
racunovodstvo1_all_entries_list.append(racunovodstvo_entry_uvjeti_stand_pos)

racunovodstvo_entry_datum_otkupa = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=190,border_color="black")
racunovodstvo_entry_datum_otkupa.grid(column=4,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo_row.append(racunovodstvo_entry_datum_otkupa)
racunovodstvo1_all_entries_list.append(racunovodstvo_entry_datum_otkupa)

racunovodstvo_entry_datum_dospijeca = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=220,border_color="black")
racunovodstvo_entry_datum_dospijeca.grid(column=5,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo_row.append(racunovodstvo_entry_datum_dospijeca)
racunovodstvo1_all_entries_list.append(racunovodstvo_entry_datum_dospijeca)

racunovodstvo_entry_iznos_racuna = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=180,border_color="black")
racunovodstvo_entry_iznos_racuna.grid(column=6,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo_row.append(racunovodstvo_entry_iznos_racuna)
racunovodstvo1_all_entries_list.append(racunovodstvo_entry_iznos_racuna)

racunovodstvo_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=180,border_color="black")
racunovodstvo_entry_iznos_otkupa.grid(column=7,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo_row.append(racunovodstvo_entry_iznos_otkupa)
racunovodstvo1_all_entries_list.append(racunovodstvo_entry_iznos_otkupa)

#endregion

#region Checkbox Racunovodstvo1
cbox_var = tkinter.IntVar()
kwargs = {}
kwargs["checked"] = cbox_var
kwargs["row"] = racunovodstvo_row

racunovodstvo_checkbox = ctk.CTkCheckBox(scrollable_frame_racunovodstvo1,text=None,fg_color="#37CB56",hover_color="#176828",
                                onvalue=1, offvalue=0,
                                variable=cbox_var, command=lambda kwargs=kwargs: checkbox_check(kwargs))
racunovodstvo_checkbox.grid(column=0,row=1,ipadx=0,ipady=0,sticky="w")
#endregion

#region gumb za dodavanje/oduzimanje Racunovodstvo1
racunovodstvo1_button_add_row = ctk.CTkButton(fixed_frame_racunovodstvo1,text="+",
                               width=10,
                               corner_radius=120,
                               anchor="w",
                               command=racunovodstvo1_add_row)
racunovodstvo1_button_add_row.grid(column=0,row=0,sticky="w",ipadx=0,ipady=0)

racunovodstvo1_button_delete_row = ctk.CTkButton(fixed_frame_racunovodstvo1,text="-",
                               width=10,
                               corner_radius=20,
                               command=racunovodstvo1_delete_row)
racunovodstvo1_button_delete_row.grid(column=0,row=0,padx=40,ipadx=0,ipady=0)
#endregion



#region Label Racunovodstvo2
rac_label_diskont_bruto = ctk.CTkLabel(fixed_frame_racunovodstvo2,
                                         text="%" + "diskont bruto",
                                        font=("Arial",24))
rac_label_diskont_bruto.grid(column=1,row=0,padx=(0,40))

rac_label_diskont_netto = ctk.CTkLabel(fixed_frame_racunovodstvo2,
                                         text="%" + "diskont netto",
                                        font=("Arial",24))
rac_label_diskont_netto.grid(column=2,row=0,padx=(0,40))

rac_label_diskont_god_trosak = ctk.CTkLabel(fixed_frame_racunovodstvo2,
                                         text="Godisnji trosak",
                                        font=("Arial",24))
rac_label_diskont_god_trosak.grid(column=3,row=0,padx=(0,40))

rac_label_ex_ante = ctk.CTkLabel(fixed_frame_racunovodstvo2,
                                         text="Ex Ante godisnji prinos za investitora",
                                        font=("Arial",24))
rac_label_ex_ante.grid(column=4,row=0,padx=(0,40))

rac_label_razlika = ctk.CTkLabel(fixed_frame_racunovodstvo2,
                                         text="Razlika",
                                        font=("Arial",24))
rac_label_razlika.grid(column=5,row=0,padx=(0,40))

rac_label_prihod = ctk.CTkLabel(fixed_frame_racunovodstvo2,
                                         text="Prihod",
                                        font=("Arial",24))
rac_label_prihod.grid(column=6,row=0,padx=(0,40))

rac_label_pdv = ctk.CTkLabel(fixed_frame_racunovodstvo2,
                                         text="PDV",
                                        font=("Arial",24))
rac_label_pdv.grid(column=7,row=0,padx=(20,40))

rac_label_cisti_prihod = ctk.CTkLabel(fixed_frame_racunovodstvo2,
                                         text="Cisti prihod",
                                        font=("Arial",24))
rac_label_cisti_prihod.grid(column=8,row=0,padx=(130,0))


#endregion

#region Entry Racunovodstvo2

racunovodstvo2_row = []

racunovodstvo_entry_diskont_bruto = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=190,border_color="black")
racunovodstvo_entry_diskont_bruto.grid(column=1,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo2_row.append(racunovodstvo_entry_diskont_bruto)
racunovodstvo2_all_entries_list.append(racunovodstvo_entry_diskont_bruto)

racunovodstvo_entry_diskont_netto = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=200,border_color="black")
racunovodstvo_entry_diskont_netto.grid(column=2,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo2_row.append(racunovodstvo_entry_diskont_netto)
racunovodstvo2_all_entries_list.append(racunovodstvo_entry_diskont_netto)

racunovodstvo_entry_diskont_godisnji_trosak = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=200,border_color="black")
racunovodstvo_entry_diskont_godisnji_trosak.grid(column=3,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo2_row.append(racunovodstvo_entry_diskont_godisnji_trosak)
racunovodstvo2_all_entries_list.append(racunovodstvo_entry_diskont_godisnji_trosak)

racunovodstvo_entry_ex_ante = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=430,border_color="black")
racunovodstvo_entry_ex_ante.grid(column=4,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo2_row.append(racunovodstvo_entry_ex_ante)
racunovodstvo2_all_entries_list.append(racunovodstvo_entry_ex_ante)

racunovodstvo_entry_razlika = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=120,border_color="black")
racunovodstvo_entry_razlika.grid(column=5,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo2_row.append(racunovodstvo_entry_razlika)
racunovodstvo2_all_entries_list.append(racunovodstvo_entry_razlika)

racunovodstvo_entry_prihod = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=120,border_color="black")
racunovodstvo_entry_prihod.grid(column=6,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo2_row.append(racunovodstvo_entry_prihod)
racunovodstvo2_all_entries_list.append(racunovodstvo_entry_prihod)

racunovodstvo_entry_pdv = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=100,border_color="black")
racunovodstvo_entry_pdv.grid(column=7,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo2_row.append(racunovodstvo_entry_pdv)
racunovodstvo2_all_entries_list.append(racunovodstvo_entry_pdv)

racunovodstvo_entry_cisti_prihod = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=400,border_color="black")
racunovodstvo_entry_cisti_prihod.grid(column=8,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo2_row.append(racunovodstvo_entry_cisti_prihod)
racunovodstvo2_all_entries_list.append(racunovodstvo_entry_cisti_prihod)




#endregion

#region Checkbox Racunovodstvo2
cbox_var = tkinter.IntVar()
kwargs = {}
kwargs["checked"] = cbox_var
kwargs["row"] = racunovodstvo2_row

racunovodstvo_checkbox = ctk.CTkCheckBox(scrollable_frame_racunovodstvo2,text=None,fg_color="#37CB56",hover_color="#176828",
                                onvalue=1, offvalue=0,
                                variable=cbox_var, command=lambda kwargs=kwargs: checkbox_check(kwargs))
racunovodstvo_checkbox.grid(column=0,row=1,ipadx=0,ipady=0,sticky="w")
#endregion

#region gumb za dodavanje/oduzimanje Racunovodstvo2
racunovodstvo2_button_add_row = ctk.CTkButton(fixed_frame_racunovodstvo2,text="+",
                               width=10,
                               corner_radius=120,
                               anchor="w",
                               command=racunovodstvo2_add_row)
racunovodstvo2_button_add_row.grid(column=0,row=0,sticky="w",ipadx=0,ipady=0)

racunovodstvo2_button_delete_row = ctk.CTkButton(fixed_frame_racunovodstvo2,text="-",
                               width=10,
                               corner_radius=20,
                               command=racunovodstvo2_delete_row)
racunovodstvo2_button_delete_row.grid(column=0,row=0,padx=40,ipadx=0,ipady=0)
#endregion





#region Label Racunovodstvo3
rac_label_ex_post = ctk.CTkLabel(fixed_frame_racunovodstvo3,
                                        text="Ex post godisnji prinos za investitora",
                                        font=("Arial",24))
rac_label_ex_post.grid(column=1,row=0,padx=(0,80))

rac_label_kasni_iza_valute = ctk.CTkLabel(fixed_frame_racunovodstvo3,
                                        text="Kasni iza valute",
                                        font=("Arial",24))
rac_label_kasni_iza_valute.grid(column=2,row=0,padx=(0,80))

rac_label_godisnji_ako_plati_valuti = ctk.CTkLabel(fixed_frame_racunovodstvo3,
                                        text="Godisnji trosak financiranja ako plati u valuti",
                                        font=("Arial",24))
rac_label_godisnji_ako_plati_valuti.grid(column=3,row=0,padx=(0,80))

rac_label_stvarni_godisnji_trosak = ctk.CTkLabel(fixed_frame_racunovodstvo3,
                                        text="Stvarni godisnji trosak financiranja",
                                        font=("Arial",24))
rac_label_stvarni_godisnji_trosak.grid(column=4,row=0,padx=(0,40))





#endregion

#region Entry Racunovodstvo3
racunovodstvo3_row = []

racunovodstvo_entry_ex_post = ctk.CTkEntry(scrollable_frame_racunovodstvo3,width=430,border_color="black")
racunovodstvo_entry_ex_post.grid(column=1,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo3_row.append(racunovodstvo_entry_ex_post)
racunovodstvo3_all_entries_list.append(racunovodstvo_entry_ex_post)

racunovodstvo_entry_kasni_iza_valute = ctk.CTkEntry(scrollable_frame_racunovodstvo3,width=250,border_color="black")
racunovodstvo_entry_kasni_iza_valute.grid(column=2,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo3_row.append(racunovodstvo_entry_kasni_iza_valute)
racunovodstvo3_all_entries_list.append(racunovodstvo_entry_kasni_iza_valute)

racunovodstvo_entry_godisnji_ako_plati_valuti = ctk.CTkEntry(scrollable_frame_racunovodstvo3,width=550,border_color="black")
racunovodstvo_entry_godisnji_ako_plati_valuti.grid(column=3,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo3_row.append(racunovodstvo_entry_godisnji_ako_plati_valuti)
racunovodstvo3_all_entries_list.append(racunovodstvo_entry_godisnji_ako_plati_valuti)

racunovodstvo_entry_stvarni_godisnji_trosak = ctk.CTkEntry(scrollable_frame_racunovodstvo3,width=460,border_color="black")
racunovodstvo_entry_stvarni_godisnji_trosak.grid(column=4,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo3_row.append(racunovodstvo_entry_stvarni_godisnji_trosak)
racunovodstvo3_all_entries_list.append(racunovodstvo_entry_stvarni_godisnji_trosak)


#endregion

#region Checkbox Racunovodstvo3
cbox_var = tkinter.IntVar()
kwargs = {}
kwargs["checked"] = cbox_var
kwargs["row"] = racunovodstvo3_row

racunovodstvo_checkbox = ctk.CTkCheckBox(scrollable_frame_racunovodstvo3,text=None,fg_color="#37CB56",hover_color="#176828",
                                onvalue=1, offvalue=0,
                                variable=cbox_var, command=lambda kwargs=kwargs: checkbox_check(kwargs))
racunovodstvo_checkbox.grid(column=0,row=1,ipadx=0,ipady=0,sticky="w")
#endregion

#region gumb za dodavanje/oduzimanje Racunovodstvo3
racunovodstvo3_button_add_row = ctk.CTkButton(fixed_frame_racunovodstvo3,text="+",
                               width=10,
                               corner_radius=120,
                               anchor="w",
                               command=racunovodstvo3_add_row)
racunovodstvo3_button_add_row.grid(column=0,row=0,sticky="w",ipadx=0,ipady=0)

racunovodstvo3_button_delete_row = ctk.CTkButton(fixed_frame_racunovodstvo3,text="-",
                               width=10,
                               corner_radius=20,
                               command=racunovodstvo3_delete_row)
racunovodstvo3_button_delete_row.grid(column=0,row=0,padx=40,ipadx=0,ipady=0)
#endregion




"""
#region binding

main_entry_datum.bind("<1>", pick_date)

#endregion
"""

#region Promjena scaling aplikacije
def change_scaling_event(new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
        



scaling_label = ctk.CTkLabel(tabView.tab("Datoteka"), text="UI Scaling:", anchor="w")
scaling_label.pack()
scaling_optionemenu = ctk.CTkOptionMenu(tabView.tab("Datoteka"), values=["50%","55%","60%","70%","80%", "90%", "100%", "110%", "120%"],
                                                               command=change_scaling_event)
scaling_optionemenu.pack()
#endregion



#trebam rucno dodati entry odmah nakon kreiranja entrya i bok




load_func()

app.mainloop()