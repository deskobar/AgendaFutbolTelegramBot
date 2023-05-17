import typing
from datetime import datetime

from schema.Event.Event import Event
from schema.Event.utils import (get_events_df, get_events_df_per_date,
                                filter_events_using_substring)
from schema.Alias.resolvers import aliases


async def get_events() -> typing.List[Event]:
    df = get_events_df()
    events = df.to_dict('records')
    return [Event.from_entry(event) for event in events]


async def get_events_per_date(date: str) -> typing.List[Event]:
    df = get_events_df()
    date_object = datetime.strptime(date, '%Y-%m-%d').date()
    events_df = get_events_df_per_date(df, date_object)
    events = events_df.to_dict('records')
    return [Event.from_entry(event) for event in events]


async def get_events_match_text(user_id: str, text: str) -> typing.List[Event]:
    df = get_events_df()
    team_name_by_alias = aliases.get(user_id, {}).get(text)
    filter_by = team_name_by_alias if team_name_by_alias else text
    events_filtered_df = filter_events_using_substring(df, filter_by)
    events = events_filtered_df.to_dict('records')
    return [Event.from_entry(event) for event in events]
