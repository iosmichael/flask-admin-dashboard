import json
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from .controller.model.db import db
from .controller.user_controller import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
db.init_app(app)

@app.route('/')
def admin():
	return render_template('dashboard/index.html')

@app.route('/admin')
def admin_change():
	(header, users), _ = display_user()
	return render_template('dashboard/index.html', header = header, users=users)

@app.route('/page/<page>')
def user_page(page):
	(users, pages), _ = retrieve_users(page=int(page))
	user_dicts = [user.as_dict() for user in users]
	return json.dumps(user_dicts)

# @app.route('/import')
# def import_user():
# 	import_csv()
# 	return 'success'

# @app.route('/create_all')
# def create_all():
# 	db.drop_all()
# 	db.create_all()
# 	return 'success'

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=5000)