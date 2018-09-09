import json
import datetime
import os, sys
from flask import Flask, request, render_template, redirect, url_for
from admin.extensions import firebase_database, firebase_auth_manager
from admin.controller.reset_controller import *
from admin.controller.main_controller import *

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def create_record(phone, operator, content):
	record_data = {
		'operator': operator, 
		'phone': phone, 
		'content': content, 
		'is_client': False,
		'time': datetime.datetime.now()
	}
	record = build_object("Record", record_data)
	print(record)
	return record

def search_delivered_record():
	page, _ = paginate_with_filters('Record', 20, page=3, filters={'delivered': True})
	for record in page.items:
		print(record)

with app.app_context():
	# operator = {
	# 'phone': '8157612213',
	# 'id': 'yHD9R9uS9ZgBboP4nUuXR2h1cj43'
	# }
	# jobs = firebase_database.child('/jobs').order_by_child('operator').equal_to('8157612213').get().val()
	# jobs_with_tag = [{"id": key, "phone": jobs[key]['phone'], "operator":jobs[key]['operator'], "content": jobs[key]['content'], "record_id": jobs[key]['record_id']} for key in jobs.keys() if jobs[key]['tag'] == "AUTOMATION"]
	# print(jobs_with_tag)
	# sys.exit("Terminated")
	search_delivered_record()
	sys.exit('Terminated')