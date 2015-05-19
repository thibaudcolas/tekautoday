# -*- coding: utf-8 -*-

from os import environ
from datetime import date
from requests import get
from calendar import Calendar

import records

DNZ_URL = 'http://api.digitalnz.org/v3/records/'
DNZ_KEY = environ.get('DNZ_KEY')


def get_metadata(record):
    """
    Calls DNZ's API to retrieve the metadata for a given record.
    """

    id = record['id']

    url = DNZ_URL + '{id}.json?api_key={key}'.format(id=id, key=DNZ_KEY)

    metadata = get(url).json()['record']
    metadata['hash'] = record['hash']

    return metadata


def get_calendar():
    """
    Generates a calendar structure for the current month.
    """

    year = date.today().year
    month = date.today().month

    return Calendar(0).monthdatescalendar(year, month)


def update_record_cache(cache={}):
    """
    Fills the cache with values for the record of the day if necessary.
    """

    today = date.today()

    if ('day' not in cache) or (today != cache['day']):
        print('Invalidating cache for ' + str(today))

        cache['day'] = today
        cache['record'] = records.records_date[str(cache['day'])]
        cache['metadata'] = get_metadata(cache['record'])

    return cache
