import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHROME_PATH = os.getenv('CHROME_PATH')