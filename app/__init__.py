from flask import Flask
from app.route import customer_route
import os
from app.utils.database import db, migrate
from app.models import customer

app = Flask(__name__)

DATABASE_TYPE = os.getenv('DATABASE_TYPE')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_PORT = os.getenv('DATABASE_PORT')
app.config["SQLALCHEMY_DATABASE_URI"] = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

db.init_app(app)
# migrate.init_app(app, db)

app.register_blueprint(customer_route.customer_blueprint, url_prefix="/customer")

# Testing Routing App 
# @app.route('/')
# def my_app():
#     return 'hello revou'