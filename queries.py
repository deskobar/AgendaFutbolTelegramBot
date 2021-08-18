from utils import get_current_datetime


def get_matches_today(df):
    locale_dt = get_current_datetime()
    current_date = locale_dt.date()
    df_filtered = df.loc[df.FECHA == current_date]
    return df_filtered
