# Generated by Django 5.1.3 on 2024-12-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_profile_image_url_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer_status',
            field=models.CharField(choices=[('CLOSED', 'Closed'), ('PENDING', 'Pending'), ('STANDBY', 'Standby'), ('REJECTED', 'Rejected')], default='STANDBY', max_length=20),
        ),
    ]