# Generated by Django 3.2.4 on 2021-06-17 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSI', '0004_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='Image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
