# Generated by Django 2.2.2 on 2019-06-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20190610_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
