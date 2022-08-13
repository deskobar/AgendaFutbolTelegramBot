import logging

from telegram.ext import Updater, CommandHandler

from commands import (all, date, help, start, today, when)
from settings import TELEGRAM_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("hoy", today))
    dispatcher.add_handler(CommandHandler("cuando", when))
    dispatcher.add_handler(CommandHandler("fecha", date))
    dispatcher.add_handler(CommandHandler("todo", all))
    dispatcher.add_handler(CommandHandler("version", version))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
