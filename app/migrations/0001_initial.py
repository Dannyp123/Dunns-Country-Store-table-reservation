# Generated by Django 2.2 on 2019-04-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('p_number', models.IntegerField()),
                ('num_of_people', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
