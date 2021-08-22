from datetime import datetime, date

import pytz


def get_current_datetime():
    """
    Get the current datetime for America/Santiago
    :return: An datetime.Datetime object
    """
    tz = pytz.timezone('America/Santiago')
    dt = datetime.now(tz)
    return dt


def parse_day_to_date(day):
    """
    Parse an string day to datetime.Date
    :param day: An int that's represent a day
    :return: A datetime.Date object with the day parsed inside.
    """
    local_dt = get_current_datetime()
    current_day, current_month, current_year = local_dt.day, local_dt.month, local_dt.year
    if day >= current_day:
        year, month = current_year, current_month
    elif day < current_day and current_month == 12:
        year, month = current_year + 1, 1
    else:
        year, month = current_year, current_month + 1
    return date(year=year, month=month, day=day)
