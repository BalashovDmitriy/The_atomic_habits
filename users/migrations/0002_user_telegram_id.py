# Generated by Django 4.2.7 on 2023-12-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
