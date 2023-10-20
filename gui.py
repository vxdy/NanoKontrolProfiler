import tkinter as tk
from math import ceil
from variables import config

from developer_func import test_mode, log


def reset_channel():
    global current_channel
    config['current_channel'] = 1


def set_setup_trackup():
    config['setup_trackup'] = True
    log("ok")


def set_setup_trackdown():
    config['setup_trackdown'] = True


def set_setup_exclude():
    global set_exclude
    set_exclude = True

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

        button_set_down = tk.Button(self, text="Set Down", command=set_setup_trackdown)
        button_set_down.pack(pady=10)

        button_set_up = tk.Button(self, text="Set Up", command=set_setup_trackup)
        button_set_up.pack(pady=10)

        button_reset = tk.Button(self, text="Reset", command=set_setup_exclude)
        button_reset.pack(pady=10)

        self.channel_label.config(text=str(0))




class Settingspage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)


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
