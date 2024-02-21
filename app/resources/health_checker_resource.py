from flask_restful import Resource


class HealthChecker(Resource):
    def get(self):
        try:
            return {'message': 'The server is running!'}, 200
        except Exception as e:
            return {'message': f'An error occurred: {e}'}, 500

