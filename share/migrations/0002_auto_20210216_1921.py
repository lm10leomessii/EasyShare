# Generated by Django 3.1.3 on 2021-02-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file_field',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]