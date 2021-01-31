# Generated by Django 3.1.5 on 2021-01-31 17:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('needley', '0003_auto_20210131_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avator',
            field=models.URLField(null=True, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
