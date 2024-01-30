from flask import Flask, request, jsonify
import os
#from flask.ext.bcrypt import Bcrypt
from random import choice

from itsdangerous import json
import database_helper

app = Flask(__name__)
# sockets = Sockets(app)
signedInUsers = dict() # Dictionary with key token and value email
userSocketList = dict() # Key: email, value: websocket

host = ''
port = 5000

@app.route('/api')
def api():
    """
    Creates a websocket to disconnect a user when someone else logs in on same account
    """
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        token = ws.receive()

        if token in signedInUsers:
            email = signedInUsers[token]

            if email in userSocketList:
                previous_user = userSocketList[email]
                previous_user.send("logout")

            userSocketList[email] = ws

        while True:
            try:
                ws.receive()
            except:
                return "WEEEE"
    return "REEEEEE"

def generate_token():
    """
    Use random choice to generate random token from all letters and numbers.
    """
    letters = "abcdefghiklmnopqrstuvwwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    token = "".join(choice(letters) for i in range(36))
    return token

def check_token(token):
    """
    Validates a user token
    """
    return token in signedInUsers

def get_token():
    """
    Get the current user token from the Authorization header.
    """
    header = request.headers.get('Authorization')
    if header:
        return header.split(" ")[1]
    else:
        return ''

@app.teardown_request
def after_request(exception):
    database_helper.disconnect_db()

@app.route('/', methods=["GET", 'POST'])
def welcome_view():

    return app.send_static_file('client.html')

@app.route("/sign_in", methods=['POST'])
def sign_in():
    """
    Sign user in if right password is used, if so, create a token and put it in the dictionary of signed in users
    """
    json_request = request.get_json()
    email = json_request['email']
    password = json_request['password']
    res = database_helper.sign_in_user(email, password)
    if res:
        token = generate_token()
        signedInUsers[token] = email
        return jsonify({"token": token}), 200
    else:
        return jsonify({}) , 400

@app.route("/sign_up", methods=['POST'])
def sign_up():
    """
    Creates a new user
    """
    json_request = request.get_json()
    email = json_request['email']
    password = json_request['password']
    firstName = json_request['firstname']
    familyName = json_request['familyname']
    gender = json_request['gender']
    city = json_request['city']
    country = json_request['country']
    if (len(password) >= 6) and email is not None and firstName is not None and familyName is not None and city is not None and country is not None:
        res = database_helper.add_user_to_db(email,password,firstName,familyName,gender,city,country)
        if res:
            return jsonify({}), 201
        else:
            return jsonify({}), 500
    else:
        return jsonify({}), 400

@app.route("/sign_out", methods=['POST'])
def sign_out():
    """
    Retreives token from user and deletes token and user in list so the user logs out
    """
    token = get_token()
    if check_token(token):
        email = signedInUsers[token]
        if email in userSocketList:
            del userSocketList[email]
        del signedInUsers[token]
        return jsonify({}), 200
    else:
        return jsonify({}), 400

@app.route("/change_password", methods=['POST'])
def change_password():
    """
    Changes the password of the current user
    """
    token = get_token()
    old_password = request.json['password']
    new_password = request.json['newpassword']
    email = signedInUsers[token]
    if check_token(token):
        if len(new_password) >= 6 :
            res = database_helper.change_password(email, old_password, new_password)
            if res:
                return jsonify({}), 200
            else:
                return jsonify({}), 401
        else:
            return jsonify({}), 411
    else:
         return jsonify({}), 401

@app.route("/get_user_data_by_token", methods=['GET'])
def get_user_data_by_token():
    """
    Retrievs the user data of the current user
    """
    token = get_token()
    # print(token)
    if check_token(token):
        email = signedInUsers[token]
        user = database_helper.get_user(email)
        if user:
            data = database_helper.get_user_data_by_email(email)
            return jsonify({"data": data}), 200
        else:
            return jsonify({}), 404
    else:
        return jsonify({}), 401

@app.route("/get_user_data_by_email", methods=['POST'])
def get_user_data_by_email():
    """
    Retrievs the user data by the user mail
    """
    email = request.json['email']
    token = get_token()
    user = database_helper.get_user(email)
    if check_token(token):
        if user:
            data = database_helper.get_user_data_by_email(email)
            return jsonify({"data": data}), 200
        else:
            return jsonify({}), 404

    else:
        return jsonify({}), 401

@app.route("/get_user_messages_by_token", methods=['GET'])
def get_user_messages_by_token():
    """
    Retrives messages on the users message board by token
    """
    token = get_token()
    if check_token(token):
        email = signedInUsers[token]
        if database_helper.get_user(email):
            message = database_helper.get_user_messages_by_email(email)
            return jsonify({"data": message}), 200
        else:
            return jsonify({}), 404

    else:
        return jsonify({}), 401



@app.route("/get_user_messages_by_email", methods=['POST'])
def get_user_messages_by_email():
    """
    Retrives messages on the users message board from their email
    """
    email = request.json['email']
    token = get_token()
    if check_token(token):
        if database_helper.get_user(email):
            messages = database_helper.get_user_messages_by_email(email)
            return jsonify({"data": messages}), 200
        else:
            return jsonify({}), 404
    else:
        return jsonify({}), 401

@app.route("/post_message", methods=['POST'])
def post_message():
    """
    Post message on either on the users own page or another persons page by checking what recipient it is
    """
    token = get_token()
    email = signedInUsers[token]
    recipient = request.json['recipient']
    if recipient == "self":
        recipient = signedInUsers[token]

    message = request.json['message']
    if check_token(token):
        res = database_helper.post_message(message, email, recipient)
        if res:
            return jsonify({}), 200
        else:
            return jsonify({}), 404
    else:
        return jsonify({}), 401



if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    print("Running server: " + host + ':' + str(port))
    server = pywsgi.WSGIServer((host, port), app, handler_class=WebSocketHandler)
    server.serve_forever()


