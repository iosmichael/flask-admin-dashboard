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

def get_settings():
	setting_dicts = firebase_database.child("/setting").get().val()
	if setting_dicts is None:
		node.child("/setting").set(data_mapping)
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
	try:
		json = firebase_database.child("/setting/{}".format(subdir)).update(data)
	except:
		return None
	return json

