from django.urls import path, include

from products.views import(
    product_detail_view,
    product_create_view,
    product_dynamic_detail_view,
    product_delete_detail_view,
    product_list_view,

)


app_name = 'products'
urlpatterns = [
    path('product/', product_detail_view, name='product_detail_view'),
    path('', product_list_view, name='product_list_view'),
    path('<int:my_id>/', product_dynamic_detail_view, name='product_dynamic_detail'),
    path('<int:my_id>/delete/', product_delete_detail_view, name='product_delete'),
    path('create/', product_create_view, name='product_create_view'),

]