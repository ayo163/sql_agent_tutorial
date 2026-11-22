
from os import getcwd
from dotenv import load_dotenv


env_path = getcwd() + "/.env"
load_dotenv(env_path)