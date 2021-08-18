from datetime import datetime, date

import pytz


def get_current_datetime():
    tz = pytz.timezone('America/Santiago')
    dt = datetime.now(tz)
    return dt


def parse_day_to_date(day):
    local_dt = get_current_datetime()
    current_day, current_month, current_year = local_dt.day, local_dt.month, local_dt.year
    if day >= current_day:
        year, month = current_year, current_month
    elif day < current_day and current_month == 12:
        year, month = current_year + 1, 1
    else:
        year, month = current_year, current_month + 1
    return date(year=year, month=month, day=day)


def df_to_string(df):
    pass
