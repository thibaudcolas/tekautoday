import os
import json
import random
import flask
import requests
import hashlib

DNZ_URL = 'http://api.digitalnz.org/v3/records/'
DNZ_KEY = os.environ.get('DNZ_KEY')
records = {}

# TODO This should be switched to records associated with days.
# Create a hash table of all records.
for record in json.loads(open('data/records-2015.json').read())['records']:
    record_hash = hashlib.md5(str(record['id']).encode('utf-8')).hexdigest()
    records[record_hash] = record

app = flask.Flask(__name__)


@app.route('/')
def index():
    image = flask.url_for('static', filename='img/placeholder-clouds-fog-haze-5086.jpeg')
    return flask.render_template('index.html', image=image)


@app.route('/hello')
def hello():
    return 'hello'


@app.route('/random')
def random_record():
    record_hash = random.choice(list(records.keys()))
    image = get_metadata(records[record_hash]['id'])['thumbnail_url']
    return flask.render_template('index.html', image=image)


def get_metadata(id):
    url = DNZ_URL + '{id}.json?api_key={key}'.format(id=id, key=DNZ_KEY)
    return requests.get(url).json()['record']

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
