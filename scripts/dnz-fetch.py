import os
import math

from pprint import pprint
from pydnz import Dnz

dnz = Dnz(os.environ.get('DNZ_KEY'))

def dnz_request(page = 1):
    return dnz.search('', _and={'category':['Images'], 'year':['2005+TO+2006']}, per_page=100, page=page, fields=['id', 'title', 'date'])

result = dnz_request()
