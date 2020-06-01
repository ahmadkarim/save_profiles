from flask import Flask
from flask_restful import Resource, Api

app = Flask (__name__)
api = Api(app)

class Profile(Resource):
	def get(self):
		return {
			'product' : ['a','b','c']
			}

api.add_resource(Profile, '/')

if __name__ == '__main__':
	app.run (host='0.0.0.0', port= 80 , debug =True)