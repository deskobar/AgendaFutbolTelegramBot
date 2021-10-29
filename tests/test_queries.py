import datetime
import unittest
from unittest.mock import patch

import pandas as pd

from queries import get_events_per_date, get_events_today, filter_events_using_substring


class TestQueries(unittest.TestCase):
    def setUp(self):
        events_dict = {
            'FECHA': [datetime.date(year=2021, month=1, day=1)] * 3,
            'PARTIDO': ['bullita vs colo', 'bullita vs cato', 'bullita vs bullita b'],
            'CANAL': ['cedefe', 'tenete', 'iespien'],
            'COMPETENCIA': ['torneo local A', 'torneo local B', 'torneo local C']
        }
        self.events_df = pd.DataFrame(events_dict)

    def test_get_events_per_date_with_coincidences(self):
        date_to_compare = datetime.date(year=2021, month=1, day=1)
        events_these_day = get_events_per_date(self.events_df, date_to_compare)
        self.assertFalse(events_these_day.index.empty)
        self.assertEqual(len(events_these_day.index), 3)
        self.assertListEqual(events_these_day['FECHA'].to_list(), [date_to_compare] * 3)

    def test_get_events_per_date_without_coincidences(self):
        date_to_compare = datetime.date(year=2021, month=1, day=2)
        events_these_day = get_events_per_date(self.events_df, date_to_compare)
        self.assertTrue(events_these_day.index.empty)
        self.assertEqual(len(events_these_day.index), 0)
        self.assertListEqual(events_these_day['FECHA'].to_list(), [])

    @patch('queries.get_current_datetime')
    def test_get_events_today(self, mock_datetime):
        today = datetime.datetime(year=2021, month=1, day=1)
        mock_datetime.return_value = today
        events_today = get_events_today(self.events_df)
        self.assertFalse(events_today.index.empty)
        self.assertEqual(len(events_today.index), 3)
        self.assertListEqual(events_today['FECHA'].to_list(), [today.date()] * 3)

    def test_filter_events_using_substring_with_coincidences(self):
        txt = 'BULLITA'
        filtered_df = filter_events_using_substring(self.events_df, txt)
        self.assertEqual(len(filtered_df.index), 3)

    def test_filter_events_using_substring_without_coincidences(self):
        txt = 'deskobar'
        filtered_df = filter_events_using_substring(self.events_df, txt)
        self.assertEqual(len(filtered_df.index), 0)
