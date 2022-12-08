from server import app
from flask_sqlalchemy import SQLAlchemy
import os
from functools import wraps
from flask import Flask, render_template, request, jsonify, abort

from flask_bcrypt import Bcrypt

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jti,
    get_jwt_identity, get_current_user, get_raw_jwt, decode_token
)

if 'NAMESPACE' in os.environ and os.environ['NAMESPACE'] == 'heroku':
    db_uri = os.environ['DATABASE_URL']
    debug_flag = False
else:  # when running locally with sqlite
    db_path = os.path.join(os.path.dirname(__file__), 'app.db')
    db_uri = 'sqlite:///{}'.format(db_path)
    debug_flag = True

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
app.config['JWT_SECRET_KEY'] = 'ganska_hemlig'
app.config['JWT_ACCES_TOKEN_EXPIRES'] = 604800
jwt = JWTManager(app)


def token_required(f):
    """
    Token that login person, using token as ID to the person when logged in
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'access_token' in request.headers:
            token = request.headers['access_token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        if not check_if_token_valid(token):
            return jsonify({'message': 'Token is invalid!'}), 401

        try:
            current_user = decode_token(token, None, False)['identity']
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)
    return decorated

######################################################
################## Purchase Things ###################
######################################################


def new_purchase(group, buyer, loaner, amount):
    """
    Locates if buyer and loaner is in same group.
    Then add amount of beverages that buyer has supplied
    and subtract same amount to the loaner
    """
    buyer_relation = db.session.query(Relation).filter_by(
        user_id=buyer, group_id=group).first()
    loaner_relation = db.session.query(Relation).filter_by(
        user_id=loaner, group_id=group).first()

    buyer_relation.user_status += amount
    loaner_relation.user_status -= amount

    db.session.commit()
    return True

######################################################
################### Comment Things ###################
######################################################


class Message(db.Model):
    """
    Provides information when you message a person in
    their profile in group
    """
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    message_id = db.Column(db.String, unique=True)
    message = db.Column(db.String, nullable=False, unique=False)
    location = db.Column(db.String, nullable=False, unique=False)
    amountOfLikes = db.Column(db.Integer, nullable=False)

    def __init__(self, message_id, message, location, amountOfLikes):
        self.message_id = message_id
        self.message = message
        self.location = location
        self.amountOfLikes = amountOfLikes

    def format_to_dict_with_liked(self, liker):
        """
        Helping function to get a dictionary containing if it has been
        liked by a given user
        """
        temp = db.session.query(MessageLikeRelation).filter_by(
            user_id=liker, message_id=self.message_id).first()
        isLiked = (temp != None)

        return {"postId": self.message_id, "message": self.message,
                "location": self.location, "amountOfLikes": self.amountOfLikes,
                "likedByMe": isLiked}


class MessageUserOriginRelation(db.Model):
    """
    Contains info where a specific message is posted
    """
    __tablename__ = "messageUserOriginRelation"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    message_id = db.Column(db.String, unique=True, nullable=False)
    user_id = db.Column(db.String, nullable=False)
    group_id = db.Column(db.String, nullable=False)

    def __init__(self, message_id, user_id, group_id):
        self.message_id = message_id
        self.user_id = user_id
        self.group_id = group_id


class MessageLikeRelation(db.Model):
    """
    Contains info where a specific like is posted
    """
    __tablename__ = "likeRelation"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.String, nullable=False)
    message_id = db.Column(db.String, nullable=False)

    def __init__(self, user_id, message_id):
        self.user_id = user_id
        self.message_id = message_id


def get_comments_on_user(current_user, groupname, username):
    """
    Get all post on a person in specific group
    """
    comments = []
    comment_ids_user = db.session.query(MessageUserOriginRelation.message_id).filter_by(
        user_id=username, group_id=groupname).all()
    for comment_id in comment_ids_user:
        comment = db.session.query(Message).filter_by(
            message_id=comment_id[0]).first()
        comments.append(comment.format_to_dict_with_liked(current_user))

    return comments


def post_comment_on_user(commentID, groupname, username, location, message):
    """
    Adds a post to the given user and makes sure it is specific for
    a given group. The likes on the message is set to 0
    """
    message_info = Message(commentID, message, location, 0)
    user_origin = MessageUserOriginRelation(commentID, username, groupname)

    db.session.add(message_info)
    db.session.add(user_origin)
    db.session.commit()

    return True


def like_user_comment_by_id(current_user, commentID):
    """
    Adds a like on the designated persons post
    """
    message = db.session.query(Message).filter_by(message_id=commentID).first()
    message.amountOfLikes += 1
    add_like = MessageLikeRelation(current_user, commentID)
    db.session.add(add_like)
    db.session.commit()
    return True


def dislike_user_comment_by_id(current_user, commentID):
    """
    Adds a dislike on the designated persons post
    """
    message
    message = db.session.query(Message).filter_by(message_id=commentID).first()
    message.amountOfLikes -= 1

    db.session.query(MessageLikeRelation).filter_by(
        user_id=current_user, message_id=commentID).delete(synchronize_session='fetch')
    db.session.commit()


class Relation(db.Model):
    """
    contains info of users and their status of what group they are in
    """
    __tablename__ = "relation"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    group_id = db.Column(db.String)
    user_id = db.Column(db.String)
    user_status = db.Column(db.Integer)

    def __init__(self, group_name, user_id):
        self.group_id = group_name
        self.user_id = user_id
        self.user_status = 0

    def format_user_stats(self):
        return {"username": self.user_id, "user_status": self.user_status}


######################################################
##################  Group Things #####################
######################################################


class Group(db.Model):
    """
    Contains group name
    """
    __tablename__ = "group"
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, group_name):
        self.group_name = group_name

    def to_dict(self):
        return {
            "group": self.group_name
        }


def create_group(new_groupname, creater):
    """
    creates a new group, person who created is always included
    """
    temp = db.session.query(Group).filter_by(group_name=new_groupname).first()
    if temp != None:
        return False
    add_person_to_group(new_groupname, creater)
    new_group = Group(new_groupname)
    db.session.add(new_group)
    db.session.commit()
    return True


def add_person_to_group(group_id, user):
    """
    Adds a person to designated group
    """
    add_user = Relation(group_id, user)
    db.session.add(add_user)
    db.session.commit()
    return True


def view_group_users(group):
    """
    return useres in a group
    """
    grp_user = []
    user_ids_in_group = db.session.query(
        Relation.user_id).filter_by(group_id=group).all()
    for user_id in user_ids_in_group:
        username = db.session.query(User).filter_by(
            username=user_id[0]).first()
        grp_user.append(username.to_dict())
    return grp_user


def view_group_status(groupname):
    """
    return username and how many beverages user owes or how many
    people owes him
    """
    all_relations = db.session.query(
        Relation).filter_by(group_id=groupname).all()
    usr_status = []
    for relation in all_relations:
        usr_status.append(relation.format_user_stats())
    return usr_status


def view_users_group(user):
    """
    return what groups user is a member of
    """
    temp = db.session.query(Relation).filter_by(user_id=user).first()
    user_grp = []
    relations = db.session.query(Relation).filter_by(user_id=user).all()
    for relation in relations:
        group = db.session.query(Group).filter_by(
            group_name=relation.group_id).first()
        user_grp.append(group.to_dict())
    return user_grp


# NOT USED, POSSIBLE FUTURE WORK
"""
#delete person from group
def delete_from_group(group, user):
    db.session.query(Relation).filter_by(group_id = group, user_id = user).delete()
    db.session.commit()
    return True

#add person in a group
def users_not_in_group(group, creater):
    users_not_members = []
    user_ids_in_group = db.session.query(Relation.user_id).filter_by(group_id = group).all()
    users = db.session.query(User.username).all()
    for user_id in user_ids_in_group:
        if user_id[0] in users:
            users.remove(user_id[0])
    users.remove(creater)
    return users

"""


###################################################
################# User things #####################
###################################################


class User(db.Model):
    """
    contains info for a user with a hashed-password
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    passw_hash = db.Column(db.String(200), unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.passw_hash = bcrypt.generate_password_hash(password).decode(
            'utf-8')

    def to_dict(self):
        return {
            "username": self.username
        }


def register_user(user_name, password):
    """
    registers new user
    """
    temp = db.session.query(User).filter_by(username=user_name).first()
    if temp != None:
        return False
    new_user = User(user_name, password)
    db.session.add(new_user)
    db.session.commit()
    return True


def get_all_users(creator):
    """
    Get all user in database
    """
    users = []
    remove_creator = db.session.query(User).filter_by(
        username=creator).first().to_dict()
    for usr in db.session.query(User).all():
        users.append(usr.to_dict())
    users.remove(remove_creator)
    return users


def login_user(user_name, password):
    """
    logins the user if provided correct password,
    created as unique token for ID
    """
    user = db.session.query(User).filter_by(
        username=user_name).first()
    if user == None:
        return jsonify("{'Error':'No such user'}"), 400

    if bcrypt.check_password_hash(user.passw_hash, password):
        token = create_access_token(identity=user.username)
        return jsonify(access_token=token), 200
    return jsonify("{'Error':'Wrong password'}"), 400


###################################################
############### initialize database ###############
###################################################

def init_db():
    """
    resets database
    """
    db.drop_all()
    db.create_all()
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
