import os
import tempfile
import pytest
from server import app
import data_handler
from flask import json


@pytest.fixture
def client():
    db_fd, app.config["DATABASE_FILE_PATH"] = tempfile.mkstemp()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
                                app.config["DATABASE_FILE_PATH"]
    app.config["TESTING"] = True

    client = app.test_client()

    with app.app_context():
        data_handler.init_db()

    yield client

    os.close(db_fd)
    os.unlink(app.config["DATABASE_FILE_PATH"])


def test_empty_db(client):
    r = client.get("/")
    assert b"Hello World!" in r.data

def test_post_comment_on_user(client):
    payload = { "message": "get this message",
                "username": "Robin",
                "password": "123",
                "group": "najs",
	            "location": "Din pappa",
                "userName": "Robin",
                "groupName": "najs"
               }
    
    r = client.post("/user", json=payload, content_type="application/json")
    r2 = client.post("/login", json=payload, content_type="application/json")
    token = json.loads(r2.data.decode(encoding="utf-8"))["access_token"]
    r3 = client.post("/group", json=payload,
                    content_type="application/json",
                    headers={"access_token": token})
    r4 = client.post("/group/najs/add/Robin", json=payload,
                    content_type="application/json",
                    headers={"access_token": token})
    r5 = client.post("/group/comment/username", json=payload,
                    content_type="application/json",
                    headers={"access_token": token})
    r6 = client.get("/najs/comment/Robin", headers={"access_token": token})
    post_comment = json.loads(r6.data.decode(encoding="utf-8"))["comments"]
    assert len(post_comment) == 1





def test_get_group(client):
    payload = {"username": "Robin",
                "password":"123",
                "group": "najs"
                }
    r = client.post("/user", json=payload, content_type="application/json")
    r2 = client.post("/login", json=payload, content_type="application/json")
    token = json.loads(r2.data.decode(encoding="utf-8"))["access_token"]
    r3 = client.post("/group", json=payload,
                    content_type="application/json",
                    headers={"access_token": token})
    group = json.loads(r3.data.decode(encoding="utf-8"))["group"]

    assert group == "najs"

def test_new_user(client):
    payload = {"username": "Robin",
               "password": "123"}

    r = client.post("/user", json=payload, content_type="application/json")
    username = json.loads(r.data.decode(encoding="utf-8"))["username"]
    assert len(username) == 5

def test_user_in_group(client):
    payload = {"username": "Robin",
               "password": "123",
               "group": "najs"

           }
    r = client.post("/user", json=payload, content_type="application/json")
    r2 = client.post("/login", json=payload, content_type="application/json")
    token = json.loads(r2.data.decode(encoding="utf-8"))["access_token"]
    r3 = client.post("/group", json=payload,
                    content_type="application/json",
                    headers={"access_token": token})
    r4 = client.get("/group/users/najs",  headers={"access_token": token})
    user = json.loads(r4.data.decode(encoding="utf-8"))["users"]
    assert user == [{'username': 'Robin'}]





def test_login(client):
    payload = {"username": "Robin",
               "password": "123"
               }
    r = client.post("/user", json=payload, content_type="application/json")
    r2 = client.post("/login", json=payload, content_type="application/json")
    token = json.loads(r2.data.decode(encoding="utf-8"))["access_token"]
    assert len(token) > 200
