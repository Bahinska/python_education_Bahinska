
import django.core.validators
from django.db import migrations, models
import product.validation


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(validators=[product.validation.date_validation], verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_id', message='It is not a proper id', regex='^[0-9]{9}$')], verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.CharField(max_length=10000, validators=[django.core.validators.RegexValidator(code='invalid_title', message='It is not a proper title', regex='[A-Z][A-Za-z]{2,25}(\\s[A-Z][A-Za-z]{2,25})?$')], verbose_name='image url'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[product.validation.validate_decimals], verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(code='invalid_title', message='It is not a proper title', regex='[A-Z][A-Za-z]{2,25}(\\s[A-Z][A-Za-z]{2,25})?$')], verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateField(validators=[product.validation.date_validation], verbose_name='updated date'),
        ),
    ]