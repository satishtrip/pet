# Generated by Django 2.2.9 on 2020-05-01 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petcab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petcab',
            name='status',
            field=models.CharField(choices=[('Booked', 'Booked'), ('Pending', 'Pending')], default='Pending', max_length=7),
        ),
    ]