from flask import Flask, request, jsonify
from random import choice
import database_helper

app = Flask(__name__)
signedInUsers = dict() #Dictionary with key token and value email

def generate_token():
    """
    Use random choice to generate random token from all letters and numbers.
    """
    letters = "abcdefghiklmnopqrstuvwwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    token = "".join(choice(letters) for i in range(36))
    return token

def check_token(token):
    """
    If token is in dictionary return True
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

@app.route("/")
def hello_word():
    return "<p>Hello world!!!</p>"

@app.route("/sign_in", methods=['POST'])
def sign_in():
    email = request.json['email']
    password = request.json['password']
    res = database_helper.sign_in_user(email, password)
    if res:
        token = generate_token()
        signedInUsers[token] = email
        return jsonify({"token": token}), 200

    else:
        return jsonify({}) , 400

@app.route("/sign_up", methods=['POST'])
def sign_up():
    email = request.json['email']
    password = request.json['password']
    firstName = request.json['firstname']
    familyName = request.json['familyname']
    gender = request.json['gender']
    city = request.json['city']
    country = request.json['country']
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
    token = get_token()
    if check_token(token):
        del signedInUsers[token]
        return jsonify({}), 200
    else:
        return jsonify({}), 400

@app.route("/change_password", methods=['POST'])
def change_password():
    token = get_token()
    old_password = request.json['password']
    new_password = request.json['newpassword']
    email = request.json['email']
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
    token = get_token()
    print(token)
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

@app.route("/get_user_data_by_email", methods=['GET'])
def get_user_data_by_email():
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


@app.route("/get_user_messages_by_email", methods=['GET'])
def get_user_messages_by_email():
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
    email = request.json['email']
    token = get_token()
    recipient = request.json['recipient']
    message = request.json['message']
    if check_token(token):
        res = database_helper.post_message(message, email, recipient)
        if res:
            return jsonify({}), 200
        else:
            return jsonify({}), 404
    else:
        return jsonify({}), 401
