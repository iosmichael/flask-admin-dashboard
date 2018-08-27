from admin.extensions import db

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tag = db.Column(db.String(30), unique=True, nullable=False)
	content = db.Column(db.String(30), unique=False, nullable=False, default="MISSING CONTENT")
	tru_indicator = db.Column(db.String(30), unique=False, nullable=False, default='KEYWORD')
	fal_indicator = db.Column(db.String(30), unique=False, nullable=False, default='KEYWORD')
	tru_tag = db.Column(db.String(20), unique=False, nullable=False, default='NULL')
	fal_tag = db.Column(db.String(20), unique=False, nullable=False, default='NULL')
	el_tag = db.Column(db.String(20), unique=False, nullable=False, default='NULL')

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

	def __repr__(self):
		return '<Message %s>' % (self.tag + " " + self.tru_tag + " " + self.fal_tag)
	
	def update(self, **kwarg):
		if 'tag' in kwarg.keys():
			self.tag = kwarg.get('tag')
		if 'content' in kwarg.keys():
			self.content = kwarg.get('content')
		if 'tru_indicator' in kwarg.keys():
			self.tru_indicator = kwarg.get('tru_indicator')
		if 'fal_indicator' in kwarg.keys():
			self.fal_indicator = kwarg.get('fal_indicator')
		if 'tru_tag' in kwarg.keys():
			self.tru_tag = kwarg.get('tru_tag')
		if 'fal_tag' in kwarg.keys():
			self.fal_tag = kwarg.get('fal_tag')
		if 'el_tag' in kwarg.keys():
			self.el_tag = kwarg.get('el_tag')