from admin.extensions import db
from datetime import datetime

class Record(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	operator = db.Column(db.String(30))
	phone = db.Column(db.String(30))
	content = db.Column(db.String(300))
	is_client = db.Column(db.Boolean)
	delivered = db.Column(db.Boolean, default=False)
	time = db.Column(db.DateTime, default=datetime.utcnow)

	def as_dict(self):
		data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
		data['time'] = self.time.strftime('%H:%M:%S %m/%d/%Y')
		return data

	def __repr__(self):
		return '<Record %s>' % (self.operator + " " + self.phone + " " + self.content + ": " + self.time.strftime('%H:%M:%S %m/%d/%Y'))
	
	def update(self, **kwarg):
		if 'operator' in kwarg.keys():
			self.operator = kwarg.get('operator')
		if 'content' in kwarg.keys():
			self.content = kwarg.get('content')
		if 'time' in kwarg.keys():
			self.time = kwarg.get('time')
		if 'delivered' in kwarg.keys():
			self.delivered = kwarg.get('delivered')
			