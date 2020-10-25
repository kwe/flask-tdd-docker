from flask import Blueprint
from flask_restx import Resource, api
from flask_restx.api import Api

ping_blueprint = Blueprint('ping', __name__)
api = Api(ping_blueprint)

class Ping(Resource):
  def get(self):
    return {
      'status' : 'success',
      'message' : 'pong!'
    }
api.add_resource(Ping, '/ping')