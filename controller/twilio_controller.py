import datetime
from .main_controller import *
from admin.twilio.rest import Client
from admin.twilio.twiml.messaging_response import MessagingResponse
from admin.extensions import firebase_database

ACCOUNT_SID = "ACd2472e0ee6d04299378549ffbfb96b60"
AUTH_TOKEN = "a1ae82e7e6267045be699fd464a7311b"
INIT_STATE = "CREATED"
FINAL_STATE_SUCCESS = "QUALIFIED"
FINAL_STATE_FAILURE = "UNQUALIFIED"
FINAL_STATE_ERROR = "ACTION"
DEFAULT_CARRIER = "+13317041126"

def auto_reply(form):
	answer = form['Body']
	phone = form['From'][2:]
	INFO = create_record(False, phone, DEFAULT_CARRIER, answer)
	user, _ = query_object('User', filters={'phone': phone})
	tag = get_tag(user.tag)
	if tag is not None and is_final(tag) is False:
		next_tag_node = next_tag(answer, tag)
		if next_tag_node is not None:
			update_user_tag(user.id, next_tag_node.tag)
			#twilio api
			INFO = create_record(True, phone, DEFAULT_CARRIER, next_tag_node.content)
			print(INFO)
			return next_tag_node.content
	INFO = create_record(True, phone, DEFAULT_CARRIER, "I will contact with you shortly")
	return "I will contact with you shortly"

def send_msg(user, message):
	if user is None or user.operator == "UNASSIGNED":
		return "CANNOT MANUALLY SEND MESSAGE AT THIS STAGE"
	record = create_record(user.phone, user.operator, message, False)
	print("successfully created record: {}".format(str(record.id)))
	data = {
		"phone": user.phone,
		"operator": user.operator,
		"content": message,
		"last_update": datetime.datetime.now().strftime('%H:%M:%S %m/%d/%Y'),
		"tag": "MANUAL",
		"record_id": record.id
	}
	firebase_database.child('/jobs').push(data)
	print('successfully pushed job into firebase')
	return "SUCCESS"

def create_record(phone, operator, content, is_client=False):
	record_data = {
		'operator': operator, 
		'phone': phone, 
		'content': content, 
		'is_client': is_client,
		'time': datetime.datetime.now()
	}
	record = build_object('Record', record_data)
	print(record)
	record, _ = add_object('Record', record)
	return record
