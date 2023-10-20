from math import ceil
import mido
import tkinter as tk
import threading
import json

from gui import MainView
from variables import *

from developer_func import *

# Specify the updated names of the source and destination MIDI ports
source_port_name = "nanoKONTROL2"
destination_port_name = "pymid"

output = mido.open_output()

try:
    # Find exakt Midi Names
    korg_port_name = [s for s in mido.get_input_names() if source_port_name in s][0]
    virtual_port_name = [g for g in mido.get_output_names() if destination_port_name in g][0]
except IndexError:
    log("Device not found")
    exit(500)

root = tk.Tk()
root.title("MIDI Channel Display")
root.attributes('-topmost', True)

main = MainView(root)
main.pack(side="top", fill="both", expand=True)


def load_config():
    try:
        with open('config.json') as f:
            d = json.load(f)
            print(d)
    except FileNotFoundError as e:
        log(e)


load_config()


# Function to update the channel display in the tkinter GUI
def update_channel_display():

    if test_mode:
        root.geometry("{}x{}".format(200, 500))

    while True:
        main.mainpage.channel_label.config(text=str(ceil(config['current_channel'])))
        if test_mode:
            main.mainpage.trackdown_lable.config(text=str(ceil(config['trackdown'])))
            main.mainpage.trackup_lable.config(text=str(ceil(config['trackup'])))
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

            if config['setup_trackup']:
                config['trackup'] = data.control
                config['setup_trackup'] = False

            if set_exclude:
                trackdown = data.control

            if is_setup_mode():
                continue

            if data.control == config['trackdown'] and config['current_channel'] != 1 and not setup_trackdown:
                config['current_channel'] -= 0.5
            elif data.control == config['trackup'] and not setup_trackup:
                config['current_channel'] += 0.5
            elif data.control != config['trackdown'] and data.control != config['trackup']:
                data.channel = int(config['current_channel'])
                print(f"Received: {data}")
                destination_port.send(data)  # Forward received MIDI message

    except KeyboardInterrupt:
        pass
    finally:
        source_port.close()
        destination_port.close()
        exit()



def is_setup_mode():
    if setup_trackup or setup_trackdown or set_exclude:
        return True


# Create a tkinter window


# Create a label to display the current channel value


# Create threads for GUI update and MIDI handling
gui_thread = threading.Thread(target=update_channel_display)
midi_thread = threading.Thread(target=handle_midi_messages)

# Start both threads
gui_thread.start()
midi_thread.start()

# Start the tkinter main loop
root.mainloop()
