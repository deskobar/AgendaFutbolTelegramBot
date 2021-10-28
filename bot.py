import logging

import dataframe_image as dfi
from telegram.ext import Updater, CommandHandler

from answers import HOW_TO_USAGE, DATE_WITHOUT_ARGS, DATE_WITH_NO_COINCIDENCES, WHEN_WITHOUT_ARGS, \
    WHEN_WITH_NO_COINCIDENCES
from envs import TOKEN, TEMPORAL_DATAFRAME_PATH
from queries import get_events_today, get_events_per_date, filter_events_using_substring
from scrap import get_events_df

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
    dfi.export(matches_today, TEMPORAL_DATAFRAME_PATH, table_conversion=None)
    img = open(TEMPORAL_DATAFRAME_PATH, 'rb')
    update.message.bot.send_photo(update.message.chat.id, img)
    img.close()


def fecha(update, context):
    """
    Send all the events for a given string date
    """
    if len(context.args) != 1:
        update.message.reply_text(DATE_WITHOUT_ARGS)
    date = context.args[0]
    matches = get_events_df()
    matches_these_day = get_events_per_date(matches, date)
    if not matches_these_day.index.empty:
        dfi.export(matches_these_day, TEMPORAL_DATAFRAME_PATH, table_conversion=None)
        img = open(TEMPORAL_DATAFRAME_PATH, 'rb')
        update.message.bot.send_photo(update.message.chat.id, img)
        img.close()
    else:
        update.message.reply_text(DATE_WITH_NO_COINCIDENCES.format(date))


def cuando(update, context):
    """
    Given all the events that contains a substring given in their columns
    """
    if len(context.args) != 1:
        update.message.reply_text(WHEN_WITHOUT_ARGS)
    substring = context.args[0]
    matches = get_events_df()
    matches_filtered = filter_events_using_substring(matches, substring)
    if not matches_filtered.index.empty:
        dfi.export(matches_filtered, TEMPORAL_DATAFRAME_PATH, table_conversion=None)
        img = open(TEMPORAL_DATAFRAME_PATH, 'rb')
        update.message.bot.send_photo(update.message.chat.id, img)
        img.close()
    else:
        update.message.reply_text(WHEN_WITH_NO_COINCIDENCES.format(substring))


def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("hoy", hoy))
    dispatcher.add_handler(CommandHandler("cuando", cuando))
    dispatcher.add_handler(CommandHandler("fecha", fecha))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
