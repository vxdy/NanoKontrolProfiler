import tkinter as tk
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


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Mainpage(Page):
    channel_label = None
    trackup_lable = None
    trackdown_lable = None

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.channel_label = tk.Label(self, text="", font=("Helvetica", 24))
        self.channel_label.pack(padx=20, pady=20)

        if test_mode:
            self.trackup_lable = tk.Label(self, text="", font=("Helvetica", 24))
            self.trackup_lable.pack(padx=20, pady=20)

            self.trackdown_lable = tk.Label(self, text="", font=("Helvetica", 24))
            self.trackdown_lable.pack(padx=20, pady=20)

        # Create buttons for "Set Up," "Set Down," and "Reset"

        self.channel_label.config(text=str(0))


class Settingspage(Page):
    trackdown_lable = ""
    trackup_lable = ""
    exclude_lable = ""
    current_warning = ""

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        firstbuttonframe = tk.Frame(self)
        secondbuttonframe = tk.Frame(self)
        thirdbuttonframe = tk.Frame(self)

        secondbuttonframe.pack(side="top", fill="x", expand=False)
        self.trackup_lable = tk.Label(secondbuttonframe, text="Current: 00", font=("Helvetica", 10))
        self.trackup_lable.pack(side="left")

        button_set_up = tk.Button(secondbuttonframe, text="Set Up", command=set_setup_trackup)
        button_set_up.pack(pady=10, side="left")

        firstbuttonframe.pack(side="top", fill="x", expand=False)
        self.trackdown_lable = tk.Label(firstbuttonframe, text="Current: 00", font=("Helvetica", 10))
        self.trackdown_lable.pack(side="left")

        button_set_down = tk.Button(firstbuttonframe, text="Set Down", command=set_setup_trackdown)
        button_set_down.pack(pady=10, side="left")

        button_reset = tk.Button(self, text="Exclude Button", command=set_setup_exclude)
        button_reset.pack(pady=10)

        reset_exclude = tk.Button(self, text="Reset Excludes", command=reset_exludes)
        reset_exclude.pack(pady=10)

        self.current_warning = tk.Label(self, text="", font=("Helvetica", 10))
        self.current_warning.pack(side="left")


class MainView(tk.Frame):
    mainpage = None
    settingspage = None

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.mainpage = Mainpage(self)
        self.settingspage = Settingspage(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        self.mainpage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.settingspage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        buttonmain = tk.Button(buttonframe, text="Home", command=self.mainpage.show)
        buttonmain.pack(side="left")

        buttonsettings = tk.Button(buttonframe, text="Settings", command=self.settingspage.show)
        buttonsettings.pack(side="left")

        self.mainpage.show()

    def set_current_channel(self, text):
        self.mainpage.config(text=text)
