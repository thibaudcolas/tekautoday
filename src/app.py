# -*- coding: utf-8 -*-

from os import environ
import flask

import datetime

import records
import utils
import filters

app = flask.Flask(__name__)
app.register_blueprint(filters.blueprint)


@app.route('/')
def index():
    today = datetime.date.today()
    record = records.records_date[str(today)]
    metadata = utils.get_metadata(record)

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
        },
        'calendar_month': utils.get_calendar()
    }

    return flask.render_template('index.html', **context)


@app.route('/record/<record_hash>')
def record(record_hash):
    record = records.records_hash[record_hash]
    metadata = utils.get_metadata(record)

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
    record = records.records_date[str(today)]
    metadata = utils.get_metadata(record)

    return flask.jsonify(**metadata)


@app.route('/api/record/<record_hash>')
def api_record(record_hash):
    metadata = utils.get_metadata(records.records_hash[record_hash])

    return flask.jsonify(**metadata)


if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
