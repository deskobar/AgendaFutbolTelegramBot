from answers import HOW_TO_USAGE


def start(update, context):
    """
    Send a message when the command /start is issued.
    """
    update.message.reply_text(HOW_TO_USAGE)
