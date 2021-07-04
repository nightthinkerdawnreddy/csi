# Generated by Django 3.2.4 on 2021-06-22 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSI', '0007_individualeventspics_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='academicyear20_21',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images/')),
                ('eventnumber', models.IntegerField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CSI.year')),
            ],
        ),
    ]