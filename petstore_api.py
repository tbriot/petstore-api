from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Pets(Resource):
    def get(self):
        return [
			{
				"id": 1,
				"type": "dog",
				"price": 249.99
			},
			{
				"id": 2,
				"type": "cat",
				"price": 124.99
			},
			{
				"id": 3,
				"type": "fish",
				"price": 0.99
			}
		]

api.add_resource(Pets, '/api/pets')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)