# Generated by Django 4.1.7 on 2023-04-20 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_service_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_description',
            field=models.TextField(blank=True),
        ),
    ]
