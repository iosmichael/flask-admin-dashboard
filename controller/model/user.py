from .db import db
import csv, os
from sqlalchemy.exc import IntegrityError

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), unique=False, nullable=False)
	last_name = db.Column(db.String(30), unique=False, nullable=False)
	state = db.Column(db.String(20), unique=False, nullable=True)
	zipcode = db.Column(db.String(20), unique=False, nullable=True)
	dob = db.Column(db.String(20), unique=False, nullable=True)
	sex = db.Column(db.String(10), unique=False, nullable=False)
	phone = db.Column(db.String(20), unique=False, nullable=False)

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

	def __repr__(self):
		return '<User %s>' % (self.first_name + " " + self.last_name)