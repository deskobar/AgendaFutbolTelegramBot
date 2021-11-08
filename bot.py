import logging

from telegram.ext import Updater, CommandHandler

from commands.All import all
from commands.Date import date
from commands.Help import help
from commands.Start import start
from commands.Today import today
from commands.When import when
from envs import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("hoy", today))
    dispatcher.add_handler(CommandHandler("cuando", when))
    dispatcher.add_handler(CommandHandler("fecha", date))
    dispatcher.add_handler(CommandHandler("todo", all))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
