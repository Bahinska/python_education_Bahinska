from django.contrib import admin
from django.urls import path, include
from product.views import *
from .swagger import schema_view

app_name = 'product'
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),

]
#urlpatterns = format_suffix_patterns(urlpatterns)
