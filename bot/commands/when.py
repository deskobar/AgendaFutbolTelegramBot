import pandas as pd
from commands.queries import events_substring
from graphql_client import client

from answers import WHEN_WITHOUT_ARGS, WHEN_WITH_NO_COINCIDENCES
from utils import send_img_or_msg_if_no_content


def when(update, context):
    """
    Given all the events that contains a substring given in their columns
    """
    if len(context.args) != 1:
        update.message.reply_text(WHEN_WITHOUT_ARGS)
    else:
        substring = context.args[0]
        result = client.execute(events_substring, variable_values={"text": substring})
        events_result = result['eventsMatchText']
        events_df = pd.DataFrame(events_result)
        send_img_or_msg_if_no_content(update, events_df, WHEN_WITH_NO_COINCIDENCES, substring)
