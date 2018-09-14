import datetime
from admin.controller.main_controller import *
from admin.twilio.rest import Client
from admin.twilio.twiml.messaging_response import MessagingResponse
from admin.extensions import firebase_database

ACCOUNT_SID = "ACd2472e0ee6d04299378549ffbfb96b60"
AUTH_TOKEN = "a1ae82e7e6267045be699fd464a7311b"

def auto_reply(form):
	answer = form['Body']
	phone = form['From'][2:]
	user, _ = query_object('User', filters={'phone': phone})
	INFO = create_record(False, phone, user.operator, answer)
	if user.tag in ["POSITIVE", "NEGATIVE"]:
		return
	negative_indicator = firebase_database.child('/setting/replyIndicator').get().val()
	negative_tokens = [word.strip() for word in negative_indicator.split(",")]
	for token in negative_tokens:
		if token in answer:
			update_object('User', user.id, {"tag": "NEGATIVE"})
			return
	update_object('User', user.id, {"tag": "POSITIVE"})
	return

def send_msg(user, message):
	if user is None or user.operator == "UNASSIGNED":
		return "CANNOT MANUALLY SEND MESSAGE AT THIS STAGE"
	record = create_record(user.phone, user.operator, message, False)
	client = Client(ACCOUNT_SID, AUTH_TOKEN)
	msg = client.messages.\
	create(
    	to="+1"+'8157612213',
    	body=message,
    	from_="+1"+'3317041126'
    )
	return "SUCCESS"

def create_record(phone, operator, content, is_client=False):
	record_data = {
		'operator': operator, 
		'phone': phone, 
		'content': content, 
		'is_client': is_client,
		'time': datetime.datetime.now(),
		'delivered': True
	}
	record = build_object('Record', record_data)
	print(record)
	record, _ = add_object('Record', record)
	return record
