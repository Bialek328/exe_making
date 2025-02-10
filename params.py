import configparser

config = configparser.ConfigParser()
try:
    config.read("config.ini")

except FileNotFoundError as e:
    print("no config file found")


PARAM1 = config.get("DEFAULT", "PARAM1")
