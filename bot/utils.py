import dataframe_image as dfi
import io


def send_img_or_msg_if_no_content(update, df, msg, value):
    """
    Send an img of the dataframe content if it has it, an informative msg otherwise
    :param update: A Telegram Bot Updater
    :param df: A Pandas DataFrame
    :param msg: A String
    :param value: A String
    :return: None
    """
    if df.index.empty is False:
        with io.BytesIO() as tmp:
            dfi.export(df, tmp, table_conversion=None, max_rows=-1)
            tmp.seek(0)
            update.message.bot.send_photo(update.message.chat.id, tmp)
    else:
        update.message.reply_text(msg.format(value))
