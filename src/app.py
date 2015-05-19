# -*- coding: utf-8 -*-

from os import environ
import flask

from datetime import datetime

import records
import utils
import filters

app = flask.Flask(__name__)
app.register_blueprint(filters.blueprint)

cache = utils.update_record_cache()


@app.route('/')
def index():
    global cache
    cache = utils.update_record_cache(cache)

    d = datetime.strptime(cache['record']['date'], '%Y-%m-%d').date()

    if cache['metadata']['object_url'] is not None:
        image = cache['metadata']['object_url']
    else:
        image = cache['metadata']['large_thumbnail_url']

    context = {
        'readable_date': d.strftime('%d %B %Y'),
        'record': {
            'image': image,
            'url': cache['metadata']['landing_url'],
            'author': cache['metadata']['display_content_partner'],
            'title': cache['metadata']['title'],
            'permalink': '/record/' + cache['record']['hash']
        },
        'calendar': utils.get_calendar()
    }

    return flask.render_template('index.html', **context)


@app.route('/record/<record_hash>')
def record(record_hash):
    record = records.records_hash[record_hash]
    metadata = utils.get_metadata(record)

    d = datetime.datetime.strptime(record['date'], '%Y-%m-%d').date()

    if metadata['object_url'] is not None:
        image = metadata['object_url']
    else:
        image = metadata['large_thumbnail_url']

    context = {
        'readable_date': d.strftime('%d %B %Y'),
        'record': {
            'image': image,
            'url': metadata['landing_url'],
            'author': metadata['display_content_partner'],
            'title': metadata['title'],
            'permalink': '/record/' + record_hash
        },
        'calendar': utils.get_calendar()
    }

    return flask.render_template('index.html', **context)


@app.route('/api/record/')
def api_index():
    global cache
    cache = utils.update_record_cache(cache)

    return flask.jsonify(**cache['metadata'])


@app.route('/api/record/<record_hash>')
def api_record(record_hash):
    metadata = utils.get_metadata(records.records_hash[record_hash])

    return flask.jsonify(**metadata)


if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
