import logging

import dataframe_image as dfi
from telegram import ForceReply
from telegram.ext import Updater, CommandHandler

from envs import TOKEN, CHROME_PATH
from queries import get_matches_today
from scrap import get_matches_df

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update, context):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def hoy(update, context):
    matches = get_matches_df()
    matches_today = get_matches_today(matches)
    dfi.export(matches_today, 'dataframe.png', chrome_path=CHROME_PATH)
    img = open('dataframe.png', 'rb')
    update.message.bot.send_photo(update.message.chat.id, open('dataframe.png', 'rb'))
    img.close()
    # update.message.reply_text(f'```{matches_today}```', parse_mode='MarkdownV2')


def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("hoy", hoy))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
