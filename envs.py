import os

from dotenv import load_dotenv

load_dotenv()

# Token for Telegram API
TOKEN = os.getenv('TOKEN')
# URL to scrap
URL = os.getenv('URL')
# Temporal dataframe path
TEMPORAL_DATAFRAME_PATH = os.getenv('TEMPORAL_DATAFRAME_PATH')
