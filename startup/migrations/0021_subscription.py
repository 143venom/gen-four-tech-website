# Generated by Django 5.0.6 on 2024-07-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0020_featurepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
