from tkinter import *
# import serial_module as Serial

color = "white"

window = Tk()
window.title("Injector")
window.geometry("800x800")
window.configure(background='lightgreen')
for i in range(0, 9):
    window.columnconfigure(index=i, weight=1)
    window.rowconfigure(index=i, weight=1)

existing_model = None

title_label = Label(
    text = "הכנסת נתונים",
    background = color,
    # font=("Arial Bold", 30)
).grid(row=0, column=3)

serial_entry_label = Label(
    text = "מספר סריאלי",
    background = color,
    # font=("Arial", 12)
).grid(row=1, column=9)
serial_entry_label = Label(
    text = "מספר סריאלי",
    background = color,
    # font=("Arial", 12)
).grid(row=1, column=8)
serial_entry_label = Label(
    text = "מספר סריאלי",
    background = color,
    # font=("Arial", 12)
).grid(row=1, column=7)
serial_entry_label = Label(
    text = "מספר סריאלי",
    background = color,
    # font=("Arial", 12)
).grid(row=1, column=6)
serial_entry_label = Label(
    text = "מספר סריאלי",
    background = color,
    # font=("Arial", 12)
).grid(row=1, column=5)
serial_entry_label = Label(
    text = "מספר סריאלי",
    background = color,
    # font=("Arial", 12)
).grid(row=1, column=4)
serial_entry_label = Label(
    text = "מספר סריאלי",
    background = color,
    # font=("Arial", 12)
).grid(row=1, column=2)
serial_entry_label = Label(
    text = "מספר סריאלי",
    background = color,
    # font=("Arial", 12)
).grid(row=1, column=1)
serial_entry_label = Label(
    text = "מספר סריאלי",
    background = color,
    # font=("Arial", 12)
).grid(row=1, column=0)

serial_entry = Entry(
    fg="black",
    bg="white",
).grid(row=1, column=3)

existing_model_label = Label(
    text = existing_model,
    background = color,
    # font=("Arial", 20)
).grid(row=2, column=3)



window.mainloop()