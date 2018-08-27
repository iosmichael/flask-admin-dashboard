from admin.extensions import db
from datetime import datetime

class Record(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	carrier = db.Column(db.String(30))
	phone = db.Column(db.String(30))
	content = db.Column(db.String(300))
	receive = db.Column(db.Boolean)
	time = db.Column(db.DateTime, default=datetime.utcnow)

	def as_dict(self):
		data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
		data['time'] = self.time.strftime('%H:%M:%S %m/%d/%Y')
		return data

	def __repr__(self):
		return '<Record %s>' % (self.carrier + " " + self.phone + " " + self.content + ": " + self.time.strftime('%H:%M:%S %m/%d/%Y'))
	