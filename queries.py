from datetime import datetime

from utils import get_current_datetime


def get_matches_per_date(df, date):
    if type(date) is str:
        date = datetime.strptime(date, '%Y-%m-%d').date()
    df_filtered = df.loc[df.FECHA == date]
    return df_filtered


def get_matches_today(df):
    locale_dt = get_current_datetime()
    current_date = locale_dt.date()
    df_filtered = get_matches_per_date(df, current_date)
    return df_filtered
