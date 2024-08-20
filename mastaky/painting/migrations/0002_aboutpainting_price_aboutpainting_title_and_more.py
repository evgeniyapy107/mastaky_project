# Generated by Django 5.0.6 on 2024-08-14 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpainting',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AddField(
            model_name='aboutpainting',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='painting',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
