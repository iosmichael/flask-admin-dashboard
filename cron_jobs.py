import datetime
import sys, os
from flask import Flask, request, render_template, redirect, url_for, make_response
from admin.controller.main_controller import *
from admin.controller.firebase_controller import *
from admin.extensions import *

'''
USER STATES:
	- CREATED
	- SUCCESS 
	- NEGATIVE
	- ARCHIVED

JOB STATES:
	- AUTOMATION
	- MANUAL
'''

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

TEMPLATE_CONTENT = "This is a testing job."

MAX_ASSIGNMENT_PER_OPERATOR = 2

def assign_job(operator, content):
	filter_dict = {
		'tag': 'CREATED'
	}
	page, _ = paginate_with_filters('User', MAX_ASSIGNMENT_PER_OPERATOR, 1, filters=filter_dict)
	for user in page.items:
		record = create_record(user.phone, operator['phone'], content)
		print("successfully created record")
		print(record)
		data = {
			"phone": user.phone,
			"operator": str(operator['phone']),
			"content": content,
			"last_update": datetime.datetime.now().strftime('%H:%M:%S %m/%d/%Y'),
			"tag": "AUTOMATION",
			"record_id": record.id
		}
		firebase_database.child('/jobs').push(data)
		print('successfully pushed job into firebase')
		MSG = update_object('User', user.id, { 'operator': operator['phone'], 'tag': 'ARCHIVED' })
		print("update user object: " + MSG)

def create_record(phone, operator, content):
	record_data = {
		'operator': operator, 
		'phone': phone, 
		'content': content, 
		'is_client': False,
		'time': datetime.datetime.now()
	}
	record = build_object('Record', record_data)
	record, _ = add_object('Record', record)
	return record

def run_job_scripts():
	operators = get_operators()
	for operator in operators:
		print(operator)
		assign_job(operator, TEMPLATE_CONTENT)

with app.app_context():
	run_job_scripts()
	sys.exit("Terminated")