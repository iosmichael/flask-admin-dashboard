from admin.extensions import firebase_database, firebase_auth_manager
from flask import request

data_mapping = {
	"info": {
		"autoMessage": "Set Auto Message Content",
		"replyIndicator": "Set Response Indicatior",
		"enableScheduler": "false"
	},
	"api": {
		"twilioAccountSID": "Your Twilio SID",
		"twilioAuthToken": "Your Twilio Auth Token"
	},
	"profile": {
		"username": "Your Name",
		"title": "Insurance Agent"
	}
}

def get_node():
	if firebase_auth_manager.is_auth() is False:
		return None
	return firebase_database

def get_settings():
	node = get_node()
	if node is None:
		return node
	setting_dicts = node.child("/{}/setting".format(firebase_auth_manager.get_uid())).get(token=firebase_auth_manager.get_idToken()).val()
	if setting_dicts is None:
		node.child("/{}/setting".format(firebase_auth_manager.get_uid())).set(data_mapping, token=firebase_auth_manager.get_idToken())
		return data_mapping
	return setting_dicts

def add_operator(data):
	firebase_database.child('/operators').push(data)
	return get_operators()

def get_operators():
	data = firebase_database.child('/operators').get().val()	
	data_modified = [{'id': key, 'phone': data[key]['phone']} for key in data.keys()]
	return data_modified

def get_jobs():
	return firebase_database.child('/jobs').get().val()

def update_node(subdir, data):
	node = get_node()
	if node is None:
		return node
	try:
		json = node.child("/{}/setting/{}".format(firebase_auth_manager.get_uid(), subdir)).update(data, token=firebase_auth_manager.get_idToken())
	except request.extensions.HTTPError as e:
		return None
	return json

