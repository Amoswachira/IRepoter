'''redflags endpoints'''
import datetime

from flask_restful import Resource
from flask import jsonify, make_response, request, abort



INCIDENTS = []


class RedFlags(Resource):
    """ RedFlags"""

    def __init__(self):
        self.db = INCIDENTS
        if len(INCIDENTS) == 0:
            self.id = 1
        else:
            self.id = INCIDENTS[-1]['id'] + 1
        self.id = len(INCIDENTS) + 1

    def get(self):
        '''GET ALL REDFLAGS'''
        return make_response(jsonify({
            "status": 200,
            "data": self.db
        }), 200)