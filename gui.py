import tkinter as tk
import customtkinter as ctk

from math import ceil

from configloader import save_config
from variables import config

from developer_func import test_mode, log


def reset_channel():
    global current_channel
    config['current_channel'] = 1


def set_setup_trackup():
    config['setup_trackup'] = True
    config['current_warning'] = "Press the Button you want \n to use to increase the Profile"


def set_setup_trackdown():
    config['setup_trackdown'] = True
    config['current_warning'] = "Press the Button you want \n to use to decrease the Profile"


def set_setup_exclude():
    config['set_exclude'] = True
    config['current_warning'] = "Press the Button \n that you want to exlude"


def reset_exludes():
    config['excluded'] = []
    save_config()
    config['current_warning'] = "Your Exludes \n were Resetted"


class Page(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        ctk.CTkFrame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Mainpage(Page):
    channel_label = None
    trackup_lable = None
    trackdown_lable = None

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.channel_label = ctk.CTkLabel(self, text="", font=("Helvetica", 60))
        self.channel_label.place(relx=.5, rely=.5, anchor="c")

        # Create buttons for "Set Up," "Set Down," and "Reset"

        self.channel_label.configure(text=str(0))


class Settingspage(Page):
    trackdown_lable = ""
    trackup_lable = ""
    exclude_lable = ""
    current_warning = ""

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        firstbuttonframe = ctk.CTkFrame(self, fg_color="transparent")
        secondbuttonframe = ctk.CTkFrame(self, fg_color="transparent")

        secondbuttonframe.pack(side="top", pady=10, fill="x", expand=False, anchor="c")
        self.trackup_lable = ctk.CTkLabel(secondbuttonframe, text="Current: 00", font=("Helvetica", 16))
        self.trackup_lable.pack(side="left", padx=5)

        button_set_up = ctk.CTkButton(secondbuttonframe, text="Set Up", command=set_setup_trackup)
        button_set_up.place(relx=.5, rely=.5, anchor="c")

        firstbuttonframe.pack(side="top", pady=10, fill="x", expand=False, anchor="c")
        self.trackdown_lable = ctk.CTkLabel(firstbuttonframe, text="Current: 00", font=("Helvetica", 16))
        self.trackdown_lable.pack(side="left", padx=5)

        button_set_down = ctk.CTkButton(firstbuttonframe, text="Set Down", command=set_setup_trackdown)
        button_set_down.place(relx=.5, rely=.5, anchor="c")

        button_reset = ctk.CTkButton(self, text="Exclude Button", command=set_setup_exclude)
        button_reset.pack(pady=10)

        reset_exclude = ctk.CTkButton(self, text="Reset Excludes", command=reset_exludes)
        reset_exclude.pack(pady=10)

        self.current_warning = ctk.CTkLabel(self, text="", font=("Helvetica", 14))
        self.current_warning.place(relx=.5, rely=.75, anchor="c")


class MainView(ctk.CTkFrame):
    mainpage = None
    settingspage = None

    def __init__(self, *args, **kwargs):
        ctk.CTkFrame.__init__(self, *args, **kwargs)
        self.mainpage = Mainpage(self)
        self.settingspage = Settingspage(self)

        buttonframe = ctk.CTkFrame(self)
        container = ctk.CTkFrame(self)
        buttonframe.pack(side="top")
        container.pack(side="top", fill="both", expand=True)

        self.mainpage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.settingspage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        buttonmain = ctk.CTkButton(buttonframe, text="Home", command=lambda: self.show_mainpage())
        buttonmain.pack(side="left")

        buttonsettings = ctk.CTkButton(buttonframe, text="Settings", command=lambda: self.show_settings())
        buttonsettings.pack(side="left")

        self.mainpage.show()

    def show_settings(self):
        config['current_width'] = "200"
        config['current_height'] = "350"

        self.settingspage.show()

    def show_mainpage(self):
        config['current_width'] = "200"
        config['current_height'] = "200"

        self.mainpage.show()
