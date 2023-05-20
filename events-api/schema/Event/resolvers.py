import typing
from datetime import datetime

from constants import LOW_THRESHOLD, DECENT_THRESHOLD
from schema.Event.Event import Event
from schema.Event.utils import (
    get_events_df,
    get_events_df_per_date,
    filter_events_using_substring,
    may_get_team_name_from_user_and_alias,
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
    team_name = await may_get_team_name_from_user_and_alias(user_id, text)
    filter_by = team_name if team_name else text
    threshold = DECENT_THRESHOLD if team_name else LOW_THRESHOLD
    events_filtered_df = filter_events_using_substring(
        df, filter_by, threshold=threshold
    )
    events = events_filtered_df.to_dict("records")
    return [Event.from_entry(event) for event in events]
