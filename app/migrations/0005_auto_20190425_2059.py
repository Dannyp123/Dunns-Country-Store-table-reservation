# Generated by Django 2.2 on 2019-04-25 20:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190424_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablereservation',
            name='p_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\s*(?:\\+?(\\d{1,3}))?[-. (]*(\\d{3})[-. )]*(\\d{3})[-. ]*(\\d{4})(?: *x(\\d+))?\\s*$')]),
        ),
    ]
