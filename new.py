def main_add_row():
    global i
    main_row_data = {}

    main_checkbox = ctk.CTkCheckBox(scrollable_frame_Main, text=None, fg_color="#37CB56", hover_color="#176828")
    main_checkbox.grid(column=0, row=i+1, padx=0, sticky="w")
    main_row_data['checkbox'] = main_checkbox

    main_entry_datum = ctk.CTkEntry(scrollable_frame_Main, width=100)
    main_entry_datum.grid(column=1, row=i+1, padx=0, pady=0, sticky="w")
    main_row_data['datum'] = main_entry_datum

    main_entry_otkup = ctk.CTkEntry(scrollable_frame_Main, width=340)
    main_entry_otkup.grid(column=2, row=i+1, padx=0, pady=0)
    main_row_data['otkup'] = main_entry_otkup

    main_entry_ustup = ctk.CTkEntry(scrollable_frame_Main, width=260)
    main_entry_ustup.grid(column=3, row=i+1, padx=0)
    main_row_data['ustup'] = main_entry_ustup

    main_entry_datumipotpis = ctk.CTkEntry(scrollable_frame_Main, width=310)
    main_entry_datumipotpis.grid(column=4, row=i+1, padx=0, pady=0)
    main_row_data['datumipotpis'] = main_entry_datumipotpis

    main_add_all_list.append(main_row_data)
    print(main_add_all_list)

    i += 1
