import os
from flask import Flask, request, render_template, redirect, url_for, make_response
from admin.controller.main_controller import *
from admin.controller.firebase_controller import *
from admin.extensions import db, firebase_auth, firebase_auth_manager
from admin.routers.database_endpoints import endpoints
from admin.routers.firebase_endpoints import firebase_endpoints
from admin.routers.twilio_endpoints import twilio_endpoints

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////' + os.path.join(basedir, 'database.db')
print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
UPLOAD_FOLDER = './upload'
print(UPLOAD_FOLDER)
app.register_blueprint(endpoints)
app.register_blueprint(firebase_endpoints)
app.register_blueprint(twilio_endpoints)
db.init_app(app)

'''
Static variables
'''
MAX_NUM_PER_PAGE = 20

@app.route('/')
@app.route('/admin')
def index():
    if firebase_auth_manager.is_auth() is False:
        return render_template('login.html')
    return admin()

@app.route('/operators')
def operators():
    setting_dict = get_settings();
    return render_template('operator.html', settings=setting_dict, data=None)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginAuth')
def loginAuth():
    # Log the user in
    email = "x4liu@eng.ucsd.edu"
    password = "00000000"
    if firebase_auth_manager.login(email, password) != "VALID LOGIN":
        return render_template('login.html')
    else:
        return admin()

def admin():
    header = display_visible_headers('User')
    page, _ = paginate('User', MAX_NUM_PER_PAGE)
    users = page.items
    data = {
        "metadata": {},
        "table": { "header": header, "users": users}
    }
    resp = make_response(render_template('index.html', data=data))
    return resp

@app.route('/signup')
def signup():
    return render_template('signup.html')

#file upload api
#TODO: Add a spinner for file being uploaded
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return redirect(url_for('uploaded_file',
                                filename=file.filename))

@app.route('/uploaded_file/<filename>')
def uploaded_file(filename):
    sign, msg = import_csv(filename)
    if sign:
        return 'success'
    else:
        return 'error'

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

def allowed_file(filename):
    ALLOWED_EXTENSIONS = ['csv']
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=5000)
