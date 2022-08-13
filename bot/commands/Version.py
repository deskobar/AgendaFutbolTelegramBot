from answers import VERSION


def version(update, context):
    """
    Send a message when the command /version is issued.
    """
    update.message.reply_text(VERSION)
