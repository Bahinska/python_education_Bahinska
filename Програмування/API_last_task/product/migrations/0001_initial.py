
import django.core.validators
from django.db import migrations, models
import product.validation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='invalid_id', message='It is not a proper id', regex='^[0-9]{9}$')])),
                ('title', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(code='invalid_title', message='It is not a proper title', regex='[A-Z][A-Za-z]{2,25}(\\s[A-Z][A-Za-z]{2,25})?$')])),
                ('image_url', models.CharField(max_length=10000, validators=[django.core.validators.RegexValidator(code='invalid_title', message='It is not a proper title', regex='[A-Z][A-Za-z]{2,25}(\\s[A-Z][A-Za-z]{2,25})?$')])),
                ('price', models.FloatField(validators=[product.validation.validate_decimals])),
                ('created_at', models.DateField(validators=[product.validation.date_validation])),
                ('updated_at', models.DateField(validators=[product.validation.date_validation])),
            ],
        ),
    ]