from answers import ALL_WITH_NO_COINCIDENCES
from scrap import get_events_df
from utils import send_img_or_msg_if_no_content


def all(update, context):
    """
    Return all the events available
    """
    matches = get_events_df()
    send_img_or_msg_if_no_content(update, matches, ALL_WITH_NO_COINCIDENCES, 'uwu')
