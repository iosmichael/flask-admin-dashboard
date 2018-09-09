import json
import datetime
import os, sys
from flask import Flask, request, render_template, redirect, url_for
from admin.extensions import firebase_database, firebase_auth_manager
from admin.controller.reset_controller import *

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, '/upload')
db.init_app(app)

with app.app_context():
	reset_all()
	sys.exit('Terminated')