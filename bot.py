import logging

import dataframe_image as dfi
from telegram.ext import Updater, CommandHandler

from envs import TOKEN, CHROME_PATH
from queries import get_events_today, get_matches_per_date, filter_matches_substring
from scrap import get_events_df

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update, context):
    """
    Send a message when the command /start is issued.
    """
    txt = """
    Bienvenido! Los comandos con que me puedes llamar son:
    /hoy 
        Entrega los partidos del día (a la hora de Chile)
    /fecha <fecha>
        Entrega los partidos para la fecha dada, debe estar en formato YYYY-MM-DD
    /cuando <palabra>
        Entrega los eventos que contienen la palabra en el nombre del evento, canal o liga.
    """
    update.message.reply_text(txt)


def help_command(update, context):
    """
    Send a message when the command /help is issued.
    """
    txt = """
    Bienvenido! Los comandos con que me puedes llamar son:
    /hoy 
        Entrega los partidos del día (a la hora de Chile)
    /fecha <fecha>
        Entrega los partidos para la fecha dada, debe estar en formato YYYY-MM-DD
    /cuando <palabra>
        Entrega los eventos que contienen la palabra en el nombre del evento, canal o liga.
    """
    update.message.reply_text(txt)


def hoy(update, context):
    """
    Send all the events of the current day
    """
    matches = get_events_df()
    matches_today = get_events_today(matches)
    dfi.export(matches_today, 'dataframe.png', chrome_path=CHROME_PATH)
    img = open('dataframe.png', 'rb')
    update.message.bot.send_photo(update.message.chat.id, open('dataframe.png', 'rb'))
    img.close()


def fecha(update, context):
    """
    Send all the events for a given string date
    """
    if len(context.args) != 1:
        update.message.reply_text(f'Debes enviar /fecha <fecha> en formato YYYY-MM-DD')
    date = context.args[0]
    matches = get_events_df()
    matches_these_day = get_matches_per_date(matches, date)
    if not matches_these_day.index.empty:
        dfi.export(matches_these_day, 'dataframe.png', chrome_path=CHROME_PATH)
        img = open('dataframe.png', 'rb')
        update.message.bot.send_photo(update.message.chat.id, open('dataframe.png', 'rb'))
        img.close()
    else:
        update.message.reply_text(f'No hay eventos agendados aún para {date} unu. Prueba con otra fecha')


def cuando(update, context):
    """
    Given all the events that contains a substring given in their columns
    """
    if len(context.args) != 1:
        update.message.reply_text(f'Debes enviar /cuando <una palabra>')
    substring = context.args[0]
    matches = get_events_df()
    matches_filtered = filter_matches_substring(matches, substring)
    if not matches_filtered.index.empty:
        dfi.export(matches_filtered, 'dataframe.png', chrome_path=CHROME_PATH)
        img = open('dataframe.png', 'rb')
        update.message.bot.send_photo(update.message.chat.id, open('dataframe.png', 'rb'))
        img.close()
    else:
        update.message.reply_text(f'No se encontraron eventos que contengan {substring} unu. Prueba escribiéndolo de '
                                  f'otra forma')


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
