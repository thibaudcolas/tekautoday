# -*- coding: utf-8 -*-

import json
from hashlib import md5
from datetime import datetime

# Hash tables that store the records.
records_date = {}
records_hash = {}


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


def load_records():
    """
    Loads records into two hash tables.
    """

    json_records = json.loads(open('data/records-2015.json').read())['records']

    for record in json_records:
        record = parse_record(record)

        records_date[record['date_current_year']] = record
        records_hash[record['hash']] = record

load_records()
