# Generated by Django 4.1.2 on 2022-11-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_userdata_is_admin_alter_userdata_date_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='role',
        ),
        migrations.AddField(
            model_name='userdata',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
