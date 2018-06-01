from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

Users = [{'username':'number1', 'email':'riker@rikersisland.com'},
            {}, {}]
