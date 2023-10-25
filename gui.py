import tkinter as tk
from pathlib import Path

from configloader import save_config
from variables import config

from developer_func import DEVELOPER_MODE, log
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


#ASSETS_PATH = Path(str(Path().parent) + "\\assets\\frame0")
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_MAIN = OUTPUT_PATH / Path(r"C:\Users\Marco\Desktop\Project\NanoKontrolProfiler\guitest\build\assets\frame0")
ASSETS_PATH_SECOND = OUTPUT_PATH / Path(r"C:\Users\Marco\Desktop\Project\NanoKontrolProfiler\guitest\build\assets\frame1")



def relative_to_assets(path: str, window) -> Path:
    if(window == "settings"):
        return ASSETS_PATH_SECOND / Path(path)
    return ASSETS_PATH_MAIN / Path(path)


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

    def __init__(self, main_view, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_view = main_view
        Page.__init__(self, *args, **kwargs)
        canvas = Canvas(
            self,
            bg="#2D2D2D",
            height=250,
            width=250,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png", "main"))
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.on_button_press,
            relief="flat"
        )
        button_1.place(
            x=200.0,
            y=15.0,
            width=35.0,
            height=35.0
        )

        canvas.create_text(
            96.0,
            111.0,
            anchor="nw",
            text="1",
            fill="#FFFFFF",
            font=("Inter Bold", 64 * -1)
        )

        canvas.create_text(
            61.0,
            72.0,
            anchor="nw",
            text="Profile",
            fill="#FFFFFF",
            font=("Inter Bold", 40 * -1)
        )

    def on_button_press(self):
        self.main_view.show_settings()


class Settingspage(Page):
    trackdown_lable = ""
    trackup_lable = ""
    exclude_lable = ""
    current_warning = ""

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        self.canvas = Canvas(
            container,
            bg="#2D2D2D",
            height=422,
            width=330,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png", "settings"))
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=83.0,
            y=86.0,
            width=163.0,
            height=39.0,

        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png", "settings"))
        button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=84.0,
            y=150.0,
            width=163.0,
            height=39.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png", "settings"))
        button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=84.0,
            y=214.0,
            width=163.0,
            height=39.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png", "settings"))
        button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=83.0,
            y=278.0,
            width=163.0,
            height=39.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png", "settings"))
        button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=8.0,
            y=19.0,
            width=127.0,
            height=27.0
        )

        self.canvas.create_text(
            38.0,
            331.0,
            anchor="nw",
            text="Info Text",
            fill="#FFFFFF",
            font=("Inter Bold", 14 * -1)
        )

        self.canvas.create_text(
            151.0,
            68.0,
            anchor="nw",
            text="0",
            fill="#FFFFFF",
            font=("Inter Medium", 16 * -1)
        )

        self.canvas.create_text(
            151.0,
            132.0,
            anchor="nw",
            text="0",
            fill="#FFFFFF",
            font=("Inter Medium", 16 * -1)
        )


class MainView(tk.Frame):
    mainpage = None
    settingspage = None

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.mainpage = Mainpage(self, self)
        self.settingspage = Settingspage(self, self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        self.mainpage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.settingspage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)



        self.mainpage.show()

    def set_current_channel(self, text):
        self.mainpage.config(text=text)

    def show_settings(self):
        self.mainpage.show()
        self.settingspage.place_forget

        #self.settingspage.show()

    def show_main(self):
        self.mainpage.show()
