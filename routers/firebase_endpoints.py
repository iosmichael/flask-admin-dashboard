import json
import os
from flask import Blueprint, request, url_for
from admin.extensions import firebase_database, firebase_auth_manager
from admin.controller.firebase_controller import *

'''
this file deals with endpoints that connects to firebase
'''
firebase_endpoints = Blueprint('firebase_endpoints', __name__, template_folder='templates')

@firebase_endpoints.route('/firebase/add/operator', methods=['POST'])
def create_operator():
	data = add_operator(request.form.to_dict())
	if data is None:
		return None
	return json.dumps(data)

@firebase_endpoints.route('/firebase/update/<name>', methods=['POST'])
def update_settings(name):
	data = update_node(name, request.form.to_dict())
	if data is None:
		return None
	return json.dumps(data)

@firebase_endpoints.route('/firebase/update/<name>/<id>')
def update_operator(name, id):
	pass

@firebase_endpoints.route('/firebase/delete/<name>/<id>')
def delete_operator(name, id):
	pass