import sqlite3
from flask import g
from server import app
from flask_bcrypt import Bcrypt
import os
DATABASE = 'database.db'

bcrypt = Bcrypt(app)



def get_db():
    db = getattr(g, 'db', None)
    if db is None:
            db = g.db = sqlite3.connect(DATABASE)
    return db


def disconnect_db():
    db = getattr(g, 'db', None)
    if db is not None:
        g.db.close()


def add_user_to_db(email, password, firstname, familyname, gender, city, country):
    try:
        #pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        get_db().execute("insert into users values(?,?,?,?,?,?,?)", [email, password, firstname, familyname, gender, city, country])
        get_db().commit()
        return True
    except sqlite3.Error as e:
        print("Database error: %s" % e)
        return False
    except Exception as e:
        print("Exception in _query: %s" % e)
        return False

def sign_in_user(login_email, password):
    try:
        # salt = '' #TODO
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("select password from users where email = ?", [login_email])
        psw = cursor.fetchone()[0]
        #hashed_password = bcrypt.check_password_hash(psw, password) # returns True

        if psw == password:
            return True
    except sqlite3.Error as e:
        print("Database error: %s" % e)
        return False
    except Exception as e:
        print("Exception in _query: %s" % e)
        return False


def get_user_data_by_email(email):
    try:
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("select email, firstname, familyname, gender, city, country from users where email = ?", [email])
        row = cursor.fetchall()[0]
        data = {'email': row[0], 'firstname':row[1], 'familyname': row[2], 'gender': row[3],
             'city': row[4], 'country': row[5]} #the different values in the tuple from SQL query
        cursor.close()
        return data
    except sqlite3.Error as e:
        print("Database error: %s" % e)
        return False
    except Exception as e:
        print("Exception in _query: %s" % e)
        return False

def get_user(email):
    try:
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("select email from users where email = ?", [email])
        user = cursor.fetchone()[0]
        if user is not None:
            return True
    except sqlite3.Error as e:
        print("Database error: %s" % e)
        return False
    except Exception as e:
        print("Exception in _query: %s" % e)
        return False

def change_password(email, old_password, new_password):
    try:
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("select password from users where email = ?", [email])
        password = cursor.fetchone()[0]
        if password == old_password: #Check that password in DB is the same as the arg
            cursor.execute("update users set password = ? where email = ? ", [new_password, email])
            connection.commit()
            return True

    except sqlite3.Error as e:
        print("Database error: %s" % e)
        return False
    except Exception as e:
        print("Exception in _query: %s" % e)
        return False


def post_message(message, sender, recipient):
    try:
        if get_user(recipient):
            connection = get_db()
            cursor = connection.cursor()
            cursor.execute("insert into messages (email_sender, message, recipient) values(?,?,?)", [sender,message,recipient])
            connection.commit()
            return True
    except sqlite3.Error as e:
        print("Database error: %s" % e)
        return False
    except Exception as e:
        print("Exception in _query: %s" % e)
        return False

def get_user_messages_by_email(email):
    try:
        if get_user(email):
            connection = get_db()
            cursor = connection.cursor()
            cursor.execute("select * from messages where recipient = ?", [email])
            row = cursor.fetchall()
            message_data = []
            for i in range(len(row)):
                message_data.append({'email_sender': row[i][1], 'message':row[i][2], 'recipient': row[i][3]}) #iterate over all values in the row and add them seperatly in a list
            cursor.close()
            return message_data
    except sqlite3.Error as e:
        print("Database error: %s" % e)
        return False
    except Exception as e:
        print("Exception in _query: %s" % e)
        return False
