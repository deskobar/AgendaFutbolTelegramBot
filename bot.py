import logging
from datetime import datetime

from telegram.ext import Updater, CommandHandler

from answers import HOW_TO_USAGE, DATE_WITHOUT_ARGS, DATE_WITH_NO_COINCIDENCES, WHEN_WITHOUT_ARGS, \
    WHEN_WITH_NO_COINCIDENCES, ALL_WITH_NO_COINCIDENCES
from envs import TOKEN
from queries import get_events_today, get_events_per_date, filter_events_using_substring
from scrap import get_events_df
from utils import send_img_or_msg_if_no_content

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update, context):
    """
    Send a message when the command /start is issued.
    """
    update.message.reply_text(HOW_TO_USAGE)


def help_command(update, context):
    """
    Send a message when the command /help is issued.
    """
    update.message.reply_text(HOW_TO_USAGE)


def hoy(update, context):
    """
    Send all the events of the current day
    """
    matches = get_events_df()
    matches_today = get_events_today(matches)
    send_img_or_msg_if_no_content(update, matches_today, DATE_WITH_NO_COINCIDENCES, 'hoy')


def fecha(update, context):
    """
    Send all the events for a given string date
    """
    if len(context.args) != 1:
        update.message.reply_text(DATE_WITHOUT_ARGS)
    else:
        date = context.args[0]
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        matches = get_events_df()
        matches_these_day = get_events_per_date(matches, date_obj)
        send_img_or_msg_if_no_content(update, matches_these_day, DATE_WITH_NO_COINCIDENCES, date)


def cuando(update, context):
    """
    Given all the events that contains a substring given in their columns
    """
    if len(context.args) != 1:
        update.message.reply_text(WHEN_WITHOUT_ARGS)
    else:
        substring = context.args[0]
        matches = get_events_df()
        matches_filtered = filter_events_using_substring(matches, substring)
        send_img_or_msg_if_no_content(update, matches_filtered, WHEN_WITH_NO_COINCIDENCES, substring)


def todo(update, context):
    """
    Return all the events available
    """
    matches = get_events_df()
    send_img_or_msg_if_no_content(update, matches, ALL_WITH_NO_COINCIDENCES, 'uwu')


def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("hoy", hoy))
    dispatcher.add_handler(CommandHandler("cuando", cuando))
    dispatcher.add_handler(CommandHandler("fecha", fecha))
    dispatcher.add_handler(CommandHandler("todo", fecha))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
