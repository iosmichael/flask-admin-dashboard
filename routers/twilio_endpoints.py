import json
import os
from flask import Blueprint, request
from admin.controller.twilio_controller import *

twilio_endpoints = Blueprint('twilio_endpoints', __name__, template_folder='templates')

#Twillio Endpoints
@twilio_endpoints.route("/twilio/send", methods=['GET', 'POST'])
def send_custom():
    if 'phone' in request.form.keys():
        if 'message' in request.form.keys():
            return send_msg(request.form['phone'], request.form['message'])
    return 'Custom Message Does Not Send'

@twilio_endpoints.route("/twilio", methods=['GET', 'POST'])
def reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()
    resp.message(auto_reply(request.form))
    return str(resp)