from .panel import Panel
from customtkinter import *
from tkcalendar import DateEntry
from excel_serial import Item

class SerialEntryPanel(Panel):
    def __init__(self, root: CTk):
        self.root = root
        background = root.cget("fg_color")
        self.main_frame = CTkFrame(root, bg_color=background, fg_color=background)
        generalFont = CTkFont("arial", 15)
        btnFont = CTkFont("arial", 17)
        infoFont = CTkFont("arial bold", 17)

        # Frame content
        
        self.msg_label = CTkLabel(self.main_frame, text_color="white", font=generalFont, corner_radius=5)

        # title
        title = CTkLabel(
            self.main_frame,
            text="סריאלי",
            font=CTkFont("arial", 23, underline=True),
            bg_color=background,
        )
        title.grid(row=0, column=1, pady=30)


        # serial
        self.serial_frame = CTkFrame(self.main_frame, fg_color=background)
        self.serial_frame.grid(row=1, column=1, pady=5)

        serial_label = CTkLabel(
            self.serial_frame, text="  :מס' סריאלי ", font=generalFont, bg_color=background
        )
        serial_label.grid(row=0, column=3)

        serial_input = CTkEntry(self.serial_frame, bg_color=background, font=generalFont)
        serial_input.grid(row=0, column=2, padx=10)

        serial_droplist = CTkOptionMenu(
            self.serial_frame,
            bg_color=background,
            fg_color="white",
            button_color="white",
            button_hover_color="gray",
            font=generalFont,
            text_color="black",
            anchor="e",
            width=20,
            values=["2400-03-", "2400-24-", "N220", "N160", "N50", "N60"],
        )
        serial_droplist.grid(row=0, column=1)

        serial_sumbit_btn = CTkButton(
            self.main_frame,
            text="חיפוש",
            width=10,
            font=btnFont,
            bg_color=background,
            command=lambda: self.submit_serial(
                serial_droplist.get() + serial_input.get()
            )
        )
        serial_sumbit_btn.grid(row=1, column=0, padx=15)


        #   form
        # name
        self.form_frame = CTkFrame(self.main_frame, fg_color=background)

        name_label = CTkLabel(self.form_frame, text="  :שם", font=generalFont, bg_color=background)
        name_label.grid(row=0, column=3, pady=5)

        self.name_input = CTkEntry(
            self.form_frame, bg_color=background, font=generalFont, justify="right"
        )
        self.name_input.grid(row=0, column=2, padx=10, pady=5)


        # previous name
        self.prev_name_label = CTkLabel(
            self.form_frame, text=":זכאי קודם", font=generalFont, bg_color=background
        )
        self.prev_name = CTkLabel(self.form_frame, bg_color=background, font=infoFont, justify="right")


        # id
        id_label = CTkLabel(self.form_frame, text=":מס' זהות", font=generalFont, bg_color=background)
        id_label.grid(row=1, column=3, pady=5)

        self.id_input = CTkEntry(self.form_frame, bg_color=background, font=generalFont)
        self.id_input.grid(row=1, column=2, padx=10, pady=5)


        # date
        date_label = CTkLabel(
            self.form_frame, text=":מועד אספקה", font=generalFont, bg_color=background
        )
        date_label.grid(row=3, column=3, pady=5)

        self.date_input = DateEntry(self.form_frame, date_pattern="dd/mm/yy")
        self.date_input.grid(row=3, column=2, padx=10, pady=5)


        #   model frames
        # new model
        self.new_model_frame = CTkFrame(self.main_frame, fg_color=background)
        new_model_label = CTkLabel(
            self.new_model_frame, text="       :דגם      ", font=generalFont, bg_color=background
        )
        new_model_label.grid(row=0, column=1)

        self.new_model_input = CTkEntry(self.new_model_frame, bg_color=background, font=generalFont)
        self.new_model_input.grid(row=0, column=0, padx=10)


        # existing model
        self.existing_model_frame = CTkFrame(self.main_frame, fg_color=background)
        existing_model_label = CTkLabel(
            self.existing_model_frame, text="       :דגם      ", font=generalFont, bg_color=background
        )
        existing_model_label.grid(row=0, column=1)

        self.existing_model_Name = CTkLabel(self.existing_model_frame, bg_color=background, font=infoFont)
        self.existing_model_Name.grid(row=0, column=0, padx=10)

        device_birthday_label = CTkLabel(
            self.existing_model_frame, bg_color=background, font=generalFont, text=":תאריך הנפקת מוצר"
        )
        device_birthday_label.grid(row=1, column=1, padx=10)

        self.device_birthday_date = CTkLabel(self.existing_model_frame, bg_color=background, font=infoFont)
        self.device_birthday_date.grid(row=1, column=0, padx=10)

        self.info_submit_btn = CTkButton(
            self.main_frame,
            bg_color=background,
            text="הוסף מידע",
            font=CTkFont("arial", 17),
            command=lambda: self.submit_info()
        )


        # return
        self.device_return_frame = CTkFrame(self.main_frame, fg_color=background)
        device_return_label = CTkLabel(
            self.device_return_frame,
            bg_color=background,
            font=generalFont,
            text=" :המוצר לא הוחזר מזכאי קודם",
        )
        device_return_label.grid(row=0, column=2)
        self.device_return_name = CTkLabel(self.device_return_frame, bg_color=background, font=infoFont)
        self.device_return_name.grid(row=0, column=1, padx=10)

    def start(self):
        self.main_frame.pack()

    def stop(self):
        self.main_frame.pack_forget()

    def submit_serial(self, input):
        self.item = None

        self.msg_label.grid_forget()
        self.existing_model_frame.grid_forget()
        self.new_model_frame.grid_forget()
        self.prev_name.grid_forget()
        self.prev_name_label.grid_forget()
        self.form_frame.grid_forget()
        self.info_submit_btn.grid_forget()
        self.device_return_frame.grid_forget()

        clear_entry(self.name_input)
        clear_entry(self.id_input)
        clear_entry(self.new_model_input)

        tempItem = Item(input)

        if (
            isinstance(tempItem._wb, FileNotFoundError)
            or isinstance(tempItem.sheet, KeyError)
            or tempItem.row == -1
        ):
            self.show_msg("מספר סריאלי לא נמצא", error=True)
            return

        if isinstance(tempItem.prevName, AttributeError):
            self.show_msg("נראה כי יש בעיה עם השורה המתבקשת. אנא בדקו אותה בקובץ הסריאלי", error=True)
            return

        if tempItem.returned or tempItem.new:
            self.form_frame.grid(row=2, column=1, pady=5)
            self.info_submit_btn.grid(row=4, column=1, pady=5)

        if tempItem.new:
            self.new_model_frame.grid(row=3, column=1, pady=5)
        else:
            self.existing_model_frame.grid(row=3, column=1, pady=5)
            self.existing_model_Name.configure(text=tempItem.modelName)
            self.device_birthday_date.configure(text=tempItem.deviceBirthday)

            if tempItem.returned:
                self.prev_name_label.grid(row=0, column=1, pady=5, padx=(0, 20))
                self.prev_name.grid(row=0, column=0, padx=10, pady=5)
                self.prev_name.configure(text=tempItem.prevName)
            else:
                self.device_return_frame.grid(row=4, column=1, pady=5)
                self.device_return_name.configure(text=tempItem.prevName)

        self.item = tempItem

    def submit_info(self):
        try:
            success = self.item._update_info(
                self.name_input.get(),
                self.id_input.get(),
                self.date_input.get_date().strftime("%d/%m/%y"),
                self.new_model_input.get()
                )
            if not success:
                self.show_msg(
                    'השורה עודכנה ע"י משתמש אחר. אנא הקש "חיפוש" שנית', error=True
                )
                return
            else:
                self.show_msg("הקובץ עודכן בהצלחה", error=False)
                self.info_submit_btn.grid_forget()
        except PermissionError:
            self.show_msg("הקובץ המתבקש נמצא בשימוש, אנא דאג לסגירתו", error=True)

    def submit_returned(self):
        try:
            success = self.item._set_returned()
            if not success:
                self.show_msg(
                    'השורה עודכנה ע"י משתמש אחר. אנא הקש "חיפוש" שנית', error=True
                )
            else:
                self.show_msg("הקובץ עודכן בהצלחה", error=False)
        except PermissionError:
            self.show_msg("הקובץ המתבקש נמצא בשימוש, אנא דאג לסגירתו", error=True)

    def show_msg(self, description, error):
        self.msg_label.configure(text=description)
        if error:
            self.msg_label.configure(bg_color="red")
        else:
            self.msg_label.configure(bg_color="green")
        self.msg_label.grid(row=5, column=1)


def clear_entry(widget: CTkEntry):
    widget.delete(0, "end")
