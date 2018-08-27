from admin.extensions import firebase_database, firebase_auth_manager
from flask import request

data_mapping = {
	"info": {
		"autoMessage": "Set Auto Message Content",
		"replyIndicator": "Set Response Indicatior"
		"enableScheduler": False
	},
	"api": {
		"twilioAccoundSID": "Your Twilio SID",
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
	return firebase_database.child('/{}'.format(firebase_auth_manager.get_uid()))

def get_settings():
	node = get_node()
	if node is None:
		return node
	setting_dicts = node.child("setting").get(token=firebase_auth_manager.get_idToken()).val()
	if setting_dicts.keys() is None or len(setting_dicts.keys()) < 3:
		node.set(data_mapping, token=firebase_auth_manager.get_idToken())
		return data_mapping
	return setting_dicts

def get_operators():
	node = get_node()
	if node is None:
		return node
	return node.child('operators').get(token=firebase_auth_manager.get_idToken()).val()	

def get_jobs():
	node = get_node()
	if node is None:
		return node
	return node.child('jobs').get(token=firebase_auth_manager.get_idToken()).val()

def update_node(subdir, data):
	node = get_node()
	if node is None:
		return node
	try:
		json = node.child(subdir).update(data, token=firebase_auth_manager.get_idToken())
	except request.extensions.HTTPError as e:
		return e
	return json


