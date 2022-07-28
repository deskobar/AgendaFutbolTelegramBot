import pandas as pd
from commands.queries import events_per_date
from graphql_client import client

from answers import DATE_WITHOUT_ARGS, DATE_WITH_NO_COINCIDENCES
from utils import send_img_or_msg_if_no_content


def date(update, context):
    """
    Send all the events for a given string date
    """
    if len(context.args) != 1:
        update.message.reply_text(DATE_WITHOUT_ARGS)
    else:
        date = context.args[0]
        result = client.execute(events_per_date, variable_values={"date": date})
        events_result = result['eventsPerDate']
        events_df = pd.DataFrame(events_result)
        send_img_or_msg_if_no_content(update, events_df, DATE_WITH_NO_COINCIDENCES, date)
