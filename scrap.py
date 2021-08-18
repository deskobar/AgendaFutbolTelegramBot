import requests
import pandas as pd
from bs4 import BeautifulSoup

from utils import parse_day_to_date


def get_html_text():
    url = 'https://agenda.redgol.cl/tv/schedule/agenda-principal/'
    r = requests.get(url)
    return r.text


def get_channels(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    channels_elements = soup.findAll('img', class_='di-tv-channel-thumb', alt=True)
    channels = [channel['alt'] for channel in channels_elements]
    return channels


def get_matches_df():
    html = get_html_text()
    df = pd.read_html(html)[0]
    df.drop(['PARTIDO.1', 'PARTIDO.2', 'PARTIDO.3'], axis=1, inplace=True)
    channels = get_channels(html)
    df['FECHA'] = df['FECHA'].map(lambda fecha: parse_day_to_date(int(fecha[-2:])))
    df['CANAL'] = channels
    return df
