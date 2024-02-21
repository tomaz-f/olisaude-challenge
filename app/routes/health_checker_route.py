from flask_restful import Api

from app.resources.health_checker_resource import HealthChecker


def config_routes(app):
    api = Api()

    api.add_resource(HealthChecker, '/health-checker', methods=['GET'], endpoint='health-checker')

    api.init_app(app)

