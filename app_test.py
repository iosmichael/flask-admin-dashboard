import json
import os
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from .controller.model.db import db
from .controller.main_controller import *
from .controller.model.user import User
from .controller.twilio_controller import *
from .controller.reset_controller import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = '/tmp/flask/upload'
db.init_app(app)

UID = 11

def sample_data(num):
    return {
        'tag': 'tag_'+str(num), 
        'content': 'content_'+str(num),
        'tru_indicator': 'tru_indicator_'+str(num),
        'fal_indicator': 'fal_indicator_'+str(num),
        'tru_tag': 'tru_tag_'+str(num),
        'fal_tag': 'fal_tag_'+str(num),
        'el_tag': 'el_tag_'+str(num)
    }

def build_work_flow():
    step1 = {
        'tag': INIT_STATE, 
        'content': 'content_6',
        'tru_indicator': 'tru_indicator_6',
        'fal_indicator': 'fal_indicator_6',
        'tru_tag': 'tru_tag_6',
        'fal_tag': FINAL_STATE,
        'el_tag': ACTION_STATE
    }

    step2 = {
        'tag': 'tru_tag_6', 
        'content': 'content_12',
        'tru_indicator': 'tru_indicator_12',
        'fal_indicator': 'fal_indicator_12',
        'tru_tag': ACTION_STATE,
        'fal_tag': FINAL_STATE,
        'el_tag': ACTION_STATE
    }

    msg1 = build_object("Message", step1)
    add_object("Message", msg1)
    msg2 = build_object("Message", step2)
    add_object("Message", msg2)
    return 'Success'

def request_in(uid):
    user, _ = query_object('User', filters= {'id':uid})
    print(user)
    return {
        'Body': 'Yes is my answer',
        'Phone': user.phone,
        'UID': uid
    }

def test_auto_reply():
    data = request_in(UID)
    print(update_object('User', UID, {'tag': INIT_STATE}))
    INFO, phone = auto_reply(data)
    print(INFO, phone)
    records, _ = paginate_with_filters("Record", 100, filters={"phone": phone}, criterion=['time'])
    user, _ = query_object('User', filters= {'id': UID})

def find_tag():
    tag, _ = query_object('Message', filters={"tag": INIT_STATE})
    return tag

def find_tags():
    tags, _ = paginate_with_filters("Message", 20)
    for tag in tags.items:
        print(tag)
        print(tag.tag)
        print(tag.content)

with app.test_request_context():
    # test_auto_reply()
    # auto_reply({
    #     'Body': 'Yes is my answer',
    #     'Phone': '9549295555'
    #     })
    # records, _ =query_all('Record', filters={'phone':'9549295555'})
    # for record in records:
    #     print(record)
    # update_object('Message', 5, {'content': 'change to this'})
    # uid = 5
    # obj, _ = query_object('Message', filters={'id':uid})
    # print(drop_object(obj))
    # for user in users:
    #     print(user.tag)
    # print(find_tags())
    reset_all()
    reset_workflow()
    exit(0)
