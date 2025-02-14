from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ProductCategory, Product, Order

@csrf_exempt
def create_category(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        category = ProductCategory.objects.create(name=name)
        return JsonResponse({"id": category.id, "name": category.name}, status=201)
    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def update_category(request, category_id):
    if request.method == "PUT":
        category = get_object_or_404(ProductCategory, id=category_id)
        data = json.loads(request.body)
        name = data.get("name", category.name)
        category.name = name
        category.save()
        return JsonResponse({"id": category.id, "name": category.name})
    return JsonResponse({"error": "Invalid request method"}, status=400)


def get_category_by_id(request, category_id):
    category = get_object_or_404(ProductCategory, id=category_id)
    return JsonResponse({"id": category.id, "name": category.name})


@csrf_exempt
def delete_category(request, category_id):
    if request.method == "DELETE":
        category = get_object_or_404(ProductCategory, id=category_id)
        category.delete()
        return JsonResponse({"message": "Category deleted successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def create_product(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        category_id = data.get("category_id")
        price = data.get("price")
        category = get_object_or_404(ProductCategory, id=category_id)
        product = Product.objects.create(name=name, category=category, price=price)
        return JsonResponse({"id": product.id, "name": product.name, "category": product.category.name, "price": product.price}, status=201)
    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def update_product(request, product_id):
    if request.method == "PUT":
        product = get_object_or_404(Product, id=product_id)
        data = json.loads(request.body)
        name = data.get("name", product.name)
        category_id = data.get("category_id", product.category.id)
        price = data.get("price", product.price)
        category = get_object_or_404(ProductCategory, id=category_id)
        product.name = name
        product.category = category
        product.price = price
        product.save()
        return JsonResponse({"id": product.id, "name": product.name, "category": product.category.name, "price": product.price})
    return JsonResponse({"error": "Invalid request method"}, status=400)


def get_product_by_id(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return JsonResponse({"id": product.id, "name": product.name, "category": product.category.name, "price": product.price})


@csrf_exempt
def delete_product(request, product_id):
    if request.method == "DELETE":
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return JsonResponse({"message": "Product deleted successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def create_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        customer_name = data.get("customer_name")
        product_id = data.get("product_id")
        quantity = data.get("quantity")
        product = get_object_or_404(Product, id=product_id)
        order = Order.objects.create(customer_name=customer_name, product=product, quantity=quantity)
        return JsonResponse({
            "order_id": order.id,
            "customer_name": order.customer_name,
            "product": order.product.name,
            "quantity": order.quantity,
            "cost": order.cost
        }, status=201)
    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def update_order(request, order_id):
    if request.method == "PUT":
        order = get_object_or_404(Order, id=order_id)
        data = json.loads(request.body)
        customer_name = data.get("customer_name", order.customer_name)
        product_id = data.get("product_id", order.product.id)
        quantity = data.get("quantity", order.quantity)
        product = get_object_or_404(Product, id=product_id)
        order.customer_name = customer_name
        order.product = product
        order.quantity = quantity
        order.save()
        return JsonResponse({
            "order_id": order.id,
            "customer_name": order.customer_name,
            "product": order.product.name,
            "quantity": order.quantity,
            "cost": order.cost
        })
    return JsonResponse({"error": "Invalid request method"}, status=400)


def get_order_by_id(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return JsonResponse({
        "order_id": order.id,
        "customer_name": order.customer_name,
        "product": order.product.name,
        "quantity": order.quantity,
        "cost": order.cost
    })


@csrf_exempt
def delete_order(request, order_id):
    if request.method == "DELETE":
        order = get_object_or_404(Order, id=order_id)
        order.delete()
        return JsonResponse({"message": "Order deleted successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=400)

