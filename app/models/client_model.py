from datetime import datetime

from app.database.connection import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    disease_type_id = db.Column(db.Integer, db.ForeignKey('disease_type.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    disease_type = db.relationship('DiseaseType', backref='clients')

    def __init__(self, name, birth_date, gender, disease_type):
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.disease_type = disease_type
