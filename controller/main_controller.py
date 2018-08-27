'''
this is the main controller that provides the general orm mapping to all different tables
'''
import os, csv
from admin.extensions import db
from admin.model.user import User
from admin.model.message import Message
from admin.model.record import Record
from sqlalchemy.exc import IntegrityError

UPLOAD_FOLDER = '/tmp/flask/upload'
ERROR_MESSAGE = "ERROR ---"
SUCCESS_MESSAGE = "SUCCESS ---"

table_mapping_objects = {
	"User": User,
	"Message": Message,
	"Record": Record
}

table_mapping_headers = {
	"User": ['NAME', 'STATE', 'ZIP', 'DOB', 'SEX', 'PHONE'],
	"Message": ['NAME','TRUE TAG', 'FAL TAG','EL TAG', 'CONTENT']
}

table_mapping_keys = {
	"User": ['first_name', 'last_name', 'zipcode', 'state', 'dob', 'sex', 'phone', 'tag'],
	"Message": ['tag','content','tru_indicator','fal_indicator','tru_tag', 'fal_tag','el_tag'],
	"Record": ['carrier', 'phone', 'content', 'receive']
}

def form_validation(table, form):
	if len(form) == 0:
		return False
	for key in form.keys():
		if key not in table_mapping_keys[table]:
			return False
	return True

'''
this is a method that takes a table and perform pagination on it
the method returns two parts: object array/arrays and a error message
'''
def paginate(table, max_num_page, page=1, criterion=[]):
	if table in table_mapping_objects.keys():
		pagination = db.session.query(table_mapping_objects[table]).order_by(*criterion).paginate(page, per_page=max_num_page, max_per_page=max_num_page, error_out=False)
		return pagination, SUCCESS_MESSAGE
	return None, ERROR_MESSAGE

def paginate_with_filters(table, max_num_page, page=1, filters={}, criterion=[]):
	if table in table_mapping_objects.keys():
		pagination = db.session.query(table_mapping_objects[table]).filter_by(**filters).order_by(*criterion).paginate(page, per_page=max_num_page, max_per_page=max_num_page, error_out=False)
		return pagination, SUCCESS_MESSAGE
	return None, ERROR_MESSAGE

def query_object(table, filters={}):
	if table in table_mapping_objects.keys():
		items = db.session.query(table_mapping_objects[table]).filter_by(**filters)
		if items.count() >= 0:
			return items.first(), SUCCESS_MESSAGE
		return items.one_or_none(), SUCCESS_MESSAGE
	return None, ERROR_MESSAGE

def query_all(table, filters={}):
	if table in table_mapping_objects.keys():
		items = db.session.query(table_mapping_objects[table]).filter_by(**filters)
		return items.all(), SUCCESS_MESSAGE
	return None, ERROR_MESSAGE

'''
total pages shown on the page is 5
'''
def get_pages(max_page, current_page, min_page=1):
	if current_page <= 3:
		return [i for i in range(1,6)]
	if current_page >= max_page-2:
		return [i for i in range(max_page-4, max_page+1)]
	return [i for i in range(current_page-2, current_page+ 3)]

'''
this function returns the visible header displayed in the header
'''
def display_visible_headers(table):
	if table in table_mapping_headers.keys():
		return table_mapping_headers[table]
	return None

def build_object(table, data):
	if form_validation(table, data) is False:
		return None
	if table in table_mapping_objects.keys():
		return table_mapping_objects[table](**data)
	return None

'''
this function add a single object in a table
'''
def add_object(table, item):
	db.session.add(item)
	try:
		db.session.commit()
		return item, SUCCESS_MESSAGE
	except IntegrityError as e:
		db.session.rollback()
		return item, e

'''
this function add a bulk of objects in a table
'''
def add_multi_object(table, items):
	db.session.add_all(items)
	db.session.commit()
	return items, SUCCESS_MESSAGE

def update_object(table, uid, info):
	if form_validation(table, info) is False:
		return 'INVALID FORM'
	if table in table_mapping_objects.keys():
		item = db.session.query(table_mapping_objects[table]).get(uid)
		item.update(**info)
		db.session.add(item)
		db.session.commit()
		return SUCCESS_MESSAGE
	return ERROR_MESSAGE

'''
this function drops a single object in a table
'''
def drop_object(item):
	db.session.delete(item)
	db.session.commit()
	return SUCCESS_MESSAGE

'''
this function drops a bulk of objects in a table
'''
def drop_multi_objects(items):
	for item in items:
		db.session.delete(item)
	db.session.commit()
	return SUCCESS_MESSAGE
	# return ERROR_MESSAGE

''' 
this function provides essential import methods
'''
def map_column_index(row):
	try:
		index = {
			'first_name':row.index('first_name'),
			'last_name':row.index('last_name'),
			'state':row.index('state'),
			'zip':row.index('zip'),
			'dob':row.index('dob'),
			'sex':row.index('sex'),
			'phone':row.index('phone')
		}
		return index
	except ValueError:
		return None

def data_column_map(row, index_map):
	return {
		'first_name':row[index_map['first_name']],
		'last_name':row[index_map['last_name']],
		'state':row[index_map['state']],
		'zipcode':row[index_map['zip']],
		'dob':row[index_map['dob']],
		'sex':row[index_map['sex']],
		'phone':row[index_map['phone']]
	}

def import_csv(filename):
	path = os.path.join(UPLOAD_FOLDER, filename)
	with open(path, 'r') as f:
		reader = csv.reader(f)
		content = ""
		num = 0
		index_map = {}
		for row in reader:
			if num == 0:
				index_map = map_column_index(row)
				if index_map is None:
					return False, 'import column error'
			else:
				if len(row) >= 7:
					item = build_object('User', data_column_map(row, index_map))
					INFO = add_object('User', item)
			num += 1
		return True, 'success import file path: %s' % path
	return False, 'error'
