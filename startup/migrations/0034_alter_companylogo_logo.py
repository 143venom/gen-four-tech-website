# Generated by Django 4.1.13 on 2024-07-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0033_companylogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companylogo',
            name='logo',
            field=models.ImageField(default='defaultvendor.jpg', upload_to='company_logo'),
        ),
    ]
