import os
from dotenv import load_dotenv
from os.path import join, dirname


def env(key, default=None):
    # set the .env path
    dotenv_path = join(dirname(__file__), '.env')
    # load variables
    load_dotenv(dotenv_path)
    return os.getenv(key, default)
