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

# Create a hash table of all records.
for record in json.loads(open('data/records-2015.json').read())['records']:
    record['hash'] = hashlib.md5(str(record['id']).encode('utf-8')).hexdigest()
    record['date'] = record['date'][-1][:10]
    date = datetime.datetime.strptime(record['date'], '%Y-%m-%d').date()
    today_year = date.year + 10
    records[str(date.replace(year=today_year))] = record

app = flask.Flask(__name__)


@app.route('/')
def index():
    today = datetime.date.today()
    metadata = get_metadata(records[str(today)]['id'])
    image = metadata['thumbnail_url']
    readable_date = today.strftime('%d %B %Y')
    return flask.render_template('index.html', image=image, readable_date=readable_date)


@app.route('/hello')
def hello():
    return 'hello'


@app.route('/today')
def today_record():
    today = str(datetime.date.today())
    image = get_metadata(records[today]['id'])['thumbnail_url']
    return flask.render_template('index.html', image=image)


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
