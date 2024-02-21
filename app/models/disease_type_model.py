from app.database.connection import db


class DiseaseType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    problem_degree = db.Column(db.Integer, nullable=False)  # Assuming problem degree is an integer from 1 to 2

    def __init__(self, name, problem_degree):
        self.name = name
        self.problem_degree = problem_degree
