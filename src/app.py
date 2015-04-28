import os
import json
import random
import flask

from hashlib import md5

records = {}

# Create a hash table of all records.
for record in json.loads(open('data/records-2015.json').read())['records']:
    records[md5(str(record['id']).encode('utf-8')).hexdigest()] = record

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/hello')
def hello():
    return 'hello'


@app.route('/random')
def random_record():
    record_hash = random.choice(list(records.keys()))
    return str(records[record_hash])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
