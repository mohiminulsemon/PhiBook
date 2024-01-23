# Generated by Django 4.2.7 on 2024-01-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userdetails_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/static/profile_pics/'),
        ),
    ]