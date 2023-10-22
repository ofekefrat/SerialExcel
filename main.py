# from serial_module import *
from customtkinter import *

def submit_serial(input, frameBuffer: CTkFrame, modelBuffer: CTkLabel, newModelFrame: CTkFrame, existingModelFrame: CTkFrame):
    # data = find_serial(input)
    # data = {
    #     'modelName': "CANEO B 45"
    # }
    new = False
    frameBuffer.pack()

    if new:
        newModel_frame.pack()
    else:
        existingModel_frame.pack() 
        modelBuffer.configure(text=input)
    
#window
window = CTk()
window.title("Injector")
window.geometry("600x600")
globalFont = CTkFont("arial", 15)

#title
title = CTkLabel(window,
    text="הכנסת נתונים",
    font=CTkFont("arial", 20)
)
title.pack()

#serial
serial_frame = CTkFrame(window)
serial_frame.pack()

serial_label = CTkLabel(serial_frame,
    text=":מס' סריאלי",
    font=globalFont
)
serial_label.grid(row=0, column=2)

serial_input = CTkEntry(serial_frame)
serial_input.grid(row=0, column=1, padx=10)



serial_sumbit = CTkButton(serial_frame,
    text = "חפש",
    width = 10,
    command = lambda: submit_serial(serial_input.get(),
                                     form_frame,
                                       existingModel_Name,
                                         newModel_frame,
                                           existingModel_frame)
)
serial_sumbit.grid(row=0, column=0)


#   form
#name
form_frame = CTkFrame(window)

name_label = CTkLabel(form_frame,
    text="  :שם",
    font=globalFont
)
name_label.grid(row=0, column=1)

name_input = CTkEntry(form_frame)
name_input.grid(row=0, column=0, padx=10)

#id
id_label = CTkLabel(form_frame,
    text=":מס' זהות",
    font=globalFont
)
id_label.grid(row=1, column=1)

id_input = CTkEntry(form_frame)
id_input.grid(row=1, column=0, padx=10)

#date
date_label = CTkLabel(form_frame,
    text=":מועד אספקה",
    font=globalFont
)
date_label.grid(row=3, column=1)

date_input = CTkEntry(form_frame)
date_input.grid(row=3, column=0, padx=10)

#   model frames
#new model
newModel_frame = CTkFrame(window)
newModel_label = CTkLabel(newModel_frame,
    text=":דגם",
    font=globalFont
)
newModel_label.grid(row=0, column=1)

newModel_input = CTkEntry(newModel_frame)
newModel_input.grid(row=0, column=0, padx=10)

#existing model
existingModel_frame = CTkFrame(window)
existingModel_label = CTkLabel(existingModel_frame,
    text=":דגם",
    font=globalFont
)
existingModel_label.grid(row=0, column=1)

existingModel_Name = CTkLabel(existingModel_frame)
existingModel_Name.grid(row=0, column=0, padx=10)

serial_input.bind('<Enter>', 
    lambda: submit_serial(serial_input.get(),
                                     form_frame,
                                       existingModel_Name,
                                         newModel_frame,
                                           existingModel_frame)
)

window.mainloop()