import os
import math
import json

from pprint import pprint
from pydnz import Dnz

dnz = Dnz(os.environ.get('DNZ_KEY'))

results = []


def dnz_request(page=1):
    filters = {
        'category': ['Images'],
        'year': ['2005+TO+2006']
    }
    fields = ['id', 'date']
    return dnz.search('', _and=filters, per_page=100, page=page, fields=fields)

# First request.
first_result = dnz_request()

results = first_result.records

iterations = math.ceil(first_result.result_count / 100)
# iterations = 5

# Subsequent requests.
for i in range(2, iterations + 1):
    records = dnz_request(i).records
    for record in records:
        results.append({
            'id': record['id'],
            'date': record['date']
        })
    pprint(len(results))

with open('dnz-2015.json', 'w') as outfile:
    json.dump(results, outfile)
