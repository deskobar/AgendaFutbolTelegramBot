import logging

from telegram.ext import Updater, CommandHandler

from commands import (all, date, help, start, today, when, version, set_alias)
from settings import TELEGRAM_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

command_handlers = [
    {"command": "start", "function": start},
    {"command": "help", "function": help},
    {"command": "hoy", "function": today},
    {"command": "cuando", "function": when},
    {"command": "fecha", "function": date},
    {"command": "todo", "function": all},
    {"command": "version", "function": version},
    {"command": "set_alias", "function": set_alias},
]


def main():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    for handler in command_handlers:
        dispatcher.add_handler(CommandHandler(handler["command"], handler["function"]))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
