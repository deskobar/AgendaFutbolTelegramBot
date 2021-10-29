import datetime
import unittest
from unittest.mock import patch

from utils import get_current_datetime, parse_day_to_date


class TestUtils(unittest.TestCase):

    def test_get_correct_datetime(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        locale_datetime = get_current_datetime()
        delta = now - locale_datetime
        delta_hours = delta.seconds // 60
        self.assertGreaterEqual(delta_hours, 3)

    @patch('utils.get_current_datetime')
    def test_parse_correct_date(self, mock_datetime):
        initial_date = datetime.datetime(year=2020, month=12, day=31)
        mock_datetime.return_value = initial_date
        parsed_date = parse_day_to_date(1)
        self.assertEqual(parsed_date.day, 1)
        self.assertEqual(parsed_date.month, 1)
        self.assertEqual(parsed_date.year, 2021)
