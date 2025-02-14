import pytest
import base64
from django.test import RequestFactory


def test_middleware_with_valid_auth(valid_auth_request, middleware):
    response = middleware(valid_auth_request)
    assert valid_auth_request.headers["Authorization"] is not None
    assert response is valid_auth_request


def test_middleware_with_invalid_auth(middleware):
    factory = RequestFactory()
    request = factory.post("/create_order/")

    request.headers = {"Authorization": "Basic invalidcredentials"}
    response = middleware(request)

    assert response.status_code == 401


def test_middleware_missing_auth_header(middleware):

    factory = RequestFactory()
    request = factory.post("/create_order/")
    response = middleware(request)
    assert response.status_code == 401

