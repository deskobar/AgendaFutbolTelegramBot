import typing
from datetime import datetime

from constants import LOW_THRESHOLD, DECENT_THRESHOLD
from models import Alias
from schema.Event.Event import Event
from schema.Event.utils import (
    get_events_df,
    get_events_df_per_date,
    filter_events_using_substring,
)


async def get_events() -> typing.List[Event]:
    df = get_events_df()
    events = df.to_dict("records")
    return [Event.from_entry(event) for event in events]


async def get_events_per_date(date: str) -> typing.List[Event]:
    df = get_events_df()
    date_object = datetime.strptime(date, "%Y-%m-%d").date()
    events_df = get_events_df_per_date(df, date_object)
    events = events_df.to_dict("records")
    return [Event.from_entry(event) for event in events]


async def get_events_match_text(user_id: str, text: str) -> typing.List[Event]:
    df = get_events_df()
    alias = await Alias.objects.get(user_id=user_id, alias=text)
    team_name_by_alias = alias.team_name
    filter_by = team_name_by_alias if team_name_by_alias else text
    threshold = DECENT_THRESHOLD if team_name_by_alias else LOW_THRESHOLD
    events_filtered_df = filter_events_using_substring(df, filter_by, threshold=threshold)
    events = events_filtered_df.to_dict("records")
    return [Event.from_entry(event) for event in events]
