# Generated by Django 4.2.13 on 2024-08-07 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('about', '0001_initial'),
        ('profile_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_profile', to='profile_page.profile'),
        ),
    ]
