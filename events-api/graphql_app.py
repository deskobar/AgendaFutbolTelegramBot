import typing

import strawberry
from strawberry.fastapi import GraphQLRouter

from schema import (
    Event,
    get_events,
    get_events_per_date,
    get_events_match_text,
    get_alias,
    set_alias,
)


@strawberry.type
class Query:
    events: typing.List[Event] = strawberry.field(resolver=get_events)
    events_per_date: typing.List[Event] = strawberry.field(resolver=get_events_per_date)
    events_match_text: typing.List[Event] = strawberry.field(
        resolver=get_events_match_text
    )
    get_alias: str = strawberry.field(resolver=get_alias)


@strawberry.type
class Mutation:
    set_alias: str = strawberry.field(resolver=set_alias)


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)
