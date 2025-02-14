# Generated by Django 4.1.13 on 2024-07-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0025_alter_price_time_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='price',
            name='features_need',
        ),
        migrations.RemoveField(
            model_name='price',
            name='features_noneed',
        ),
        migrations.AddField(
            model_name='price',
            name='features_need',
            field=models.ManyToManyField(related_name='needed_in_plans', to='startup.feature'),
        ),
        migrations.AddField(
            model_name='price',
            name='features_noneed',
            field=models.ManyToManyField(blank=True, related_name='not_needed_in_plans', to='startup.feature'),
        ),
    ]
