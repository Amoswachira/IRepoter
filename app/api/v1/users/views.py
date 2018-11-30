# from flask_restful import Resource
# from flask import jsonify, make_response, request, abort

# import datetime

# users = []


# class Users(Resource):
#     """ users"""
    
#     def __init__(self):
#         self.db = users
#         if len(users) == 0:
#             self.id = 1
#         else:
#             self.id = users[-1]['id'] + 1  
#         self.id = len(users) + 1

#     def get(self):

#         return make_response(jsonify({
#             "status": 200,
#             "data": self.db
#         }), 200) 
       
#     def post(self):
        
#         data = {
#                 'id': self.id,
#                 'firstname': request.json['firstname'],
#                 'lastname': request.json['lastname'],
#                 'othernames': request.json['othernames'],
#                 'email': request.json['email'],
#                 'phoneNumber': request.json['phoneNumber'],
#                 'username': request.json['username'],
#                 'registered': datetime.datetime.utcnow(),
#                 'isAdmin': request.json['isAdmin']
#         }
#         self.db.append(data)
        
#         success_message = {
#             'id': self.id,
#             'message': 'User Created '
#         }

#         return make_response(jsonify({
#             "status": 201,
#             "data": success_message
#         }), 201)
    

# class User(Resource):
#     """docstring of User"""
#     def __init__(self):
#         self.db = users
        
#     def get(self, user_id):

#         for user in users:
#             if user['id'] == user_id:
#                 return make_response(jsonify({
#                     "status": 200,
#                     "data": user
#                 }), 200)
#         return make_response(jsonify({
#             "status": 404,
#             "error": "user does not exist"
#         }), 404)      
          
#     def delete(self, user_id):
#         for user in users:
#             if user['id'] == user_id:
#                 users.remove(user)
#                 success_message = {
#                  'id': user_id,
#                  'message': 'user record has been deleted'
#                 }
#                 return make_response(jsonify({
#                  "status": 204,
#                  "data": success_message
#                 }))
#         return make_response(jsonify({
#             "status": 404,
#             "error": "user does not exit"
#         }))   

#     def put(self, user_id):
#         for user in users:
#             if user['id'] == user_id:
#                 user['firstname'] = request.json.get
#                 ('firstname', user['firstname'])
#                 user['lastname'] = request.json.get
#                 ('lastname', user['lastname'])
#                 user['othernames'] = request.json.get
#                 ('othernames', user['othernames'])
#                 user['email'] = request.json.get
#                 ('email', user['email'])
#                 user['phoneNumber'] = request.json.get
#                 ('phoneNumber', user['phoneNumber'])
#                 user['username'] = request.json.get
#                 ('username', user['username'])
#                 user['isAdmin'] = request.json.get
#                 ('isAdmin', user['isAdmin'])

#                 success_message = {
#                     "id": user_id,
#                     "message": "user has been updated"
#                 }

#                 return make_response(jsonify({
#                     "status": 201,
#                     "data": success_message
#                 }), 201)
#         return make_response(jsonify({
#             "status": 404,
#             "error": "user does not exist"
#         }), 404)
