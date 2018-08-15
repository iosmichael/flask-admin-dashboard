import json
import os
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from .controller.model.db import db
from .controller.main_controller import *
from .controller.twilio_controller import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = '/tmp/flask/upload'
db.init_app(app)

'''
Static variables
'''
MAX_NUM_PER_PAGE = 20

@app.route('/')
@app.route('/admin')
def admin():
    header = display_visible_headers('User')
    page, _ = paginate('User', MAX_NUM_PER_PAGE)
    users = page.items
    tags = tag_options()
    return render_template('dashboard/index.html', header=header, users=users, tags = tags)

@app.route('/settings')
def settings():
    header = display_visible_headers('Message')
    page, _ = paginate('Message', MAX_NUM_PER_PAGE)
    messages = page.items
    tags = tag_options(exclude_created=True)
    return render_template('workflow/index.html', header=header, messages=messages, tags = tags)

#API Endpoints - DATA

@app.route('/page/<name>/<page>', methods=['POST'])
def paginator(name, page):
    page, _ = paginate_with_filters(name, MAX_NUM_PER_PAGE, page=int(page), filters={'tag':request.form['tag']})
    print(page)
    objs = page.items
    obj_dicts = [obj.as_dict() for obj in objs]
    package = { "metadata": None, "items": obj_dicts}
    return json.dumps(package)

@app.route('/search/<name>/<uid>')
def search(name, uid):	
    obj, _ = query_object(name, filters={'id':uid})
    return json.dumps(obj.as_dict())

#API Endpoints - INDICATION

@app.route('/update/<name>/<uid>', methods=['POST'])
def update(name, uid):    
    print(request.form.to_dict())
    INFO = update_object(name, uid, request.form.to_dict())
    return INFO

@app.route('/delete/<name>/<uid>', methods=['POST'])
def delete(name, uid):
    obj, _ = query_object(name, filters={'id':uid})
    INFO = drop_object(obj)
    return INFO

@app.route('/add/<name>', methods=['POST'])
def create(name):
    obj = build_object(name, request.form.to_dict())
    if obj is None:
        return 'Invalid Form'
    _, INFO = add_object(name, obj)
    return INFO

@app.route('/all/<phone>')
def query_records(phone):
    records, _ = query_all('Record', filters={'phone': phone})
    record_dicts = [record.as_dict() for record in records]
    return json.dumps(record_dicts)

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
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return redirect(url_for('uploaded_file',
                                filename=file.filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    sign, msg = import_csv(filename)
    if sign:
        return 'success'
    else:
        return 'error'

def allowed_file(filename):
    ALLOWED_EXTENSIONS = ['csv']
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Twillio Endpoints
@app.route("/send", methods=['GET', 'POST'])
def send_custom():
    if 'phone' in request.form.keys():
        if 'message' in request.form.keys():
            return send_msg(request.form['phone'], request.form['message'])
    return 'Custom Message Does Not Send'

@app.route("/twilio", methods=['GET', 'POST'])
def reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()
    resp.message(auto_reply(request.form))
    return str(resp)

# @app.route('/admin/recover')
# def recover_db():
#     db.drop_all()
#     db.create_all() 
#     admin()


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=5000)