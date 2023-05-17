import pandas as pd
from commands.queries import events
from graphql_client import client

from answers import ALL_WITH_NO_COINCIDENCES
from utils import send_img_or_msg_if_no_content


def all(update, context):
    """
    Return all the events available
    """
    result = client.execute(events)
    events_result = result['events']
    events_df = pd.DataFrame(events_result)
    send_img_or_msg_if_no_content(update, events_df, ALL_WITH_NO_COINCIDENCES, 'uwu')
