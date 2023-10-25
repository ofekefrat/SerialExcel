import customtkinter as ctk
from customtkinter import *
from tkcalendar import DateEntry
from serial_module import Item

item = None

def submit_serial(input,
                  formFrame: CTkFrame,
                  newModelFrame: CTkFrame,
                  existingModelFrame: CTkFrame,
                  existingModelName: CTkLabel,
                  prevName: CTkLabel,
                  prevNameLabel: CTkLabel,
                  infoSubmitBtn: CTkButton,
                  deviceReturnFrame: CTkFrame,
                  deviceReturnName: CTkLabel
                  ):
    global item
    item = None

    msg_label.grid_forget()
    existingModelFrame.grid_forget()
    newModelFrame.grid_forget()
    prevName.grid_forget()
    prevNameLabel.grid_forget()
    formFrame.grid_forget()
    infoSubmitBtn.grid_forget()
    deviceReturnFrame.grid_forget()


    tempItem = Item(input)

    if isinstance(tempItem.wb, FileNotFoundError) or isinstance(tempItem.sheet, KeyError):
        show_msg("מספר סריאלי לא קיים", error=True)
        return
    
    if tempItem.returned or tempItem.new:
        form_frame.grid(row=2, column=1, pady=5)
        infoSubmitBtn.grid(row=4, column=1, pady=5)

    if tempItem.new:
        newModelFrame.grid(row=3, column=1, pady=5)
    else:
        existingModelFrame.grid(row=3, column=1, pady=5) 
        existingModelName.configure(text=tempItem.modelName)

        if tempItem.returned:
            prevNameLabel.grid(row=0, column=1, pady=5, padx=(0, 20))
            prevName.grid(row=0, column=0, padx=10, pady=5)
            prevName.configure(text=tempItem.prevName)
        else:
            deviceReturnFrame.grid(row=4, column=1, pady=5)
            deviceReturnName.configure(text = tempItem.prevName)

    item = tempItem


def submit_info(name, id, date, modelEntry: CTkEntry):
    model = modelEntry.get()
    date = date.strftime("%d/%m/%y")
    try:
        item.updateInfo(name, id, date, model)
        show_msg("הקובץ עודכן בהצלחה", error=False)
    except PermissionError:
        show_msg("הקובץ המתבקש נמצא בשימוש, אנא דאג לסגירתו", error=True)


def submit_returned():
    try:
        item.setReturned()
        show_msg("הקובץ עודכן בהצלחה", error=False)
    except PermissionError:
        show_msg("הקובץ המתבקש נמצא בשימוש, אנא דאג לסגירתו", error=True)

def show_msg(description, error):
    global msg_label
    msg_label.configure(text=description)
    if error:
        msg_label.configure(bg_color="red")
    else:
        msg_label.configure(bg_color="green")
    msg_label.grid(row=5, column=1)
            
ctk.set_appearance_mode("light")
#window
background = "#EAEAEA"
window = CTk()
window.title("Injector")
window.geometry("600x600")
generalFont = CTkFont("arial", 15)
btnFont = CTkFont("arial", 17)
infoFont = CTkFont("arial bold", 17)

main_frame = CTkFrame(window, bg_color=background, fg_color=background)
main_frame.pack()

#title
title = CTkLabel(main_frame,
    text="הכנסת נתונים",
    font=CTkFont("arial", 23, underline=True),
    bg_color=background
)
title.grid(row=0, column=1, pady=5)

#serial
serial_frame = CTkFrame(main_frame, fg_color=background)
serial_frame.grid(row=1, column=1, pady=5)

serial_label = CTkLabel(serial_frame,
    text="  :מס' סריאלי ",
    font=generalFont,
    bg_color=background
)
serial_label.grid(row=0, column=2)

serial_input = CTkEntry(serial_frame, bg_color=background, font=generalFont)
serial_input.grid(row=0, column=1, padx=10)

serial_sumbit_btn = CTkButton(main_frame,
    text = "חפש",
    width = 10,
    font = btnFont,
    bg_color = background,
    command = lambda: submit_serial(serial_input.get(),
                                    form_frame,
                                    newModel_frame,
                                    existingModel_frame,
                                    existingModel_Name,
                                    prev_name,
                                    prev_name_label,
                                    info_submit_btn,
                                    deviceReturn_frame,
                                    deviceReturn_name)
)
serial_sumbit_btn.grid(row=1, column=0, pady=5)


#   form
#name
form_frame = CTkFrame(main_frame, fg_color=background)

name_label = CTkLabel(form_frame,
    text="  :שם",
    font=generalFont,
    bg_color=background
)
name_label.grid(row=0, column=3, pady=5)

name_input = CTkEntry(form_frame, bg_color=background, font=generalFont, justify = "right")
name_input.grid(row=0, column=2, padx=10, pady=5)

#previous name
prev_name_label = CTkLabel(form_frame,
    text=":זכאי קודם",
    font=generalFont,
    bg_color=background
)

prev_name = CTkLabel(form_frame, bg_color=background, font=infoFont, justify = "right")

#id
id_label = CTkLabel(form_frame,
    text=":מס' זהות",
    font=generalFont, 
    bg_color=background
)
id_label.grid(row=1, column=3, pady=5)

id_input = CTkEntry(form_frame, bg_color=background, font=generalFont)
id_input.grid(row=1, column=2, padx=10, pady=5)

#date
date_label = CTkLabel(form_frame,
    text=":מועד אספקה",
    font=generalFont,
    bg_color=background
)
date_label.grid(row=3, column=3, pady=5)

date_input = DateEntry(form_frame)
date_input.grid(row=3, column=2, padx=10, pady=5)

#   model frames
#new model
newModel_frame = CTkFrame(main_frame, fg_color=background)
newModel_label = CTkLabel(newModel_frame,
    text="       :דגם      ",
    font=generalFont,
    bg_color=background
)
newModel_label.grid(row=0, column=1)

newModel_input = CTkEntry(newModel_frame, bg_color=background, font=generalFont)
newModel_input.grid(row=0, column=0, padx=10)

#existing model
existingModel_frame = CTkFrame(main_frame, fg_color=background)
existingModel_label = CTkLabel(existingModel_frame,
    text="       :דגם      ",
    font=generalFont,
    bg_color=background
)
existingModel_label.grid(row=0, column=1)

existingModel_Name = CTkLabel(existingModel_frame, bg_color=background, font=infoFont)
existingModel_Name.grid(row=0, column=0, padx=10)

info_submit_btn = CTkButton(main_frame, bg_color=background,
    text = "הוסף מידע",
    font = CTkFont("arial", 17),
    command = lambda: submit_info(name_input.get(),
                                  id_input.get(),
                                  date_input.get_date(),
                                  newModel_input)
)

# return
deviceReturn_frame = CTkFrame(main_frame, fg_color=background)
deviceReturn_label = CTkLabel(deviceReturn_frame, 
                               bg_color=background,
                               font = generalFont,
                               text = " :המוצר לא הוחזר מזכאי קודם")
deviceReturn_label.grid(row=0, column=2)
deviceReturn_name = CTkLabel(deviceReturn_frame, bg_color=background, font=infoFont)
deviceReturn_name.grid(row=0, column=1, padx=10)

deviceReturn_btn = CTkButton(deviceReturn_frame, bg_color=background,
    text = "סמן הוחזר",
    font = btnFont,
    command = lambda: submit_returned()
)
deviceReturn_btn.grid(row=0, column=0, padx=10)

msg_label = CTkLabel(main_frame, text_color="white", font=generalFont, corner_radius=5)

window.mainloop()