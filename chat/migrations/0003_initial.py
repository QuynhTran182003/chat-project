# Generated by Django 5.0 on 2024-01-06 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=64, unique=True)),
                ('Password', models.CharField(max_length=64)),
                ('Name', models.CharField(max_length=64)),
                ('Surname', models.CharField(max_length=64)),
            ],
        ),
    ]
