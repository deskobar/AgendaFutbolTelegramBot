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
    query events($text: String!) {
        eventsMatchText(text: $text) {
            date
            match
            tournament
            hour
            channel
        }
    }
""")
