import json
import os
from flask import Blueprint, request, url_for, redirect
from admin.extensions import db
from admin.controller.main_controller import *

#API Endpoints - DATA
endpoints = Blueprint('endpoints', __name__, template_folder='templates')

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

@endpoints.route('/summary')
def summary():
    summary_dict = {
    'new': 250,
    'positive':5,
    'negative':5,
    'archived':0
    }
    return json.dumps(summary_dict)