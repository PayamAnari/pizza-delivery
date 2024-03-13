# Generated by Django 5.0.3 on 2024-03-13 10:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('SMALL', 'small'), ('MEDIUM', 'medium'), ('LARGE', 'large'), ('EXTRA_LARGE', 'extraLarge')], default='SMALL', max_length=20)),
                ('order_status', models.CharField(choices=[('PENDING', 'pending'), ('IN_TRANSIT', 'inTransit'), ('DELIVERED', 'delivered'), ('CANCELLED', 'cancelled')], default='PENDING', max_length=20)),
                ('quantity', models.IntegerField()),
                ('flavour', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]