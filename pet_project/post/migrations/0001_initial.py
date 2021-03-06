# Generated by Django 2.2.9 on 2020-03-03 20:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_auto_20200227_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interests', models.CharField(max_length=150)),
                ('working_style', models.TextField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('photo_with_pets', models.ImageField(blank=True, upload_to='profile_pics')),
                ('pet_lover', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
    ]
