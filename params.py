import configparser
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.ini")

config = configparser.ConfigParser()
if os.path.exists(CONFIG_PATH):
    config.read(CONFIG_PATH)
else:
    raise FileNotFoundError("Configuration file not found")

PARAM1 = config.get("DEFAULT", "PARAM1")
