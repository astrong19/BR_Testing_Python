import os
import json
import csv
import StringIO
import logging

from flask import jsonify, request, Response, stream_with_context
import requests

from . import endpoints
from ms.responders import ErrorResponder
from ms.utils.http import request_to_microservice

@endpoints.route('/hello', methods=['GET'])
def say_hello():
    """making dummy microservices"""
    logging.info('making dummy microservice')

    url = 'http://production-api.globalforestwatch.org/geostore/admin/'

    iso = request.args.get('iso')

    test = url + iso
    r = requests.get(url=test)
    data = r.json()

    return jsonify({'data': data}), 200
