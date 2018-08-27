import json
import os
from flask import Blueprint, request, url_for
from admin.extensions import firebase_database, firebase_auth_manager

'''
this file deals with endpoints that connects to firebase
'''
firebase_endpoints = Blueprint('firebase_endpoints', __name__, template_folder='templates')

@firebase_endpoints.route('/firebase/add/<name>')
def add_operator(name):
	if firebase_auth_manager.is_auth() is False:
		return "LOGIN ERROR"
	data = {
		"name": "good item"
	}
	firebase_database.child('/accounts/{}/{}'.format(firebase_auth_manager.get_uid(), name)).push(data, firebase_auth_manager.get_idToken())
	return "SUCCESS"

@firebase_endpoints.route('/firebase/update/<name>')
def update_settings():
	pass

@firebase_endpoints.route('/firebase/update/<name>/<id>')
def update_operator(id):
	pass

@firebase_endpoints.route('/firebase/delete/<name>/<id>')
def delete_operator(id):
	pass