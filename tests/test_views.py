import pytest
import base64
from django.urls import reverse
from store.models import ProductCategory, Product, Order
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_category_view(api_client):

    url = reverse("create_category")
    response = api_client.post(url, {"name": "Books"}, format="json")
    assert response.status_code == 201
    assert response.json()["name"] == "Books"

@pytest.mark.django_db
def test_update_category_view(api_client, product_category):

    url = reverse("update_category", args=[product_category.id])
    response = api_client.put(url, {"name": "Updated Category"}, format="json")
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Category"

@pytest.mark.django_db
def test_get_category_by_id_view(api_client, product_category):

    url = reverse("get_category_by_id", args=[product_category.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()["name"] == product_category.name

@pytest.mark.django_db
def test_delete_category_view(api_client, product_category):

    url = reverse("delete_category", args=[product_category.id])
    response = api_client.delete(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_product_view(api_client, product_category):

    url = reverse("create_product")
    response = api_client.post(
        url, {"name": "Smartphone", "category_id": product_category.id, "price": 699.99}, format="json"
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Smartphone"

@pytest.mark.django_db
def test_update_product_view(api_client, product):

    url = reverse("update_product", args=[product.id])
    response = api_client.put(url, {"name": "Updated Smartphone", "price": 799.99}, format="json")
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Smartphone"

@pytest.mark.django_db
def test_get_product_by_id_view(api_client, product):

    url = reverse("get_product_by_id", args=[product.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()["name"] == product.name

@pytest.mark.django_db
def test_delete_product_view(api_client, product):

    url = reverse("delete_product", args=[product.id])
    response = api_client.delete(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_order_view(api_client, product):

    url = reverse("create_order")
    response = api_client.post(
        url, {"customer_name": "Jane Doe", "product_id": product.id, "quantity": 3}, format="json"
    )
    assert response.status_code == 201
    assert response.json()["customer_name"] == "Jane Doe"

@pytest.mark.django_db
def test_update_order_view(api_client, order):

    url = reverse("update_order", args=[order.id])
    response = api_client.put(url, {"customer_name": "Updated Name", "quantity": 4}, format="json")
    assert response.status_code == 200
    assert response.json()["customer_name"] == "Updated Name"

@pytest.mark.django_db
def test_get_order_by_id_view(api_client, order):

    url = reverse("get_order_by_id", args=[order.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()["customer_name"] == order.customer_name

@pytest.mark.django_db
def test_delete_order_view(api_client, order):

    url = reverse("delete_order", args=[order.id])
    response = api_client.delete(url)
    assert response.status_code == 200
