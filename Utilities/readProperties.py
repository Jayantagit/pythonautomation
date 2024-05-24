import configparser
import os

config=configparser.RawConfigParser()
print(os.getcwd())
config.read(os.path.dirname(os.getcwd())+"\\OpenCartFramework\\Configurations\\config.ini")

class ConfigReader:

    @staticmethod
    def readConfig(key):
        return config.get("commoninfo",key)

