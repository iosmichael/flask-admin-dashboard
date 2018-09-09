import json
import os
from flask import Blueprint, request, url_for, redirect
from admin.extensions import db
from admin.controller.main_controller import *

#API Endpoints - DATA
endpoints = Blueprint('endpoints', __name__, template_folder='templates')

UPLOAD_FOLDER = '/tmp/flask/upload'
MAX_NUM_PER_PAGE = 20

@endpoints.route('/page/<name>/<page>', methods=['POST'])
def paginator(name, page):
    page, _ = paginate_with_filters(name, MAX_NUM_PER_PAGE, page=int(page), filters={'tag':request.form['tag']})
    print(page)
    objs = page.items
    obj_dicts = [obj.as_dict() for obj in objs]
    package = { "metadata": None, "items": obj_dicts}
    return json.dumps(package)

@endpoints.route('/search/<substring>', methods=['POST'])
def search_by_substring(substring):
    objs = query_user_with_substring(substring, is_number = substring.isdigit(), LIMIT_NUM = 20)
    obj_dicts = [obj.as_dict() for obj in objs]
    package = {"metadata":None, "items": obj_dicts}
    return json.dumps(package)

@endpoints.route('/search/<name>/<uid>')
def search(name, uid):	
    obj, _ = query_object(name, filters={'id':uid})
    return json.dumps(obj.as_dict())

#API Endpoints - INDICATION

@endpoints.route('/update/<name>/<uid>', methods=['POST'])
def update(name, uid):    
    print(request.form.to_dict())
    INFO = update_object(name, uid, request.form.to_dict())
    return INFO

@endpoints.route('/delete/<name>/<uid>', methods=['POST'])
def delete(name, uid):
    obj, _ = query_object(name, filters={'id':uid})
    INFO = drop_object(obj)
    return INFO

@endpoints.route('/add/<name>', methods=['POST'])
def create(name):
    obj = build_object(name, request.form.to_dict())
    if obj is None:
        return 'Invalid Form or Duplicate Data Entry'
    _, INFO = add_object(name, obj)
    return INFO

@endpoints.route('/all/<phone>')
def query_records(phone):
    records, _ = query_all_with_order('Record', filters={'phone': phone}, criterion='time')
    record_dicts = [record.as_dict() for record in records]
    return json.dumps(record_dicts)

#file upload api
#TODO: Add a spinner for file being uploaded
@endpoints.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return redirect(url_for('endpoints.uploaded_file',
                                filename=file.filename))

@endpoints.route('/uploaded_file/<filename>')
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