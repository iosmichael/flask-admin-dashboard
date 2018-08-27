from flask_sqlalchemy import SQLAlchemy
from flask import request
import datetime
from admin.firebase import *

class AuthManager:

	def __init__(self):
		self.uid = None
		self.idToken = None
		self.refreshToken = None
		self.last_update = None

	def login(self, email, password):
		try:
			user = firebase_auth.sign_in_with_email_and_password(email, password)
		except requests.exceptions.HTTPError as e:
			return e
		self.set_uid(user['localId'])
		self.set_idToken(user['idToken'])
		self.set_refreshToken(user['refreshToken'])
		return 'VALID LOGIN'

	def logout(self):
		self.set_uid(None)
		self.set_idToken(None)
		self.set_refreshToken(None)
		self.last_update = None

	def is_auth(self):
		return self.uid != None or self.idToken != None or self.refreshToken != None or self.last_update != None

	def set_uid(self, uid):
		self.uid = uid

	def set_idToken(self, idToken):
		self.idToken = idToken
		self.last_update = datetime.datetime.now()

	def set_refreshToken(self, refreshToken):
		self.refreshToken = refreshToken

	def get_uid(self):
		return self.uid

	def get_idToken(self):
		diff = datetime.datetime.now() - self.last_update
		if diff.total_seconds() / 3600 < 1:
			return self.idToken
		else:
			user = firebase_auth.refresh(self.refreshToken)
			self.idToken = user['idToken']
			self.refreshToken = user['refreshToken']
			return self.idToken

db = SQLAlchemy()
config = {
  "apiKey": "AIzaSyCIBxgb8HhUtKig_oLIDwuYVQ8wkPvrn_k",
  "authDomain": "twillio-919c4.firebaseapp.com",
  "databaseURL": "https://twillio-919c4.firebaseio.com"
}
firebase = initialize_app(config)
firebase_auth = firebase.auth()
firebase_database = firebase.database()
firebase_auth_manager = AuthManager()
