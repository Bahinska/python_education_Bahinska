# Generated by Django 4.1.2 on 2022-11-11 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_userdata_name_alter_userdata_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], default='user', max_length=100),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
