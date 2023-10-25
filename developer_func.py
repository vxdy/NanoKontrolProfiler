import os
from dotenv import load_dotenv

load_dotenv()

DEVELOPER_MODE = os.getenv("DEVELOPER_MODE", 'False').lower() in ('true', '1', 't')


def log(output):
    if DEVELOPER_MODE:
        print(output)
