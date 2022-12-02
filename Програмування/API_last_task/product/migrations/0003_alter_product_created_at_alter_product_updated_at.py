
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_created_at_alter_product_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateField(verbose_name='updated date'),
        ),
    ]