# Generated by Django 4.2.13 on 2024-07-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('0', 'Draft'), ('1', 'Publish')], default=0),
        ),
    ]
