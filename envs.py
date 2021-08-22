import os

from dotenv import load_dotenv

load_dotenv()

# Token for Telegram API
TOKEN = os.getenv('TOKEN')
# Chrome Path for dataframe_image library
CHROME_PATH = os.getenv('CHROME_PATH')
