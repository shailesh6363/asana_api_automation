import configparser
from pathlib import Path



cfgFile=('asanaqaenv.ini')
cfgFileDir=('config')

config=configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE=BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFile)

config.read(CONFIG_FILE)


def get_token():
    return config['general']['token']


print(get_token())