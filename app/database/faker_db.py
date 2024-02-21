from app import create_app
from app.models.client_model import Client, db as client_db
from app.models.disease_type_model import DiseaseType, db as disease_type_db
from faker import Faker
import random

fake = Faker()


def generate_fake_disease_type():
    # Generating a random disease type for testing purposes
    disease_name = fake.word()
    problem_degree = random.randint(1, 2)
    disease_type = DiseaseType(name=disease_name, problem_degree=problem_degree)
    disease_type_db.session.add(disease_type)
    disease_type_db.session.commit()
    return disease_type


def generate_fake_client():
    # Generating a random client for testing purposes
    name = fake.name()
    birth_date = fake.date_of_birth()
    gender = fake.random_element(elements=('Male', 'Female'))
    disease_type = generate_fake_disease_type()
    client = Client(name=name, birth_date=birth_date, gender=gender, disease_type=disease_type)
    client_db.session.add(client)
    client_db.session.commit()


def populate_database(num_clients=50):
    # Populate the database with fake clients
    for _ in range(num_clients):
        generate_fake_client()
