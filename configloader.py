import json

import variables
from developer_func import log
from variables import config


def save_config():
    try:
        with open('config.json', "w") as f:
            tempconfig = config.copy()
            tempconfig['setup_trackdown'] = False
            tempconfig['setup_trackup'] = False
            tempconfig['set_exclude'] = False
            tempconfig['set_exclude'] = config['current_channel']
            tempconfig['current_warning'] = ""

            f.write(json.dumps(tempconfig))

    except Exception:
        log("Error loading the File")


def load_config():
    try:
        with open('config.json', "r") as f:
            config = json.load(f)

        return config

    except FileNotFoundError as e:
        with open('config.json', "w") as f:
            log("Config error")
            f.write(json.dumps(variables.config))

        return variables.config
