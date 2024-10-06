from django.urls import path,include
from . import views

urlpatterns = [
    path("flipkart/<product_name>/", views.scrap_product_name),
    path("flipkart/<product_name>/<int:amount>/",views.productscrap_amount)
]
