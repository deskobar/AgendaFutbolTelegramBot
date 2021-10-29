from utils import get_current_datetime


def get_events_per_date(df, date):
    """
    Get a Pandas Dataframe where each row has as date the date given
    :param df: The Pandas Dataframe to filter
    :param date: A Datetime.Date to filter
    :return: A Pandas Dataframe filtered by the date
    """
    df_filtered = df[df['FECHA'] == date]
    return df_filtered


def get_events_today(df):
    """
    Get the matches for the current Day
    :param df: The Pandas Dataframe to filter the info.
    :return: A Pandas Dataframe for the current day
    """
    locale_dt = get_current_datetime()
    current_date = locale_dt.date()
    df_filtered = get_events_per_date(df, current_date)
    return df_filtered


def filter_events_using_substring(df, txt):
    """
    Filter the rows of a Pandas Dataframe where some attributes contains the substring given
    :param df: The Pandas Dataframe to filter
    :param txt: The substring to search
    :return: A Pandas Dataframe where each rows contains the substring given.
    """
    return df[df['PARTIDO'].str.contains(txt, case=False) |
              df['COMPETENCIA'].str.contains(txt, case=False) |
              df['CANAL'].str.contains(txt, case=False)]
