import json
import os

from webargs import Arg
from webargs.flaskparser import parser
from random import shuffle

from flask import request
from app.api import api
from app.decorators import jsonify, logrequest, logtime

query_object_structure = {
    'query' : Arg({
        'type' : Arg(str, required=True, validate=lambda t: t=='products'),
        'filters' : Arg({
            'q' : Arg(str, required=True)
            }, required=True)
        }),
    'offset' : Arg(int, default = 0),
    'size' : Arg(int, default = 10)
    }

@api.route('/search/products/', methods = ['POST'])
@jsonify
@logrequest
def products_search():
    params      = parser.parse(query_object_structure, request)
    f = open(os.path.join(os.getcwd(), 'data', 'product_search_results.json'), 'r')
    ret = json.loads(f.read())
    return paginate(ret, params['offset'], params['size'])

def paginate(ret, offset, size):
    results = ret['results'][offset:offset+size]
    total_results = len(results)
    ret.update({'results' : results, 'total_results' : total_results})
    return ret
