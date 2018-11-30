from flask import Flask, Blueprint
# from flask_restful import Api, Resource


from .api.v1 import version1 as v1


def create_app():
    app = Flask(__name__)
    # api = Api(app)
    app.register_blueprint(v1)
    return app 