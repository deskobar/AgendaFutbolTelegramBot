import typing

import strawberry
from strawberry.fastapi import GraphQLRouter

from schema.Event.Event import Event
from schema.Event.resolvers import get_events, get_events_per_date, get_events_match_text


@strawberry.type
class Query:
    events: typing.List[Event] = strawberry.field(resolver=get_events)
    events_per_date: typing.List[Event] = strawberry.field(resolver=get_events_per_date)
    events_match_text: typing.List[Event] = strawberry.field(resolver=get_events_match_text)


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)
