from answers import HOW_TO_USAGE


def help(update, context):
    """
    Send a message when the command /help is issued.
    """
    update.message.reply_text(HOW_TO_USAGE)
