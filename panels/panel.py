from customtkinter import *
from config import *

class Panel:
    """Parent class for panels"""
    def start(self):
        pass

    def stop(self):
        pass


class TextBox:
    """Text box with a label next to it."""
    def __init__(self, master: CTk | CTkFrame, row, column, label_text: str):
        background = master.cget("fg_color")
        self.row = row
        self.column = column
        self.frame = CTkFrame(master, fg_color=background)

        self.label = CTkLabel(
            master = self.frame, 
            font = generalFont,
            text = label_text,
            bg_color = background
        )
        self.label.grid(column=1)

        self.input = CTkEntry(
            master=self.frame,
            bg_color=background,
            font=generalFont,
            justify='right'
        )
        self.input.grid(column=0, padx=10)

    def show(self):
        self.frame.grid(row=self.row, column=self.column, pady=5)

    def get(self) -> str:
        return self.input.get()