# Generated by Django 4.1.13 on 2024-07-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0030_quality_remove_about_sections_about_qualities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quality',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
