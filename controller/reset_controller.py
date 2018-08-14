from .model.db import db
from .model.user import User
from .model.message import Message
from .model.record import Record
from sqlalchemy.exc import IntegrityError
from .main_controller import *

INIT_STATE = "CREATED"
FINAL_STATE_SUCCESS = "QUALIFIED"
FINAL_STATE_FAILURE = "UNQUALIFIED"
FINAL_STATE_ERROR = "ACTION"


def reset_workflow():
	'''
	there are three stages of workflow: CREATED -> INTRO -> custom tags -> QUALIFIED -> UNQUALIFIED -> ACTION NEEDED
	capable of sending custom message, and capable of turning off auto-reply
	'''
	# db.drop_all()
	# db.create_all()
	states = Message.query.all()
	for state in states:
		db.session.delete(state)
	db.session.commit()
	states = Message.query.all()
	init_state = build_object("Message",{'tag': INIT_STATE})
	final_state_success = build_object("Message", {'tag': FINAL_STATE_SUCCESS})
	final_state_failure = build_object("Message",{'tag': FINAL_STATE_FAILURE})
	final_state_error = build_object("Message",{'tag': FINAL_STATE_ERROR})
	db.session.add(init_state)
	db.session.add(final_state_success)
	db.session.add(final_state_failure)
	db.session.add(final_state_error)
	db.session.commit()

def reset_users():
	'''
	delete all users except the testing one
	'''
	pass

def reset_history():
	'''
	delete all histories
	'''
	db.session.query(Record).delete()
	db.session.commit()

def reset_all():
	'''
	delete all histories except the default workflow
	'''
	db.drop_all()
	db.create_all()
	pass