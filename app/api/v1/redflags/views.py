'''views for redflags '''
from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from .models import RedFlagModel
import datetime

##################################################
###### implement validation using reqparse #######
##################################################
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('type',
                    type=str,
                    required=True,
                    help="This field cannot be left blank! "
                    )

parser.add_argument('location',
                    type=str,
                    required=True,
                    help="This field cannot be left blank!"
                    )

parser.add_argument('status',
                    type=str,
                    required=True,
                    help="This field cannot be left blank!"
                    )
parser.add_argument('images',
                    action='append',
                    help="This field can be left blank!"
                    )
parser.add_argument('videos',
                    action='append',
                    help="This field can be left blank!"
                    )

parser.add_argument('comment',
                    type=str,
                    required=True,
                    help="This field cannot be left blank!"
                    )


class RedFlags(Resource):
    """docstring for RedFlags"""

    def __init__(self):
        self.db = RedFlagModel()

    def post(self):
        '''post redfalgs'''
        args = parser.parse_args()
        data = {
            'createdOn': datetime.datetime.utcnow(),
            'createdBy': request.json.get('createdBy', ""),
            'type': 'red-flags',
            'location': request.json.get('location', ""),
            'status': "Under Invsetigation",
            'images': request.json.get('images', ""),
            'videos': request.json.get('videos', ""),
            'title': request.json['title'],
            'comment': request.json.get('comment', "")
        }

        self.db.save(data)

        success_message = {
            'message': 'Created red-flag record'
        }

        return make_response(jsonify({
            "status": 201,
            "data": success_message
        }), 201)

    def get(self):
        '''get all redflags'''
        self.db.get_all()
        return make_response(jsonify({
            "status": 200,
            "data": self.db.get_all()
        }), 200)


class RedFlag(Resource):
    """ RedFlag class for get, delete and put"""

    def __init__(self):
        self.db = RedFlagModel()

    def get(self, redflag_id):
        '''get a specific redflag'''
        incident = self.db.find(redflag_id)
        return make_response(jsonify({
            "status": 200,
            "data": incident
        }), 200)

    def delete(self, redflag_id):
        '''delete a specific redflag'''
        incident = self.db.find(redflag_id)
        self.db.delete(incident)
        success_message = {
            'message': 'red-flag record has been deleted'
        }
        return make_response(jsonify({
            "status": 204,
            "data": success_message
        }))

    def put(self, redflag_id):
        '''put redflags'''
        incident = self.db.find(redflag_id)
        if incident:
            incident['createdBy'] = request.json.get(
                'createdBy', incident['createdBy'])
            incident['location'] = request.json.get(
                'location', incident['location'])
            incident['images'] = request.json.get('images', incident['images'])
            incident['videos'] = request.json.get('videos', incident['videos'])
            incident['title'] = request.json.get('title', incident['title'])
            incident['comment'] = request.json.get(
                'comment', incident['comment'])

            success_message = {
                "message": "Red-flag has been updated"
            }

            return make_response(jsonify({
                "status": 201,
                "data": success_message
            }), 201)


class UpdateLocation(Resource):
    '''redflag class for updatelocation/patch'''

    def __init__(self):
        self.db = RedFlagModel()

    def patch(self, redflag_id):
        '''patch location'''
        incident = self.db.find(redflag_id)
        if incident:
            incident['location'] = request.json.get(
                'location', incident['location'])
            success_message = {
                "message": "Updated red-flag record's location"
            }

            return make_response(jsonify({
                "status": 201,
                "data": success_message
            }), 201)


class UpdateComment(Resource):
    '''class for update location'''

    def __init__(self):
        self.db = RedFlagModel()

    def patch(self, redflag_id):
        '''patch comment'''
        incident = self.db.find(redflag_id)
        if incident:
            incident['comment'] = request.json.get(
                'comment', incident['comment'])

            success_message = {
                "message": "Updated red-flag record's comment"
            }

            return make_response(jsonify({
                "status": 201,
                "data": success_message
            }), 201)
