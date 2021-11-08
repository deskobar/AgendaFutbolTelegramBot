from datetime import datetime

from answers import DATE_WITHOUT_ARGS, DATE_WITH_NO_COINCIDENCES
from queries import get_events_per_date
from scrap import get_events_df
from utils import send_img_or_msg_if_no_content


def date(update, context):
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
