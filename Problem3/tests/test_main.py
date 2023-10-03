import pytest
from app import app

def user():
    app.config["TEST"] = True

def test_createPost():
    response = user.post("/post", json = {"content" : "Post Content"})
    assert response.status_code == 200
