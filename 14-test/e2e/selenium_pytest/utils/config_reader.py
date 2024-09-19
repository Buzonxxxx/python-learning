import configparser
import os

def get_config():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'config.ini')
    config.read(config_path)
    return config