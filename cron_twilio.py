import datetime
import sys
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = '/tmp/flask/upload'
db.init_app(app)

MAX_MSG_PER_OPERATOR = 20
JOB_ORDER = ['MANUAL', 'AUTOMATION']

def fetch_jobs_with_operator(operator):
	count = 0
	print(operator)
	jobs = firebase_database.child('/jobs').order_by_child('operator').equal_to(str(operator['phone'])).get().val()
	for tag in JOB_ORDER:
		jobs_with_tag = [{"id": key, "phone": jobs[key]['phone'], "operator":jobs[key]['operator'], 
		"content": jobs[key]['content'], "record_id": jobs[key]['record_id'], "last_update": jobs[key]['last_update']} for key in jobs.keys() if jobs[key]['tag'] == tag]
		for job in jobs_with_tag:
			execute_job(job)
			count += 1
			if count == 20:
				return

def execute_job(job):
	twilio_send_msg(job)
	firebase_database.child('/jobs/{}'.format(job['id'])).remove()
	#update record
	update_object('Record', job['record_id'], {'delivered': True, 'time': datetime.datetime.now()})

def twilio_send_msg(job):
	print("sending twilio job: {} from {} to {} at {}".format(job['content'], job['operator'], job['phone'], job['last_update']))
	pass

def run_job_scripts():
	operators = get_operators()
	for operator in operators:
		fetch_jobs_with_operator(operator)

with app.app_context():
	run_job_scripts()
	sys.exit("Terminate")