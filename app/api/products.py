import json
import os
from random import shuffle

from flask import request

from app.api import api
from app.decorators import jsonify, logrequest, logtime

@api.route('/search/products', methods = ['POST'])
@jsonify
@logrequest
def products_search():
    query = request.args.get('q')
    params      = {}
    ret = {
        'status' : 0,
        'msg' : 'Successful'
    }
    return ret