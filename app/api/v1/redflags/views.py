'''view for incidents records '''
import datetime
import re
from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from .models import RedFlagModel


def is_valid(value):
    '''check if the string is empty'''
    if not value:
        raise ValueError("empty string")


def has_valid_characters(value):
    '''check if string has  special characters or numbers
    '''
    if not re.match(r"[A-Za-z]", value):
        raise ValueError("contains special characters or numbers")


# implement validation using reqparse


PARSER = reqparse.RequestParser(bundle_errors=True)
PARSER.add_argument('type',
                    type=str,
                    required=True,
                    choices=("red-flag", "intervention"),
                    help="type field cannot be left "
                         "blank or Bad choice: {error_msg},400"
                    )

PARSER.add_argument('createdBy',
                    type=has_valid_characters,
                    help="createdBy field can be left blank or {error_msg},400"
                    )
PARSER.add_argument('location',
                    type=has_valid_characters,
                    required=True,
                    help="location field annt be left blank or {error_msg},400"
                    )
PARSER.add_argument('images',
                    action='append',
                    help="images field can be left blank!"
                    )
PARSER.add_argument('videos',
                    action='append',
                    help="videos field can be left blank!"
                    )

PARSER.add_argument('comment',
                    type=has_valid_characters,
                    required=True,
                    help="comment field cannt be left blank or {error_msg},400"
                    )
PARSER.add_argument('title',
                    type=has_valid_characters,
                    required=True,
                    help="title field cannot be left blank or  {error_msg},400"
                    )


class RedFlags(Resource):
    """ post method and get method for incidents records """

    def __init__(self):
        '''init(constructor) '''
        self.db = RedFlagModel()

    def post(self):
        '''post incident records method'''
        PARSER.parse_args()
        data = {
            'createdOn': datetime.datetime.utcnow(),
            'createdBy': request.json.get('createdBy', ""),
            'type': 'red-flag',
            'location': request.json.get('location', ""),
            'status': "draft",
            'images': request.json.get('images', ""),
            'videos': request.json.get('videos', ""),
            'title': request.json['title'],
            'comment': request.json.get('comment', "")
        }
        # validate if incidents are of type string
        for key, value in data.items():
            if key == 'location' and type(value) != str:
                return {"status": 400,
                        "data": [{
                            "message": "location  must be a string."
                        }]}, 400

            elif key == 'createdBy' and type(value) != str:
                return {"status": 400,
                        "data": [{
                            "message": "createdBy  must be a string."
                        }]}, 400

            elif key == 'comment' and type(value) != str:
                return {"status": 400,
                        "data": [{
                            "message": "comment  must be a string."
                        }]}, 400
            elif key == 'title' and type(value) != str:
                return {"status": 400,
                        "data": [{
                            "message": "title  must be a string."
                        }]}, 400

        self.db.save(data)

        success_message = {
            'message': 'Created Incident record'
        }

        return make_response(jsonify({
            "status": 201,
            "data": success_message
        }), 201)

    def get(self):
        '''get method for all incidents'''
        INCIDENTS = self.db.get_all()
        if len(INCIDENTS) != 0:
            All_INCIDENTS = self.db.get_all()
            return make_response(jsonify({
                "status": 200,
                "data": All_INCIDENTS
            }), 200)
        return {"status": 404,
                "data": [{
                    "message": "No Incident records."
                }]}, 404


class RedFlag(Resource):
    """
    Get method for specific id,
    delete method for a specific id,
    put method for specific id
    """

    def __init__(self):
        '''init(constructor) '''
        self.db = RedFlagModel()

    def get(self, redflag_id):
        '''get a specific redflag'''
        incident = self.db.find(redflag_id)
        if incident:
            return make_response(jsonify({
                "status": 200,
                "data": incident
            }), 200)
        return {"status": 404,
                "data": [{
                    "message": "Incident record does not exist."
                }]}, 404

    def delete(self, redflag_id):
        '''delete a specific redflag'''
        incident = self.db.find(redflag_id)
        if incident:
            self.db.delete(incident)
            success_message = {
                'message': 'Incident has been deleted'
            }
            return make_response(jsonify({
                "status": 204,
                "data": success_message
            }))
        return {"status": 404,
                "data": [{
                    "message": "Incident record Not Found."
                }]}, 404

    def put(self, redflag_id):
        '''update a specific redflag'''
        PARSER.parse_args()
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
                "message": "Incident record has been updated"
            }

            return make_response(jsonify({
                "status": 201,
                "data": success_message
            }), 201)
        return {"status": 404,
                "data": [{
                    "message": "Incident record Not Found."
                }]}, 404


class UpdateLocation(Resource):
    ''' patch method for location'''

    def __init__(self):
        '''init(constructor) intialize the db '''
        self.db = RedFlagModel()

    def patch(self, redflag_id):
        '''patch location'''
        location_paserr = reqparse.RequestParser(bundle_errors=True)
        location_paserr.add_argument('location',
                                     type=has_valid_characters,
                                     required=True,
                                     help="location field can't be left blank"
                                     )
        location_paserr.parse_args()
        location_incident = self.db.find(redflag_id)
        if location_incident:
            location_incident['location'] = request.json.get(
                'location', location_incident['location'])
            return make_response(jsonify({
                "status": 201,
                "data": [{
                    "message": "Updated Incident's location"
                     }]
            }), 201)
        return {"status": 404,
                "data": [{
                    "message": "Incident record Not Found."
                }]}, 404


class UpdateComment(Resource):
    '''class which includes patch method for comment '''

    def __init__(self):
        self.db = RedFlagModel()

    def patch(self, redflag_id):
        '''patch comment method'''
        paserrr = reqparse.RequestParser(bundle_errors=True)
        paserrr.add_argument('comment',
                             type=has_valid_characters,
                             required=True,
                             help="comment field is required or"
                             "{error_msg},400"
                             )
        paserrr.parse_args()
        incident = self.db.find(redflag_id)
        if incident:
            incident['comment'] = request.json.get(
                'comment', incident['comment'])

            success_message = {
                "message": "Updated Incident's comment"
            }

            return make_response(jsonify({
                "status": 201,
                "data": success_message
            }), 201)
        return {"status": 404,
                "data": [{
                    "message": "Incident record Not Found."
                }]}, 404
