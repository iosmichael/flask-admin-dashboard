from .user import User

mapping = {
	'first_name':User.first_name,
	'last_name':User.last_name,
	'gender':User.sex,
	'state':User.state,
	'zip':User.zipcode,
	'phone':User.phone
}

# parser.add_argument('-t', action='table tag', type=str)

#this method takes a series of command and translate them into query
def cmd(exec_line):
	desc = []
	for key in results.keys():
		desc.append(key + ": "+results[key])
	return (", \n").join(desc)