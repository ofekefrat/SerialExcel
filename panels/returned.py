from customtkinter import *
from .panel import Panel, TextBox
from config import *

class ReturnedPanel(Panel):
    def __init__(self, root: CTk):
        self.root = root
        background = root.cget("fg_color")
        main_frame = CTkFrame(root, bg_color=background, fg_color=background)
        self.main_frame = main_frame

        #Frame content

        self.msg_label = CTkLabel(main_frame, text_color="white", font=generalFont, corner_radius=5)
    
        # title
        title = CTkLabel(
            main_frame,
            text="החזרות",
            font=CTkFont("arial", 23, underline=True),
            bg_color=background,
        )
        title.grid(row=0, column=1, pady=30)

        form_frame = CTkFrame(main_frame, fg_color=background)
        # self.form_frame = form_frame

        name_input = TextBox(
            master=form_frame, row=0, column=0, label_text=":שם הזכאי"
        )
        name_input.show()

        
        

        
        

        
        

    def start(self):
        self.main_frame.pack()

    def stop(self):
        self.main_frame.pack_forget()