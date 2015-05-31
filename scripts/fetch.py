import os
import math
import json

from pprint import pprint
from datetime import date, datetime
from pydnz import Dnz

dnz_api = Dnz(os.environ.get('DNZ_KEY'))

YEAR_INTERVAL = 10
TODAY = date.today()
PAST_YEAR = TODAY.year - YEAR_INTERVAL


def request_dnz_records(timespan, page):
    parameters = {
        '_and': {
            'category': ['Images'],
            'year': [timespan]
        },
        'per_page': 100,
        'page': page,
        'fields': [
            'id',
            'date'
        ]
    }

    return dnz_api.search('', **parameters)


def format_timespan(year1, year2):
    return '{y1}+TO+{y2}'.format(y1=year1, y2=year2)


def fetch_timespan(timespan):

    first_result = request_dnz_records(timespan, 1)
    store_records(first_result.records)

    print('Fetching ' + timespan + ':')
    print(str(first_result.result_count) + ' entries')

    iterations = math.ceil(first_result.result_count / 100)
    # iterations = 5

    # Subsequent requests.
    for i in range(2, iterations + 1):
        records = request_dnz_records(timespan, i).records
        store_records(records)
        pprint(len(results))


def store_record(record):
    for date_str in record['date']:
        date_str = date_str[:10]
        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        if date.year >= PAST_YEAR and date.year <= TODAY.year:
            results[date_str] = record['id']


def store_records(records):
    for record in records:
        store_record(record)

if __name__ == '__main__':
    results = {}

    years = [y for y in range(PAST_YEAR, TODAY.year)]
    timespans = [format_timespan(y, y + 1) for y in years]

    for timespan in timespans:
        fetch_timespan(timespan)

    with open('dnz-records.json', 'w') as outfile:
        json.dump(results, outfile)
