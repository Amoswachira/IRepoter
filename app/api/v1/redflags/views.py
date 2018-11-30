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
    
    def post(self):
        '''create redflags record''' 
        data = {
                'id': self.id,
                'createdOn': datetime.datetime.utcnow(),
                'createdBy': request.json['createdBy'],
                'type': 'red-flags',
                'location': request.json.get('location', ""),
                'status': "draft",
                'images': request.json.get('images', ""),
                'videos': request.json.get('videos', ""),
                'title': request.json['title'],
                'comment': request.json.get('comment', "")
        }
        self.db.append(data)
        
        success_message = {
            'id': self.id,
            'message': 'Created red-flag record'
        }

        return make_response(jsonify({
            "status": 201,
            "data": success_message
        }), 201)


class RedFlag(Resource):
    """ RedFlag specific"""
    def __init__(self):
        self.db = INCIDENTS
        
    def get(self, redflag_id):
        '''get a redflag'''
        for incident in INCIDENTS:
            if incident['id'] == redflag_id:
                return make_response(jsonify({
                    "status": 200,
                    "data": incident
                }), 200)
        return make_response(jsonify({
            "status": 404,
            "error": "Red-flag does not exist"
        }), 404) 

    def delete(self, redflag_id):
        '''delete a redflag'''
        for incident in INCIDENTS:
            if incident['id'] == redflag_id:
                INCIDENTS.remove(incident)
                success_message = {
                 'id': redflag_id,
                 'message': 'red-flag record has been deleted'
                }
                return make_response(jsonify({
                 "status": 204,
                 "data": success_message
                }))
        return make_response(jsonify({
            "status": 404,
            "error": "Red-flag does not exist"
        }))             

    def put(self, redflag_id):
        '''edit redflag record'''
        for incident in INCIDENTS:
            if incident['id'] == redflag_id:
                incident['createdBy'] = request.json.get
                ('createdBy', incident['createdBy'])
                incident['location'] = request.json.get
                ('location', incident['location'])
                incident['images'] = request.json.get
                ('images', incident['images'])
                incident['videos'] = request.json.get
                ('videos', incident['videos'])
                incident['title'] = request.json.get
                ('title', incident['title'])
                incident['comment'] = request.json.get
                ('comment', incident['comment'])

                success_message = {
                    "id": redflag_id,
                    "message": "Red-flag has been updated"
                }

                return make_response(jsonify({
                    "status": 201,
                    "data": success_message
                }), 201)
        return make_response(jsonify({
            "status": 404,
            "error": "Red-flag does not exist"
        }), 404)


class UpdateLocation(Resource):
    '''update redflag record location'''
    def patch(self, redflag_id):
        for incident in INCIDENTS:
            if incident['id'] == redflag_id:
                incident['location'] = request.json.get
                ('location', incident['location'])

                success_message = {
                    "id": redflag_id,
                    "message": "Updated red-flag record's location"
                }

                return make_response(jsonify({
                    "status": 201,
                    "data": success_message
                }), 201)
        return make_response(jsonify({
            "status": 404,
            "error": "Red-flag does not exist"
        }), 404)        


class UpdateComment(Resource):
    '''update comment'''
    def patch(self, redflag_id):
        for incident in INCIDENTS:
            if incident['id'] == redflag_id:
                incident['comment'] = request.json.get
                ('comment', incident['comment'])

                success_message = {
                    "id": redflag_id,
                    "message": "Updated red-flag record's comment"
                }

                return make_response(jsonify({
                    "status": 201,
                    "data": success_message
                }), 201)
        return make_response(jsonify({
            "status": 404,
            "error": "Red-flag does not exist"
        }), 404)  
        