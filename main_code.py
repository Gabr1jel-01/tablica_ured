import tkinter as tk
from time import *
import customtkinter as ctk
import time 
import tkinter.messagebox
import configparser
from tkinter import END, filedialog
from tkcalendar import *



ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
#app.after(0, lambda:app.state('zoomed'))
#app.resizable(height=False,width=False)
app.title("Office")
app.geometry("1280x1080+400+50")



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
tabView.add("Datoteka")

#ovdje sam stavio da tab glavni izbornik bude prvi otvoren kada se pokrene aplikacija
tabView.set("Racunovodstvo2")
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
#Fiksni frame Racunovodstvo1
fixed_frame_racunovodstvo1 = ctk.CTkFrame(tabView.tab("Racunovodstvo1"),height=35)
fixed_frame_racunovodstvo1.pack(pady=5,padx=5,fill="both")
#Fiksni frame Racunovodstvo2
fixed_frame_racunovodstvo2 = ctk.CTkFrame(tabView.tab("Racunovodstvo2"),height=35)
fixed_frame_racunovodstvo2.pack(pady=5,padx=5,fill="both")


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
#endregion

#region Liste
main_add_all_list = []
middle_add_all_list = []
back_add_all_list = []
racunovodstvo1_add_all_list = []
racunovodstvo2_add_all_list = []

#endregion

#region Konstante
i = 1
j = 1
k = 1
l = 1
m = 1
#endregion


#region FUNKCIJE 
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
    checkbox.grid(column=0, row=i+1, padx=0, sticky="w")
    row.append(checkbox)

    entry_datum = ctk.CTkEntry(scrollable_frame_Main, width=150,border_color="black")
    entry_datum.grid(column=1, row=i+1, padx=0, pady=0, sticky="w")
    row.append(entry_datum)

    main_entry_otkup = ctk.CTkEntry(scrollable_frame_Main, width=560,border_color="black")
    main_entry_otkup.grid(column=2, row=i+1, padx=0, pady=0)
    row.append(main_entry_otkup)

    main_entry_ustup = ctk.CTkEntry(scrollable_frame_Main, width=500,border_color="black")
    main_entry_ustup.grid(column=3, row=i+1, padx=0)
    row.append(main_entry_ustup)

    main_entry_datumipotpis = ctk.CTkEntry(scrollable_frame_Main, width=500,border_color="black")
    main_entry_datumipotpis.grid(column=4, row=i+1, padx=0, pady=0)
    row.append(main_entry_datumipotpis)

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

    back_entry_br_ugovora = ctk.CTkEntry(scrollable_frame_Back,width=300,border_color="black")
    back_entry_br_ugovora.grid(column=2,row=j+1,padx=0,pady=0)
    row.append(back_entry_br_ugovora)

    back_entry_br_fakture = ctk.CTkEntry(scrollable_frame_Back,width=300,border_color="black")
    back_entry_br_fakture.grid(column=3,row=j+1,padx=0)
    row.append(back_entry_br_fakture)
    
    back_entry_iznos = ctk.CTkEntry(scrollable_frame_Back,width=350,border_color="black")
    back_entry_iznos.grid(column=4,row=j+1,padx=0,pady=0)
    row.append(back_entry_iznos)
    
    back_entry_placeno_neplaceno = ctk.CTkEntry(scrollable_frame_Back,width=410,border_color="black")
    back_entry_placeno_neplaceno.grid(column=5,row=j+1,padx=0,pady=0)
    row.append(back_entry_placeno_neplaceno)
    
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

    middle_entry_posiljatelj = ctk.CTkEntry(scrollable_frame_Middle,width=210,border_color="black")
    middle_entry_posiljatelj.grid(column=2,row=k+1,ipadx=0,pady=0)
    row.append(middle_entry_posiljatelj)

    middle_entry_broj_ugovora = ctk.CTkEntry(scrollable_frame_Middle,width=220,border_color="black")
    middle_entry_broj_ugovora.grid(column=3,row=k+1,ipadx=0,pady=0)
    row.append(middle_entry_broj_ugovora)

    middle_entry_iznos_potrazivanja = ctk.CTkEntry(scrollable_frame_Middle,width=300,border_color="black")
    middle_entry_iznos_potrazivanja.grid(column=4,row=k+1,ipadx=0,pady=0)
    row.append(middle_entry_iznos_potrazivanja)

    middle_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_Middle,width=270,border_color="black")
    middle_entry_iznos_otkupa.grid(column=5,row=k+1,ipadx=0,pady=0)
    row.append(middle_entry_iznos_otkupa)

    middle_entry_broj_fakture = ctk.CTkEntry(scrollable_frame_Middle,width=200,border_color="black")
    middle_entry_broj_fakture.grid(column=6,row=k+1,ipadx=0,pady=0)
    row.append(middle_entry_broj_fakture)

    middle_entry_datum_stavljanja_na_placanje = ctk.CTkEntry(scrollable_frame_Middle,width=400,border_color="black")
    middle_entry_datum_stavljanja_na_placanje.grid(column=7,row=k+1,ipadx=0,pady=0)
    row.append(middle_entry_datum_stavljanja_na_placanje)

    middle_row_widgets = [middle_checkbox,middle_entry_primatelj,middle_entry_posiljatelj,
                        middle_entry_broj_ugovora,middle_entry_iznos_potrazivanja,
                        middle_entry_iznos_otkupa,middle_entry_broj_fakture,
                        middle_entry_datum_stavljanja_na_placanje]
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

def checkbox_check(kwargs):
    if kwargs["checked"].get():
        for item in kwargs["row"]:
            item.configure(fg_color="#37CB56")
    else:
        for item in kwargs["row"]:
            item.configure(fg_color="white")

def racunovodstvo1_add_row():
    
    global l
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
    checkbox.grid(column=0, row=l+1, padx=0, sticky="w")
    row.append(checkbox)
    
    racunovodstvo_entry_naziv_prim_plat = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=370,border_color="black")
    racunovodstvo_entry_naziv_prim_plat.grid(column=1,row=l+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_naziv_prim_plat)

    racunovodstvo_entry_naz_izda_rac = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=300,border_color="black")
    racunovodstvo_entry_naz_izda_rac.grid(column=2,row=l+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_naz_izda_rac)

    racunovodstvo_entry_uvjeti_stand_pos = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=260,border_color="black")
    racunovodstvo_entry_uvjeti_stand_pos.grid(column=3,row=l+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_uvjeti_stand_pos)

    racunovodstvo_entry_datum_otkupa = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=190,border_color="black")
    racunovodstvo_entry_datum_otkupa.grid(column=4,row=l+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_datum_otkupa)

    racunovodstvo_entry_datum_dospijeca = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=220,border_color="black")
    racunovodstvo_entry_datum_dospijeca.grid(column=5,row=l+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_datum_dospijeca)

    racunovodstvo_entry_iznos_racuna = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=180,border_color="black")
    racunovodstvo_entry_iznos_racuna.grid(column=6,row=l+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_iznos_racuna)

    racunovodstvo_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=180,border_color="black")
    racunovodstvo_entry_iznos_otkupa.grid(column=7,row=l+1,sticky="w",ipady=0,padx=0,pady=0)
    row.append(racunovodstvo_entry_iznos_otkupa)
    
    
    racunovodstvo1_add_all_list.append(row)
    l += 1
    
def racunovodstvo1_delete_row():
    
    global l
    
    if racunovodstvo1_add_all_list:
        last_row_widgets = racunovodstvo1_add_all_list.pop()  # Remove the last row's widgets from the list
        for widget in last_row_widgets:
            widget.destroy()  # Destroy each widget in the row
        l -= 1
    else:
        tkinter.messagebox.showinfo("Error","Nije moguće izbrisati početni red")
    
    
    pass

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

main_entry_otkup = ctk.CTkEntry(scrollable_frame_Main,width=560,border_color="black")
main_entry_otkup.grid(column=2,row=1,ipadx=0,pady=(5,0))
main_row.append(main_entry_otkup)

main_entry_ustup = ctk.CTkEntry(scrollable_frame_Main,width=500,border_color="black")
main_entry_ustup.grid(column=3,row=1,ipadx=0,pady=(5,0))
main_row.append(main_entry_ustup)

main_entry_datumipotpis = ctk.CTkEntry(scrollable_frame_Main,width=500,border_color="black")
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

back_entry_br_ugovora = ctk.CTkEntry(scrollable_frame_Back,width=300,border_color="black")
back_entry_br_ugovora.grid(column=2,row=1,padx=0,pady=(5,0))
back_row.append(back_entry_br_ugovora)

back_entry_br_fakture = ctk.CTkEntry(scrollable_frame_Back,width=300,border_color="black")
back_entry_br_fakture.grid(column=3,row=1,padx=0,pady=(5,0))
back_row.append(back_entry_br_fakture)

back_entry_iznos = ctk.CTkEntry(scrollable_frame_Back,width=350,border_color="black")
back_entry_iznos.grid(column=4,row=1,padx=0,pady=(5,0))
back_row.append(back_entry_iznos)

back_entry_placeno_neplaceno = ctk.CTkEntry(scrollable_frame_Back,width=410,border_color="black")
back_entry_placeno_neplaceno.grid(column=5,row=1,padx=0,pady=(5,0))
back_row.append(back_entry_placeno_neplaceno)


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

middle_entry_posiljatelj = ctk.CTkEntry(scrollable_frame_Middle,width=210,border_color="black")
middle_entry_posiljatelj.grid(column=2,row=1,ipadx=0,ipady=0,padx=0,pady=0)
middle_row.append(middle_entry_posiljatelj)

middle_entry_broj_ugovora = ctk.CTkEntry(scrollable_frame_Middle,width=220,border_color="black")
middle_entry_broj_ugovora.grid(column=3,row=1,ipadx=0,ipady=0,padx=0,pady=0)
middle_row.append(middle_entry_broj_ugovora)

middle_entry_iznos_potrazivanja = ctk.CTkEntry(scrollable_frame_Middle,width=300,border_color="black")
middle_entry_iznos_potrazivanja.grid(column=4,row=1,ipadx=0,ipady=0,padx=0,pady=0)
middle_row.append(middle_entry_iznos_potrazivanja)

middle_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_Middle,width=270,border_color="black")
middle_entry_iznos_otkupa.grid(column=5,row=1,ipadx=0,ipady=0,padx=0,pady=0)
middle_row.append(middle_entry_iznos_otkupa)

middle_entry_broj_fakture = ctk.CTkEntry(scrollable_frame_Middle,width=200,border_color="black")
middle_entry_broj_fakture.grid(column=6,row=1,ipadx=0,ipady=0,padx=0,pady=0)
middle_row.append(middle_entry_broj_fakture)

middle_entry_datum_stavljanja_na_placanje = ctk.CTkEntry(scrollable_frame_Middle,width=400,border_color="black")
middle_entry_datum_stavljanja_na_placanje.grid(column=7,row=1,ipadx=0,ipady=0,padx=0,pady=0)
middle_row.append(middle_entry_datum_stavljanja_na_placanje)


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

racunovodstvo_entry_naz_izda_rac = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=300,border_color="black")
racunovodstvo_entry_naz_izda_rac.grid(column=2,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo_row.append(racunovodstvo_entry_naz_izda_rac)

racunovodstvo_entry_uvjeti_stand_pos = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=260,border_color="black")
racunovodstvo_entry_uvjeti_stand_pos.grid(column=3,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo_row.append(racunovodstvo_entry_uvjeti_stand_pos)

racunovodstvo_entry_datum_otkupa = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=190,border_color="black")
racunovodstvo_entry_datum_otkupa.grid(column=4,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo_row.append(racunovodstvo_entry_datum_otkupa)

racunovodstvo_entry_datum_dospijeca = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=220,border_color="black")
racunovodstvo_entry_datum_dospijeca.grid(column=5,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo_row.append(racunovodstvo_entry_datum_dospijeca)

racunovodstvo_entry_iznos_racuna = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=180,border_color="black")
racunovodstvo_entry_iznos_racuna.grid(column=6,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo_row.append(racunovodstvo_entry_iznos_racuna)

racunovodstvo_entry_iznos_otkupa = ctk.CTkEntry(scrollable_frame_racunovodstvo1,width=180,border_color="black")
racunovodstvo_entry_iznos_otkupa.grid(column=7,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo_row.append(racunovodstvo_entry_iznos_otkupa)

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



#region Label Racunoovodstvo2
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
rac_label_pdv.grid(column=7,row=0,padx=(0,40))

rac_label_pdv = ctk.CTkLabel(fixed_frame_racunovodstvo2,
                                         text="Cisti prihod",
                                        font=("Arial",24))
rac_label_pdv.grid(column=8,row=0,padx=(100,0))


#endregion

#region Entry Racunovodstvo2

racunovodstvo2_row = []

racunovodstvo_entry_diskont_bruto = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=190,border_color="black")
racunovodstvo_entry_diskont_bruto.grid(column=1,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo2_row.append(racunovodstvo_entry_diskont_bruto)

racunovodstvo_entry_diskont_netto = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=200,border_color="black")
racunovodstvo_entry_diskont_netto.grid(column=2,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo2_row.append(racunovodstvo_entry_diskont_netto)

racunovodstvo_entry_diskont_godisnji_trosak = ctk.CTkEntry(scrollable_frame_racunovodstvo2,width=200,border_color="black")
racunovodstvo_entry_diskont_godisnji_trosak.grid(column=3,row=1,sticky="w",ipady=0,padx=0,pady=0)
racunovodstvo2_row.append(racunovodstvo_entry_diskont_godisnji_trosak)


#endregion

#region Checkbox Racunovodstvo2
cbox_var = tkinter.IntVar()
kwargs = {}
kwargs["checked"] = cbox_var
kwargs["row"] = racunovodstvo_row

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
                               command=racunovodstvo1_add_row)
racunovodstvo2_button_add_row.grid(column=0,row=0,sticky="w",ipadx=0,ipady=0)

racunovodstvo2_button_delete_row = ctk.CTkButton(fixed_frame_racunovodstvo2,text="-",
                               width=10,
                               corner_radius=20,
                               command=racunovodstvo1_delete_row)
racunovodstvo2_button_delete_row.grid(column=0,row=0,padx=40,ipadx=0,ipady=0)
#endregion






#region binding

main_entry_datum.bind("<1>", pick_date)

#endregion

app.mainloop()