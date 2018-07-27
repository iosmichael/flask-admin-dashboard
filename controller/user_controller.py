#each controller functions will return a user data array along with an action instruction
from .model.user import User

def retrieve_users(page=0):
	pagination = User.query.paginate(page, per_page=20, max_per_page=20, error_out=False)
	users = pagination.items
	pages = pagination.pages
	return (users, pages), "Retrieve Users Successfully"

def display_user():
	users = User.query.limit(20)
	header = ['NAME', 'STATE', 'ZIP', 'DOB', 'SEX', 'PHONE']
	return (header, users), "Display Users Successfully"

def change_query():
	pagination = User.query.order_by('first_name').paginate(page, per_page=20, max_per_page=20, error_out=False)
	users = pagination.items
	pages = pagination.pages
	return (users, pages), "Change Query Successfully"

def count_user():
	return User.query.order_by('first_name').paginate(page, per_page=20, max_per_page=20, error_out=False).total, "Count Userss Successfully"

	#CSV import methods
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

def import_csv():
	path = os.path.abspath(".")
	path = os.path.join(path, "leads.csv")
	with open(path, 'r') as f:
		reader = csv.reader(f)
		content = ""
		num = 0
		index_map = []
		for row in reader:
			if num == 0:
				index_map = map_column_index(row)
				if index_map is None:
					return 'import column error'
			else:
				if len(row) >= 7:
					try:
						db.session.add(User(first_name=row[index_map['first_name']],
							last_name=row[index_map['last_name']],
							state=row[index_map['state']],
							zipcode=row[index_map['zip']],
							dob=row[index_map['dob']],
							sex=row[index_map['sex']],
							phone=row[index_map['phone']]))
					except IntegrityError:
						num += 1
						continue
					db.session.commit()
			num += 1
		return 'success import csv file path: %s' % path
	return 'error'



