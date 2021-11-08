from answers import DATE_WITH_NO_COINCIDENCES
from queries import get_events_today
from scrap import get_events_df
from utils import send_img_or_msg_if_no_content


def today(update, context):
    """
    Send all the events of the current day
    """
    matches = get_events_df()
    matches_today = get_events_today(matches)
    send_img_or_msg_if_no_content(update, matches_today, DATE_WITH_NO_COINCIDENCES, 'hoy')
