"""
Use a fixture to perform the prepare- and action phrase. Then each test
will assert just once.
"""

import http

import pytest
import requests

# ======================================================================


@pytest.fixture(scope="module")
def response():
    """Perform the action and return the response."""
    return requests.get("https://jsonplaceholder.typicode.com/posts/1")


@pytest.fixture(scope="module")
def payload(response):
    """
    Return the payload part

    Sample payload:

        {
            "userId": 1,
            "id": 1,
            "title": "sunt aut ...",
            "body": "quia et ..."
        }
    """
    return response.json()


# ======================================================================


def test_status_code(response):
    assert response.status_code == http.HTTPStatus.OK


def test_ok(response):
    assert response.ok


def test_userid(payload):
    assert payload["userId"] == 1


def test_id(payload):
    assert payload["id"] == 1


def test_title(payload):
    assert payload["title"]


def test_body(payload):
    assert payload["body"]


def test_content_type(response: requests.Response):
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_redirect(response: requests.Response):
    assert response.is_redirect is False


def test_no_cookie(response: requests.Response):
    assert len(response.cookies) == 0
