# Generated by Django 4.2.13 on 2024-08-07 10:23

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', django_quill.fields.QuillField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
