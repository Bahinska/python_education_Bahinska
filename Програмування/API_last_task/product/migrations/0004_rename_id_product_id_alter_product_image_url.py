
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='id',
            new_name='ID',
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.CharField(max_length=10000, validators=[django.core.validators.RegexValidator(code='invalid_url', message='It is not a proper url', regex='^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$')], verbose_name='image url'),
        ),
    ]