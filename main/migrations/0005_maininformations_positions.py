# Generated by Django 5.1.4 on 2024-12-29 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_maininformations_current_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='maininformations',
            name='positions',
            field=models.TextField(null=True, verbose_name='Positions'),
        ),
    ]
