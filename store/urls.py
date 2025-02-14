from django.urls import path
from .views import create_category, update_category,get_category_by_id, delete_category, create_product, update_product,get_product_by_id, delete_product, create_order, update_order,get_order_by_id, delete_order

urlpatterns = [
    path('create_category/', create_category, name='create_category'),
    path('update_category/<int:category_id>/', update_category, name='update_category'),
    path('get_category/<int:category_id>/', get_category_by_id, name='get_category_by_id'),
    path('delete_category/<int:category_id>/', delete_category, name='delete_category'),

    path('create_product/', create_product, name='create_product'),
    path('update_product/<int:product_id>/', update_product, name='update_product'),
    path('get_product/<int:product_id>/', get_product_by_id, name='get_product_by_id'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),

    path('create_order/', create_order, name='create_order'),
    path('update_order/<int:order_id>/', update_order, name='update_order'),
    path('get_order/<int:order_id>/', get_order_by_id, name='get_order_by_id'),
    path('delete_order/<int:order_id>/', delete_order, name='delete_order'),
]

