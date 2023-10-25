import os
from math import ceil
from time import sleep

import mido
import tkinter as tk
import threading
import json

import configloader
import variables
from configloader import load_config, save_config
from gui import MainView
from variables import config

from developer_func import *

tempconfig = load_config()

config['trackdown'] = tempconfig['trackdown']
config['trackup'] = tempconfig['trackup']
config['excluded'] = tempconfig['excluded']

# Specify the updated names of the source and destination MIDI ports
source_port_name = "nanoKONTROL2"
destination_port_name = "pymid"

isMacOS = False

#GUI Variables
guiWidth = 250
guiHight = 250

# MAC Support
try:
    import rtmidi

    vmidi_out = rtmidi.MidiOut()
    vmidi_out.open_virtual_port('pymid')
    isMacOS = True
except NotImplementedError as e:
    pass

try:
    # Find exakt Midi Names
    korg_port_name = [s for s in mido.get_input_names() if source_port_name in s][0]
    virtual_port_name = [g for g in mido.get_output_names() if destination_port_name in g][0]
except IndexError as e:
    log(mido.get_input_names())
    log(mido.get_output_names())
    log(e)
    log("Device not found")
    exit(500)

root = tk.Tk()
root.title("Nanoprofiler")
root.attributes('-topmost', True)


main = MainView(root)
main.pack(side="top", fill="both", expand=True)


# Function to update the channel display in the tkinter GUI
def update_channel_display():

    root.geometry("{}x{}".format(guiWidth, guiHight))
    root.configure(bg="#2D2D2D")

    while True:
        #main.mainpage.channel_label.config(text=str(ceil(config['current_channel'])))
        #main.settingspage.trackup_lable.config(text=str(ceil(config['trackup'])))
        #main.settingspage.trackdown_lable.config(text=str(ceil(config['trackdown'])))
        #main.settingspage.current_warning.config(text=str(config['current_warning']))
        #if DEVELOPER_MODE:
        #    main.mainpage.trackdown_lable.config(text=str(ceil(config['trackdown'])))
        #    main.mainpage.trackup_lable.config(text=str(ceil(config['trackup'])))
        root.update()


# Function to handle MIDI messages
def handle_midi_messages():
    global current_channel  # Declare current_channel as a global variable
    global source_port
    global destination_port
    global setup_trackdown
    global setup_trackup
    global set_exclude
    global trackdown
    global trackup
    global excluded
    global config

    try:
        log(f"Using input port: {source_port_name}")
        log(f"Using output port: {destination_port_name}")

        source_port = mido.open_input(korg_port_name)
        destination_port = mido.open_output(virtual_port_name)

        log(f"Listening to MIDI port '{source_port_name}'...")

        for data in source_port:

            if config['setup_trackdown']:
                config['trackdown'] = data.control
                config['setup_trackdown'] = False
                config['current_warning'] = "Button " + str(data.control) + " was set \n as profile down button"
                save_config()

            if config['setup_trackup']:
                config['trackup'] = data.control
                config['setup_trackup'] = False
                config['current_warning'] = "Button " + str(data.control) + " was set \n as profile up button"
                save_config()

            if config['set_exclude']:

                if data.control not in config['excluded']:
                    config['excluded'].append(data.control)
                    config['current_warning'] = "Button " + str(data.control) + " is \n excluded"
                else:
                    config['current_warning'] = "Button " + str(data.control) + " is \n already excluded"
                config['set_exclude'] = False
                save_config()

            if is_setup_mode():
                log(config)

            if data.control == config['trackdown'] and config['current_channel'] != 1 and not config['setup_trackdown']:
                config['current_channel'] -= 0.5
            elif data.control == config['trackup'] and not config['setup_trackup']:
                config['current_channel'] += 0.5
            elif data.control in config['excluded']:
                data.channel = int(1)
                destination_port.send(data)
                log(f"Received: {data}")

            elif data.control != config['trackdown'] and data.control != config['trackup'] and not is_setup_mode():
                data.channel = int(config['current_channel'])
                log(f"Received: {data}")
                destination_port.send(data)  # Forward received MIDI message


    except KeyboardInterrupt:
        pass
    finally:
        source_port.close()
        destination_port.close()
        exit()


def is_setup_mode():
    if config['setup_trackup'] or config['setup_trackdown'] or config['set_exclude']:
        return True


# Create a tkinter window


# Create a label to display the current channel value


# Create threads for GUI update and MIDI handling
gui_thread = threading.Thread(target=update_channel_display)
#midi_thread = threading.Thread(target=handle_midi_messages)

# Start both threads
gui_thread.start()
#midi_thread.start()

# Start the tkinter main loop
root.mainloop()
root.resizable(False, False)
configloader.save_config()
