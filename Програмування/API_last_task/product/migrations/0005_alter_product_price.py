
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_id_product_id_alter_product_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(error_messages='not a proper price', validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='price'),
        ),
    ]