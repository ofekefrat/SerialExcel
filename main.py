# from serial_module import *
import customtkinter as ctk
from customtkinter import *

def submit_serial(input, frameBuffer: CTkFrame, modelBuffer: CTkLabel, newModelFrame: CTkFrame, existingModelFrame: CTkFrame):
    # data = find_serial(input)
    # data = {
    #     'modelName': "CANEO B 45"
    # }
    new = False
    frameBuffer.grid(row=2, column=1, pady=5)

    if new:
        newModel_frame.grid(row=3, column=1, pady=5)
    else:
        existingModel_frame.grid(row=3, column=1, pady=5) 
        modelBuffer.configure(text=input)
    
ctk.set_appearance_mode("light")
#window
window = CTk()
window.title("Injector")
window.geometry("600x600")
globalFont = CTkFont("arial", 15)
main_frame = CTkFrame(window)
main_frame.pack()

#title
title = CTkLabel(main_frame,
    text="הכנסת נתונים",
    font=CTkFont("arial", 20)
)
title.grid(row=0, column=1, pady=5)

#serial
serial_frame = CTkFrame(main_frame)
serial_frame.grid(row=1, column=1, pady=5)

serial_label = CTkLabel(serial_frame,
    text="  :מס' סריאלי ",
    font=globalFont
)
serial_label.grid(row=0, column=2)

serial_input = CTkEntry(serial_frame)
serial_input.grid(row=0, column=1, padx=10)



serial_sumbit = CTkButton(main_frame,
    text = "חפש",
    width = 10,
    command = lambda: submit_serial(serial_input.get(),
                                     form_frame,
                                       existingModel_Name,
                                         newModel_frame,
                                           existingModel_frame)
)
serial_sumbit.grid(row=1, column=0, pady=5)


#   form
#name
form_frame = CTkFrame(main_frame)

name_label = CTkLabel(form_frame,
    text="  :שם",
    font=globalFont
)
name_label.grid(row=0, column=1, pady=5)

name_input = CTkEntry(form_frame)
name_input.grid(row=0, column=0, padx=10, pady=5)

#id
id_label = CTkLabel(form_frame,
    text=":מס' זהות",
    font=globalFont
)
id_label.grid(row=1, column=1, pady=5)

id_input = CTkEntry(form_frame)
id_input.grid(row=1, column=0, padx=10, pady=5)

#date
date_label = CTkLabel(form_frame,
    text=":מועד אספקה",
    font=globalFont
)
date_label.grid(row=3, column=1, pady=5)

date_input = CTkEntry(form_frame)
date_input.grid(row=3, column=0, padx=10, pady=5)

#   model frames
#new model
newModel_frame = CTkFrame(main_frame)
newModel_label = CTkLabel(newModel_frame,
    text="       :דגם      ",
    font=globalFont
)
newModel_label.grid(row=0, column=1)

newModel_input = CTkEntry(newModel_frame)
newModel_input.grid(row=0, column=0, padx=10)

#existing model
existingModel_frame = CTkFrame(main_frame)
existingModel_label = CTkLabel(existingModel_frame,
    text="       :דגם      ",
    font=globalFont
)
existingModel_label.grid(row=0, column=1)

existingModel_Name = CTkLabel(existingModel_frame)
existingModel_Name.grid(row=0, column=0, padx=10)

# serial_input.bind('<Enter>', 
#     lambda: submit_serial(serial_input.get(),
#                                      form_frame,
#                                        existingModel_Name,
#                                          newModel_frame,
#                                            existingModel_frame)
# )

window.mainloop()