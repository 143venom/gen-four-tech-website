# Generated by Django 4.1.13 on 2024-07-03 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0014_alter_about_sections'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]
