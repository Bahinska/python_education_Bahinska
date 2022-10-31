from django.contrib import admin
from django.urls import path, include

from product.views import *

app_name = 'product'
urlpatterns = [
    path('products', ProductListView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view()),

]
#urlpatterns = format_suffix_patterns(urlpatterns)
