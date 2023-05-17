from datetime import datetime

import pandas as pd
import pytz
from commands.queries import events_per_date
from graphql_client import client

from answers import DATE_WITH_NO_COINCIDENCES
from utils import send_img_or_msg_if_no_content


def today(update, context):
    """
    Send all the events of the current day
    """
    date = datetime.now(pytz.timezone('America/Santiago')).strftime('%Y-%m-%d')
    result = client.execute(events_per_date, variable_values={"date": date})
    events_result = result['eventsPerDate']
    events_df = pd.DataFrame(events_result)
    send_img_or_msg_if_no_content(update, events_df, DATE_WITH_NO_COINCIDENCES, 'hoy')
