import json
import os
from flask import Flask, request, render_template, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
from .controller.main_controller import *
from admin.extensions import db, firebase_auth, firebase_auth_manager
from admin.routers.database_endpoints import endpoints
from admin.routers.firebase_endpoints import firebase_endpoints
from admin.routers.twilio_endpoints import twilio_endpoints

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = '/tmp/flask/upload'
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
    return render_template('operator.html', data=None)

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

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=5000)
