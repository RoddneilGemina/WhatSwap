# Generated by Django 5.1.1 on 2024-11-04 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_offer_description_offer_offer_desc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='offer_item_name',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='offer_owner',
        ),
        migrations.AddField(
            model_name='offer',
            name='offer_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.item'),
        ),
    ]