from flask import Blueprint
from flask_restful import Api, Resource


from .redflags.views import RedFlags, RedFlag

version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)

# redflags
# api.add_resource(UpdateLocation, '/red-flags/<int:redflag_id>/location')
api.add_resource(RedFlags, '/red-flags') 
api.add_resource(RedFlag, '/red-flags/<int:redflag_id>')
# api.add_resource(UpdateComment, '/red-flags/<int:redflag_id>/comment')
