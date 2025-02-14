import pytest
from rest_framework.test import APIClient
import base64
from django.contrib.auth.models import User
from store.models import ProductCategory, Product, Order


@pytest.fixture
def api_client():
    client = APIClient()

    user, _ = User.objects.get_or_create(username="admin")
    user.set_password("password")
    user.save()


    credentials = base64.b64encode(b"admin:password").decode("utf-8")
    client.credentials(HTTP_AUTHORIZATION=f"Basic {credentials}")
    return client


@pytest.fixture
def product_category():
    return ProductCategory.objects.create(name="Electronics")


@pytest.fixture
def product(product_category):
    return Product.objects.create(name="Laptop", category=product_category, price=1000.00)


@pytest.fixture
def order(product):
    return Order.objects.create(customer_name="John Doe", product=product, quantity=2)


@pytest.fixture
def valid_auth_request():
    from django.test import RequestFactory
    factory = RequestFactory()
    request = factory.post("/create_order/")
    credentials = base64.b64encode(b"admin:password").decode("utf-8")
    request.headers = {"Authorization": f"Basic {credentials}"}
    return request


@pytest.fixture
def middleware():
    from store.middleware import BasicAuthMiddleware

    def dummy_get_response(request):
        return request
    return BasicAuthMiddleware(dummy_get_response)
