from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator
from .validation import *
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Product(models.Model):
    """
    Django model for Product
    """
    ID = models.CharField(default='111111111', verbose_name='id', max_length=9, unique=True, primary_key=True, validators=[
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


class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class UserData(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin'
        USER = 'user'

    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(choices=Role.choices, default=Role.USER, max_length=100)

    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']








