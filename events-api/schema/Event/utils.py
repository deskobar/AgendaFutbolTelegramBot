from os.path import exists
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup
from settings import URL
from thefuzz import fuzz

from utils import parse_day_to_date, get_current_datetime


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
    Filter the rows of a Pandas Dataframe where some attributes contain the substring given
    :param df: The Pandas Dataframe to filter
    :param txt: The substring to search
    :return: A Pandas Dataframe where each rows contain the substring given.
    """
    df_cpy = df.copy()
    df_cpy['Score'] = df_cpy.apply(lambda entry: calculate_score(entry, txt), axis=1)
    df_cpy.sort_values('Score', ascending=False, inplace=True)
    df_approximate = get_approximate_matches(df_cpy)
    df_substring = get_matches_are_substring(df_cpy, txt)
    matches = pd.concat([df_approximate, df_substring])
    return matches


def get_matches_are_substring(df, txt):

    return df[df['PARTIDO'].str.contains(txt, case=False) |
              df['COMPETENCIA'].str.contains(txt, case=False) |
              df['CANAL'].str.contains(txt, case=False)]


def get_approximate_matches(df, threshold=50):
    return df[df['Score'] >= threshold]


def calculate_score(row, txt):
    fields_and_weight = [{'field': 'PARTIDO', 'weight': 1},
                         {'field': 'COMPETENCIA', 'weight': 0},
                         {'field': 'CANAL', 'weight': 0}]
    scores = [fuzz.token_sort_ratio(txt, row[entry['field']]) * entry['weight'] for entry in fields_and_weight]
    return sum(scores)
