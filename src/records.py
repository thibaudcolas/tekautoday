# -*- coding: utf-8 -*-

import flask
import json

from hashlib import md5

# Hash tables that store the records.
records_date = {}
records_hash = {}


def get_record_by_hash(record_hash):
    try:
        return records_hash[record_hash]
    except KeyError:
        flask.abort(500)


def get_record_by_date(date):
    # date = datetime.strptime(record['date'], '%Y-%m-%d').date()
    year = date.year - 10
    key = str(date.replace(year=year))
    return records_date[key]


def create_record(date, identifier):
    """
    Creates a usable metadata record.
    """

    return {
        'id': identifier,
        'hash': md5(str(identifier).encode('utf-8')).hexdigest(),
        'date': date
    }


def load_records():
    """
    Loads records into two hash tables.
    """

    json_records = json.loads(open('data/dnz-records.json').read())

    for date in json_records:
        identifier = json_records[date]
        record = create_record(date, identifier)

        records_date[record['date']] = record
        records_hash[record['hash']] = record

load_records()
