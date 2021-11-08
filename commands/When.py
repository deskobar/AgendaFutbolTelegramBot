from answers import WHEN_WITHOUT_ARGS, WHEN_WITH_NO_COINCIDENCES
from queries import filter_events_using_substring
from scrap import get_events_df
from utils import send_img_or_msg_if_no_content


def when(update, context):
    """
    Given all the events that contains a substring given in their columns
    """
    if len(context.args) != 1:
        update.message.reply_text(WHEN_WITHOUT_ARGS)
    else:
        substring = context.args[0]
        matches = get_events_df()
        matches_filtered = filter_events_using_substring(matches, substring)
        send_img_or_msg_if_no_content(update, matches_filtered, WHEN_WITH_NO_COINCIDENCES, substring)
