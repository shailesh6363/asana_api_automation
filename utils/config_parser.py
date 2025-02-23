import configparser
from pathlib import Path
from file_utils import get_test_case_data


cfgFile=('asanaqaenv.ini')
cfgFileDir=('config')

config=configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE=BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFile)

config.read(CONFIG_FILE)


def get_token():
    return config['general']['token']


print(get_token())