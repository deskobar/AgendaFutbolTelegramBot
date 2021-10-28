import pandas as pd
import requests
from bs4 import BeautifulSoup

from envs import URL
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
    Get the channels of each event from a HTML as plain text
    :param html_text: The HTML as plain text
    :return: A List of string, where each belows to a Channel.
    """
    soup = BeautifulSoup(html_text, 'html.parser')
    channels_elements = soup.findAll('img', class_='di-tv-channel-thumb', alt=True)
    channels = [channel['alt'] for channel in channels_elements]
    return channels


def get_events_df():
    """
    Get a Pandas Dataframe with all the events available in the target WebSite.
    :return: A Pandas Dataframe.
    """
    current_date = get_current_datetime().date()
    df_filename = f'media/{current_date}.pkl'
    try:
        df = pd.read_pickle(df_filename)
        return df
    except Exception as e:
        print(e)
        html = get_html_text()
        df = pd.read_html(html)[0]
        df.drop(['PARTIDO.1', 'PARTIDO.2', 'PARTIDO.3'], axis=1, inplace=True)
        channels = get_channels(html)
        df['FECHA'] = df['FECHA'].map(lambda fecha: parse_day_to_date(int(fecha[-2:])))
        df['CANAL'] = channels
        # Saving the Pandas Dataframe in order to avoid unnecessary queries over the Website.
        df.to_pickle(df_filename)
        return df
