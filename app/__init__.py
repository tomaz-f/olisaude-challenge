import os
from flask import Flask

from app.database.connection import config_database
from app.database.faker_db import populate_database
from app.routes.health_checker_route import config_routes


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    config_routes(app)
    config_database(app)
    populate_database(50)
    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(debug=True)
