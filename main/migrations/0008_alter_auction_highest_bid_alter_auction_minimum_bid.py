# Generated by Django 5.1.1 on 2024-11-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_item_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='highest_bid',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='auction',
            name='minimum_bid',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
