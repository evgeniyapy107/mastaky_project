# Generated by Django 5.0.6 on 2024-08-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painting', '0002_aboutpainting_price_aboutpainting_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpainting',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='painting',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]