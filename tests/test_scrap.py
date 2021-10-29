import datetime
import unittest
from unittest import mock
from unittest.mock import patch

import pandas as pd

from scrap import get_events_df


class TestScrap(unittest.TestCase):
    def setUp(self):
        events_dict = {
            'FECHA': [datetime.date(year=2021, month=1, day=1)] * 3,
            'PARTIDO': ['bullita vs colo', 'bullita vs cato', 'bullita vs bullita b'],
            'CANAL': ['cedefe', 'tenete', 'iespien'],
            'COMPETENCIA': ['torneo local A', 'torneo local B', 'torneo local C']
        }
        self.events_df = pd.DataFrame(events_dict)

    @patch('scrap.get_current_datetime')
    @patch('scrap.pd')
    @patch('scrap.get_html_text')
    @patch('scrap.process_df_using_html')
    @patch.object(pd.DataFrame, 'to_pickle')
    def test_get_events_df(self, mock_pickle, mock_process, mock_html, mock_pd, mock_datetime):
        today = datetime.datetime(year=1969, month=1, day=1)
        mock_datetime.return_value = today
        mock_html.return_value = '<body></body>'
        mock_pd.read_html.return_value = [self.events_df]
        mock_process.return_value = self.events_df
        mock_pickle.return_value = None
        events = get_events_df()
        for col in self.events_df.columns:
            self.assertListEqual(events[col].to_list(), self.events_df[col].to_list())
        self.assertListEqual(mock_pickle.mock_calls,
                             [mock.call('media/1969-01-01.pkl')])
        self.assertListEqual(mock_process.mock_calls,
                             [mock.call(self.events_df, '<body></body>')])
        self.assertListEqual(mock_html.mock_calls,
                             [mock.call()])
        self.assertListEqual(mock_pd.mock_calls,
                             [mock.call.read_html('<body></body>')])
        self.assertListEqual(mock_datetime.mock_calls,
                             [mock.call()])
