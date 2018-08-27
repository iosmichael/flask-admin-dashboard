from .main_controller import *
from admin.twilio.rest import Client
from admin.twilio.twiml.messaging_response import MessagingResponse

ACCOUND_SID = "ACd2472e0ee6d04299378549ffbfb96b60"
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

def send_msg(phone, message):
	#twilio api
	'''
	client = Client(ACCOUND_SID, AUTH_TOKEN)
	msg = client.messages.\
	create(
    	to="+1"+phone,
    	body=message,
    	from_=DEFAULT_CARRIER
    )
    '''
	create_record(True, phone, DEFAULT_CARRIER, message)
	return message

'''
'''
def get_tag(tag_name):
	print("GET_TAG: ", tag_name)
	tag, _ = query_object('Message', filters={'tag': tag_name})
	print(tag)
	return tag

def next_tag(answer, tag):
	'''
	answer is request.form['Body']
	next tag
	'''
	if tag.tru_indicator in answer:
		next_tag, _ = query_object('Message', filters={'tag': tag.tru_tag})
		return next_tag 
	elif tag.fal_indicator in answer:
		next_tag, _ = query_object('Message', filters={'tag': tag.fal_tag})
		return next_tag
	next_tag, _ = query_object('Message', filters={'tag': tag.el_tag})
	return next_tag

def update_user_tag(uid, tag_name):
	INFO = update_object('User', uid, {'tag': tag_name})
	return INFO

'''
utility functions
'''
def tag_options(exclude_created = False):
	pages, _ = paginate('Message', 100)
	if exclude_created:
		return [tag for tag in pages.items if tag.tag != 'CREATED']
	return pages.items

def is_final(tag):
	return tag.tag in [FINAL_STATE_SUCCESS, FINAL_STATE_FAILURE, FINAL_STATE_ERROR]

def create_record(is_bot, caller, carrier, content):
	record = build_object('Record', {
		'carrier': carrier,
		'phone': caller,
		'content': content,
		'receive': is_bot
		})
	record, INFO = add_object('Record', record)
	return INFO
