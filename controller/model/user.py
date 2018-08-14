from .db import db
from datetime import datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), unique=False, nullable=False)
	last_name = db.Column(db.String(30), unique=False, nullable=False)
	state = db.Column(db.String(20), unique=False, nullable=True)
	zipcode = db.Column(db.String(20), unique=False, nullable=True)
	dob = db.Column(db.String(20), unique=False, nullable=True)
	sex = db.Column(db.String(10), unique=False, nullable=False)
	phone = db.Column(db.String(20), unique=True, nullable=False)
	tag = db.Column(db.String(30), unique=False, nullable=True, default='CREATED')
	last_response = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

	def as_dict(self):
		data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
		data['last_response'] = self.last_response.strftime('%H:%M:%S %m/%d/%Y')
		return data

	def __repr__(self):
		return '<User %s>' % (self.first_name + " " + self.last_name)

	def update(self, **kwarg):
		if 'first_name' in kwarg.keys():
			self.first_name = kwarg.get('first_name')
		if 'last_name' in kwarg.keys():
			self.first_name = kwarg.get('last_name')
		if 'state' in kwarg.keys():
			self.state = kwarg.get('state')
		if 'zipcode' in kwarg.keys():
			self.zipcode = kwarg.get('zipcode')
		if 'sex' in kwarg.keys():
			self.sex = kwarg.get('sex')
		if 'phone' in kwarg.keys():
			self.phone = kwarg.get('phone')
		if 'tag' in kwarg.keys():
			self.tag = kwarg.get('tag')