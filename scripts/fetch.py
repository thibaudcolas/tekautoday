import os
# import math
import json

from pprint import pprint
from datetime import date
from scripts.pydnz import Dnz

dnz_api = Dnz(os.environ.get('DNZ_KEY'))
YEAR_INTERVAL = 10


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
    pprint('Fetching ' + timespan)

    first_result = request_dnz_records(timespan, 1)
    store_results(first_result.records)

    pprint(first_result.result_count)

    # iterations = math.ceil(first_result.result_count / 100)
    iterations = 1

    # Subsequent requests.
    for i in range(2, iterations + 1):
        records = request_dnz_records(i).records
        store_results(records)
        pprint(len(results))


def store_results(records):
    for record in records:
        results.append({
            'id': record['id'],
            'date': record['date']
        })

if __name__ == '__main__':
    results = []

    present = date.today().year
    past = present - YEAR_INTERVAL
    years = [y for y in range(2005, 2006)]
    timespans = [format_timespan(y, y + 1) for y in years]

    for timespan in timespans:
        fetch_timespan(timespan)

    with open('dnz-records.json', 'w') as outfile:
        json.dump(results, outfile)
