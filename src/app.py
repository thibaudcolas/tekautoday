# -*- coding: utf-8 -*-

from os import environ
import flask

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
    context = utils.format_response(cache['record'], cache['metadata'])

    return flask.render_template('index.html', **context)


@app.route('/record/<record_hash>')
def record(record_hash):
    record = records.get_record_by_hash(record_hash)
    metadata = utils.get_metadata(record)
    context = utils.format_response(record, metadata)

    return flask.render_template('index.html', **context)


@app.route('/api/record/')
def api_index():
    global cache
    cache = utils.update_record_cache(cache)

    return flask.jsonify(**cache['metadata'])


@app.route('/api/record/<record_hash>')
def api_record(record_hash):
    metadata = utils.get_metadata(records.get_record_by_hash(record_hash))

    return flask.jsonify(**metadata)


@app.errorhandler(500)
def internal_error(error):
    context = utils.format_error_response(error)

    return flask.render_template('error.html', **context)


@app.errorhandler(404)
def not_found(error):
    context = utils.format_error_response(error)

    return flask.render_template('error.html', **context)

if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    debug = environ.get('ENV', 'development') == 'development'

    app.run(host='0.0.0.0', port=port, debug=debug)
