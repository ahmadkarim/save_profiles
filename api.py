from flask import Flask
from flask_restful import Resource, Api

app = Flask (__name__)
api = Api(app)

class Profile(Resource):
	def get(self):
		return {
			'profile1' : {
				'CH1':'tpAusten',
				'CH2':'gZlm'
			},
			'profile2' : {
				'SP1':'rEukc',
				'SP2':'firma1'
			},
			'profile3' : {
				'CP1':'rEukc'
			}
		}

api.add_resource(Profile, '/')

if __name__ == '__main__':
	app.run (host='0.0.0.0', port= 80 , debug =True)