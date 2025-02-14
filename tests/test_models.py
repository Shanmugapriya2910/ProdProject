import pytest
from store.models import ProductCategory, Product, Order


@pytest.mark.django_db
def test_product_category_creation():
    category = ProductCategory.objects.create(name="Books")
    assert category.name == "Books:"


@pytest.mark.django_db
def test_product_creation():
    category = ProductCategory.objects.create(name="Electronics")
    product = Product.objects.create(name="Laptop", category=category, price=1500.00)
    assert product.name == "Laptop"
    assert product.price == 1500.00


@pytest.mark.django_db
def test_order_creation_and_cost_calculation():
    category = ProductCategory.objects.create(name="Furniture")
    product = Product.objects.create(name="Chair", category=category, price=200.00)
    order = Order.objects.create(customer_name="Alice", product=product, quantity=3)

    assert order.customer_name == 'Alice'
    assert order.product.name == "Chair"
    assert order.quantity == 3
    assert order.cost == 600.00
