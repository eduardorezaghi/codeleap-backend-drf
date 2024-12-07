# Generated by Django 5.1.3 on 2024-12-02 22:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_datetime'],
            },
        ),
    ]
