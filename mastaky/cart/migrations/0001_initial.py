# Generated by Django 5.0.6 on 2024-09-11 07:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('painting', '0003_alter_aboutpainting_price_alter_painting_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('comment', models.TextField(blank=True, null=True)),
                ('payment_method', models.CharField(choices=[('cash', 'Наличными при получении'), ('erip', 'Через систему ЕРИП')], max_length=10)),
                ('delivery_method', models.CharField(choices=[('pickup', 'Самовывоз'), ('post', 'Почта'), ('courier', 'Курьер')], max_length=10)),
                ('delivery_date', models.DateField()),
                ('delivery_time', models.CharField(choices=[('morning', 'Утро'), ('afternoon', 'День'), ('evening', 'Вечер')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.order')),
                ('painting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='painting.painting')),
            ],
        ),
    ]
