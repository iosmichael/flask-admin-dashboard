from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from .model.db import db
from .model.user import display_csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
db.init_app(app)

@app.route('/display_user')
def display_user():
	return display_csv()

with app.test_request_context():
	print(display_user())