from os.path import exists

import pandas as pd
import requests
from bs4 import BeautifulSoup
from settings import URL

from utils import parse_day_to_date, get_current_datetime
from pathlib import Path


def get_html_text():
    """
    Get the HTML content as plain text
    :return: A string html
    """
    r = requests.get(URL)
    return r.text


def get_channels(html_text):
    """
    Get the channels of each event from an HTML as plain text
    :param html_text: The HTML as plain text
    :return: A List of string, where each belows to a Channel.
    """
    soup = BeautifulSoup(html_text, 'html.parser')
    channels_elements = soup.findAll('img', class_='di-tv-channel-thumb', alt=True)
    channels = [channel['alt'] for channel in channels_elements]
    return channels


def process_df_using_html(df, html):
    """
    Drop unused columns from a dataframe
    :param df: A Pandas DataFrame
    :param html: A HTML body
    :return: A Pandas DataFrame
    """
    df_cpy = df.copy()
    df_cpy = df_cpy.drop(['PARTIDO.1', 'PARTIDO.2', 'PARTIDO.3'], axis=1)
    channels = get_channels(html)
    df_cpy['FECHA'] = df_cpy['FECHA'].map(lambda fecha: parse_day_to_date(int(fecha[-2:])))
    df_cpy['CANAL'] = channels
    return df_cpy


def get_events_df():
    """
    Get a Pandas Dataframe with all the events available in the target WebSite.
    :return: A Pandas Dataframe.
    """
    current_date = get_current_datetime().date()
    df_base_path = Path('media')
    df_base_path.mkdir(exist_ok=True)
    df_path = df_base_path / f'{current_date}.pkl'

    if not exists(df_path):
        html = get_html_text()
        raw_df = pd.read_html(html)[0]
        df = process_df_using_html(raw_df, html)
        # Saving the Dataframe to avoid unnecessary requests over the Website.
        df.to_pickle(df_path)
        return df
    else:
        df = pd.read_pickle(df_path)
        return df


def get_events_df_per_date(df, date):
    """
    Get a Pandas Dataframe where each row has as date the date given
    :param df: The Pandas Dataframe to filter
    :param date: A Datetime.Date to filter
    :return: A Pandas Dataframe filtered by the date
    """
    df_filtered = df[df['FECHA'] == date]
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
