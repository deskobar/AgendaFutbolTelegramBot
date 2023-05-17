from gql import gql

events = gql("""
    query events {
        events {
            date
            match
            tournament
            hour
            channel
        }
    }
""")

events_per_date = gql("""
    query events($date: String!) {
        eventsPerDate(date: $date) {
            date
            match
            tournament
            hour
            channel
        }
    }
""")

events_substring = gql("""
    query events($text: String!, $userId: String!) {
        eventsMatchText(text: $text, userId: $userId) {
            date
            match
            tournament
            hour
            channel
        }
    }
""")

set_alias = gql("""
    mutation setAlias($userId: String!, $teamName: String!, $alias: String!) {
        setAlias(userId: $userId, teamName: $teamName, alias: $alias)
    }
""")
