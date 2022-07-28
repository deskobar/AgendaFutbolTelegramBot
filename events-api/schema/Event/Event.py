import strawberry


@strawberry.type
class Event:
    date: str
    match: str
    tournament: str
    hour: str
    channel: str

    @staticmethod
    def from_entry(entry):
        return Event(
            date=entry['FECHA'],
            match=entry['PARTIDO'],
            tournament=entry['COMPETENCIA'],
            hour=entry['HORARIO'],
            channel=entry['CANAL']
        )
