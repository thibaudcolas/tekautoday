# -*- coding: utf-8 -*-

from os import environ
from hashlib import md5
from datetime import datetime
from requests import get

DNZ_URL = 'http://api.digitalnz.org/v3/records/'
DNZ_KEY = environ.get('DNZ_KEY')


def parse_record(record):
    """
    Parses a metadata record to make it usable.
    """

    record['hash'] = md5(str(record['id']).encode('utf-8')).hexdigest()
    record['date'] = record['date'][-1][:10]
    date = datetime.strptime(record['date'], '%Y-%m-%d').date()
    current_year = date.year + 10
    record['date_current_year'] = str(date.replace(year=current_year))

    return record


def get_metadata(record):
    """
    Calls DNZ's API to retrieve the metadata for a given record.
    """

    id = record['id']

    url = DNZ_URL + '{id}.json?api_key={key}'.format(id=id, key=DNZ_KEY)

    metadata = get(url).json()['record']
    metadata['hash'] = record['hash']

    return metadata
