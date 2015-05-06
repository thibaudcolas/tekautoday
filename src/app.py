# -*- coding: utf-8 -*-

import os
import json
import random
import flask
import requests
import hashlib
import datetime

DNZ_URL = 'http://api.digitalnz.org/v3/records/'
DNZ_KEY = os.environ.get('DNZ_KEY')

records = {}
records_hash = {}

# Create a hash table of all records.
for record in json.loads(open('data/records-2015.json').read())['records']:
    record['hash'] = hashlib.md5(str(record['id']).encode('utf-8')).hexdigest()
    record['date'] = record['date'][-1][:10]
    date = datetime.datetime.strptime(record['date'], '%Y-%m-%d').date()
    today_year = date.year + 10
    records[str(date.replace(year=today_year))] = record
    records_hash[record['hash']] = record

app = flask.Flask(__name__)

print(records)


@app.route('/')
def index():
    today = datetime.date.today()
    record = records[str(today)]
    metadata = get_metadata(record['id'])

    date = datetime.datetime.strptime(record['date'], '%Y-%m-%d').date()

    if metadata['object_url'] is not None:
        image = metadata['object_url']
    else:
        image = metadata['large_thumbnail_url']

    context = {
        'readable_date': date.strftime('%d %B %Y'),
        'record': {
            'image': image,
            'url': metadata['landing_url'],
            'author': metadata['display_content_partner'],
            'title': metadata['title'],
            'permalink': '/record/' + record['hash']
        }
    }

    return flask.render_template('index.html', **context)


@app.route('/record/<record_hash>')
def record(record_hash):
    record = records_hash[record_hash]
    metadata = get_metadata(record['id'])

    date = datetime.datetime.strptime(record['date'], '%Y-%m-%d').date()

    if metadata['object_url'] is not None:
        image = metadata['object_url']
    else:
        image = metadata['large_thumbnail_url']

    context = {
        'readable_date': date.strftime('%d %B %Y'),
        'record': {
            'image': image,
            'url': metadata['landing_url'],
            'author': metadata['display_content_partner'],
            'title': metadata['title'],
            'permalink': '/record/' + record_hash
        }
    }

    return flask.render_template('index.html', **context)


@app.route('/api/record/')
def api_index():
    today = datetime.date.today()
    record = records[str(today)]
    metadata = get_metadata(record['id'])
    metadata['hash'] = record['hash']

    return flask.jsonify(**metadata)


@app.route('/api/record/<record_hash>')
def api_record(record_hash):
    metadata = get_metadata(records_hash[record_hash]['id'])
    metadata['hash'] = record_hash

    return flask.jsonify(**metadata)


def get_metadata(id):
    url = DNZ_URL + '{id}.json?api_key={key}'.format(id=id, key=DNZ_KEY)

    return requests.get(url).json()['record']

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
