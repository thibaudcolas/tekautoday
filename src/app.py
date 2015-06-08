from os import environ
import flask

import records
import utils
import filters
import feed

app = flask.Flask(__name__, static_folder='static', static_url_path='')
app.register_blueprint(filters.blueprint)
app.register_blueprint(feed.blueprint)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/')
def index():
    cache = utils.update_record_cache()
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
    cache = utils.update_record_cache()

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

    records.load_records()
    cache = utils.update_record_cache()
    app.run(host='0.0.0.0', port=port, debug=debug)
