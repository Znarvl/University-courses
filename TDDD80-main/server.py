from data_handler import token_required
import data_handler
from flask import Flask, render_template, request, jsonify, abort
import uuid


def create_id():
    """
    creates a uuid for message
    """
    id = uuid.uuid4().hex
    return str(id)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

###################################################
################ Groups ###########################
###################################################


@app.route('/group', methods=['POST'])
@token_required
def create_group(current_user):
    """
    route that calls on data_handler to form a new group,
    current_user always in group
    """
    group = request.json["group"]
    if not data_handler.create_group(group, current_user):
        return "Group name already taken", 404
    else:
        return jsonify({"group": group})


@app.route('/group/<group_id>/add/<username>', methods=['POST'])
def add_person_to_group(group_id, username):
    if not data_handler.add_person_to_group(group_id, username):
        return "Group or name does not exist", 404
    else:
        return " ", 200


@app.route('/group/purchase/add', methods=['POST'])
@token_required
def add_purchase(current_user):
    """
    extract values from json object to provide data_handler
    with info of how many beer on person owes in group
    """
    buyer = current_user
    loaner = request.json['username']
    group = request.json['groupname']
    amount = request.json['amount']

    data_handler.new_purchase(group, buyer, loaner, amount)
    return " ", 200


@app.route('/group/username', methods=['GET'])
@token_required
def user_get_group(current_user):
    user_grp = data_handler.view_users_group(current_user)
    return jsonify({"groups": user_grp})


@app.route('/group/users/<group>', methods=['GET'])
def group_get_user(group):
    grp_user = data_handler.view_group_users(group)
    return jsonify({"users": grp_user})


@app.route('/group/<group_name>/status', methods=['GET'])
def view_user_status(group_name):
    """
    returns all users status in group with how many
    beverages they owes or how many people owe them
    """
    status = data_handler.view_group_status(group_name)
    return jsonify({"relations": status})

###################################################
################ Message ##########################
###################################################


@app.route('/<groupname>/comment/<username>', methods=['GET'])
@token_required
def get_comment(current_user, groupname, username):
    """
    route that calls on data_handler to get all
    post on a person in specific group
    """
    comments = data_handler.get_comments_on_user(
        current_user, groupname, username)
    return jsonify({"comments": comments})


@app.route('/group/comment/username', methods=['POST'])
@token_required
def post_comment(current_user):
    """
    extracts values from json object to the data_handler
    """
    commentId = create_id()
    groupname = request.json['groupName']
    username = request.json['userName']
    location = request.json['location']
    message = request.json['message']
    data_handler.post_comment_on_user(
        commentId, groupname, username, location, message)
    return jsonify({"": ""}), 200


@app.route('/group/comment/like/<commentId>', methods=['POST'])
@token_required
def like_comment(current_user, commentId):
    data_handler.like_user_comment_by_id(current_user, commentId)
    return " ", 200


@app.route('/group/comment/dislike/<commentId>', methods=['POST'])
@token_required
def dislike(current_user, commentId):
    data_handler.dislike_user_comment_by_id(current_user, commentId)
    return " ", 200


###################################################
################# User things #####################
###################################################

@app.route('/user', methods=['POST'])
def new_user():
    """
    extract values from json object to provide a new user to
    data_handler
    """
    user = request.json['username']
    password = request.json['password']
    if not data_handler.register_user(user, password):
        return "Username already taken", 404
    else:
        return jsonify({"username": user})


@app.route('/user', methods=['GET'])
@token_required
def user_get_all(current_user):
    all_user = data_handler.get_all_users(current_user)
    return jsonify({"users": all_user})


@app.route('/login', methods=['POST'])
def login():
    user = request.json['username']
    password = request.json['password']
    return data_handler.login_user(user, password)


###################################################
############### initialize database ###############
###################################################

@app.route('/init_db')
def init_db():
    data_handler.init_db()
    return ""
