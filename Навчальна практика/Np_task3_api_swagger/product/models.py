from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from .validation import *


class Product(models.Model):
    """
    Django model for Product
    """
    ID = models.CharField(verbose_name='id', max_length=9, unique=True, primary_key=True, validators=[
        RegexValidator(
            regex='^[0-9]{9}$',
            message='It is not a proper id',
            code='invalid_id'
        )
    ])
    title = models.CharField(verbose_name='title', max_length=40, validators=[
        RegexValidator(
            regex='[A-Z][A-Za-z]{2,25}(\s[A-Z][A-Za-z]{2,25})?$',
            message='It is not a proper title',
            code='invalid_title'
        )
    ])
    image_url = models.CharField(verbose_name='image url', max_length=10000, validators=[
        RegexValidator(
            regex='^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$',
            message='It is not a proper url',
            code='invalid_url'
        )])
    price = models.FloatField(verbose_name='price', error_messages="not a proper price", validators=[
        MinValueValidator(0.0)
    ])
    created_at = models.DateField(verbose_name='created date')
    updated_at = models.DateField(verbose_name='updated date')








